# src/app_gradio.py
import cv2
import time
import gradio as gr
import numpy as np
from pathlib import Path

ultimo_log = None
hora_log = None
# --- Modelos (Haar + LBPH opcional) ---
HAAR_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(HAAR_PATH)
if face_cascade.empty():
    raise RuntimeError(f"No se pudo cargar Haar en: {HAAR_PATH}")

MODEL_PATH = Path("data/modelos/lbph.yml")
LABELS_PATH = Path("data/modelos/label_map.npy")
recognizer = None
label_map = {}

def load_lbph():
    global recognizer, label_map
    if MODEL_PATH.exists():
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(str(MODEL_PATH))
    if LABELS_PATH.exists():
        label_map = np.load(str(LABELS_PATH), allow_pickle=True).item()

load_lbph()

# --- Detección + Validación ---
def detectar_y_validar(frame_rgb, start_detection: bool):
    global ultimo_log, hora_log
    if frame_rgb is None:
        return None, "Esperando permiso de cámara…",start_detection,gr.update()

    # RGB -> BGR
    bgr = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

    if hora_log and (time.time() - hora_log < 5):
        return cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB), ultimo_log, False, gr.update(value="Comenzar reconocimiento")

    if not start_detection:
        msg = "Captura pausada (clic en Iniciar)"
        cv2.putText(bgr, msg, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2, cv2.LINE_AA)
        return cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB), msg,False,gr.update(value="Comenzar reconocimiento")

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=5, minSize=(80, 80))
    if isinstance(faces, np.ndarray):
        faces = faces.tolist()
    if faces is None or len(faces) == 0:
        return cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB), "Sin rostros",True,gr.update(value="Comenzar reconocimiento")

    logs = []
    for (x, y, w, h) in faces:
        x, y, w, h = map(int, (x, y, w, h))
        roi_gray = gray[y:y+h, x:x+w]
        color = (0, 0, 255)
        msg = "❌ Persona no reconocida"

        if recognizer is not None and label_map:
            roi_resized = cv2.resize(roi_gray, (200, 200))
            label_id, conf = recognizer.predict(roi_resized)  # menor = mejor
            if (label_id in label_map) and (conf < 80):
                nombre = label_map[label_id]  # ej: "101_Juan_Perez"
                msg = f"✅ Validado correctamente: {nombre} (conf={conf:.1f})"
                color = (0, 200, 0)
                print(msg)  # consola
                cv2.rectangle(bgr, (x, y), (x + w, y + h), color, 2)
                cv2.putText(bgr, msg, (x, max(20, y - 10)),cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2, cv2.LINE_AA)
                logs.append(msg)
                out_rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
                ultimo_log = msg
                hora_log = time.time()
                gr.Error("custom message")
                return  out_rgb,"\n".join(logs),False,gr.update(value="Comenzar reconocimiento")

            else:
                msg = f"❌ Persona no reconocida (conf={conf:.1f})"
                print("❌ Persona no reconocida")
        else:
            msg = "Rostro detectado (modelo no cargado)"
            print(msg)

        cv2.rectangle(bgr, (x, y), (x + w, y + h), color, 2)
        cv2.putText(bgr, msg, (x, max(20, y - 10)),cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2, cv2.LINE_AA)
        logs.append(msg)
    out_rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    return out_rgb, "\n".join(logs) if logs else "Prosesando...",True,gr.update(value="Detener Captura")

# --- UI: cámara pequeña + salida grande ---
def toggle_and_label(s: bool):
    s = not s
    return s, gr.update(value=("Detener captura" if s else "Comenzar reconocimiento"))

def app():
    with gr.Blocks(title="Reconocimiento Facial") as demo:
        gr.Markdown("Presiona el Boton para iniciar reconocimiento")

        start_state = gr.State(False)

        with gr.Row():
            btn_toggle = gr.Button("Comenzar reconocimiento", scale=0)
        with gr.Row():
            out_img = gr.Image(label="Salida procesada", height=480, scale=5)
        with gr.Row():
            with gr.Column(scale=8):
                out_log = gr.Textbox(label="Log", lines=7)
            with gr.Column(scale=1):
                cam = gr.Image(sources=["webcam"], label="Entrada", height=200)

       

        btn_toggle.click(fn=toggle_and_label, inputs=start_state, outputs=[start_state, btn_toggle])

        cam.stream(
            fn=detectar_y_validar,
            inputs=[cam, start_state],
            outputs=[out_img, out_log, start_state, btn_toggle]
        )

    demo.launch()

if __name__ == "__main__":
    app()
