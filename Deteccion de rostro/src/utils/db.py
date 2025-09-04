import sqlite3
from pathlib import Path
from datetime import datetime, timedelta

DB_PATH = Path("data/db/attendance.db")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

DDL = """
PRAGMA journal_mode=WAL;
CREATE TABLE IF NOT EXISTS employees (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS attendance (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  employee_id TEXT NOT NULL,
  employee_name TEXT NOT NULL,
  ts_utc TEXT NOT NULL,      -- ISO 8601 UTC
  event TEXT NOT NULL,
  FOREIGN KEY(employee_id) REFERENCES employees(id)
);
CREATE INDEX IF NOT EXISTS idx_att_by_emp_ts ON attendance(employee_id, ts_utc);
"""

def get_conn():
    conn = sqlite3.connect(DB_PATH, timeout=5, isolation_level=None)
    conn.execute("PRAGMA foreign_keys=ON;")
    return conn

def init_db():
    conn = get_conn()
    try:
        for stmt in DDL.strip().split(";"):
            s = stmt.strip()
            if s:
                conn.execute(s)
    finally:
        conn.close()

def parse_label(label: str):
    if not label:
        return None, None
    clean = label.replace("-", "_")
    parts = clean.split("_")
    if len(parts) >= 2:
        emp_id = parts[0]
        name = " ".join(parts[1:]).strip().replace("  ", " ")
        return emp_id, name
    return label, label

def get_last_event(emp_id: str, days: int = 1):
    if not emp_id:
        return None
    dt_from = (datetime.utcnow() - timedelta(days=days)).isoformat(timespec="seconds")
    conn = get_conn()
    try:
        row = conn.execute(
            "SELECT event, ts_utc FROM attendance "
            "WHERE employee_id=? AND ts_utc>=? "
            "ORDER BY ts_utc DESC LIMIT 1",
            (emp_id, dt_from)
        ).fetchone()
        if row:
            return {"event": row[0], "ts_utc": row[1]}
        return None
    finally:
        conn.close()

def infer_event_type(emp_id: str) -> str:
    last = get_last_event(emp_id, days=1)
    if not last or last["event"] in (None, "EGRESO"):
        return "INGRESO"
    return "EGRESO"

def upsert_employee(emp_id: str, name: str):
    if not emp_id:
        return
    conn = get_conn()
    try:
        conn.execute(
            "INSERT INTO employees(id, name) VALUES(?, ?) "
            "ON CONFLICT(id) DO UPDATE SET name=excluded.name;",
            (emp_id, name)
        )
    finally:
        conn.close()

def fetch_attendance_today():
    """Registros de asistencia de la fecha actual (UTC)."""
    today = datetime.now().date()
    start = datetime(today.year, today.month, today.day)
    end = start.replace(hour=0, minute=0, second=0) + timedelta(days=1)

    conn = get_conn()
    try:
        rows = conn.execute(
            "SELECT employee_id, employee_name, ts_utc, event "
            "FROM attendance "
            "WHERE ts_utc >= ? AND ts_utc < ? "
            "ORDER BY ts_utc DESC",
            (start.isoformat(timespec='seconds'), end.isoformat(timespec='seconds'))
        ).fetchall()
        cols = ["employee_id", "employee_name", "ts_utc", "event"]
        return [dict(zip(cols, r)) for r in rows]
    finally:
        conn.close()

def save_attendance(emp_id: str, name: str, event: str) -> int:
    ts = datetime.now().isoformat(timespec="seconds")
    conn = get_conn()
    try:
        upsert_employee(emp_id, name)
        cur = conn.execute(
            "INSERT INTO attendance(employee_id, employee_name, ts_utc, event) "
            "VALUES(?,?,?,?)",
            (emp_id, name, ts, event)
        )
        return cur.lastrowid
    finally:
        conn.close()
