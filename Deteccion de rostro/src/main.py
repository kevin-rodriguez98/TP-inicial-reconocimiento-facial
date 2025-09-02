from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import cv2, numpy as np
from pathlib import Path

app = FastAPI()

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
        if recognizer and label_map:
            roi_resized = cv2.resize(roi_gray, (200, 200))
            label_id, conf = recognizer.predict(roi_resized)
            if label_id in label_map and conf < 80:
                msg = f"✅ Validado: {label_map[label_id]} (conf={conf:.1f})"
        response.append({"x": int(x), "y": int(y), "w": int(w), "h": int(h), "message": msg})

    return {"faces": response}