from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import cv2, numpy as np
from pathlib import Path
from src.utils import db
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/app",StaticFiles(directory="src/web",html=True),name="static")

# Permitir requests desde cualquier frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Modelos ---
HAAR_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(HAAR_PATH)
MODEL_PATH = Path("data/modelos/lbph.yml")
LABELS_PATH = Path("data/modelos/label_map.npy")
recognizer = None
label_map = {}

if MODEL_PATH.exists():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(str(MODEL_PATH))
if LABELS_PATH.exists():
    label_map = np.load(str(LABELS_PATH), allow_pickle=True).item()

db.init_db()

@app.post("/detect")
async def detect_face(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(80, 80))
    response = []

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        msg = "❌ Persona no reconocida"
        saved = False 
        emp_id = None
        emp_name = None
        event = None  
        if recognizer and label_map:
            roi_resized = cv2.resize(roi_gray, (200, 200))
            label_id, conf = recognizer.predict(roi_resized)

            if label_id in label_map and conf < 80:
                label_txt = label_map[label_id] 
                msg = f"✅ Validado: {label_txt} (conf={conf:.1f})"
                emp_id, emp_name = db.parse_label(label_txt)
                event = db.infer_event_type(emp_id)

                #if emp_id and not db.last_attendance_within(emp_id, minutes=0):
                rowid = db.save_attendance(emp_id, emp_name, event)
                saved = True
                print(f"[DB] attendance id={rowid} emp={emp_id} {emp_name} {event}")
                #else: print("[DB] duplicado evitado")

        response.append({"x": int(x), "y": int(y), "w": int(w), "h": int(h), "message": msg, "saved": saved, "employee_id": emp_id, "employee_name": emp_name, "event":event})

    return {"faces": response}

@app.get("/attendance/today")
def attendance_today():
    return db.fetch_attendance_today()