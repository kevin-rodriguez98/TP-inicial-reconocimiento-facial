Reconocimiento Facial con OpenCV y Gradio

Este proyecto es un prototipo de control de asistencia para una PYME alimenticia.
Utiliza OpenCV para la detección y validación de rostros mediante el algoritmo LBPH (Local Binary Patterns Histograms) y una interfaz web construida con Gradio.

🚀 ¿Cómo funciona?

1 La cámara captura el rostro del empleado.

2 Con el modelo Haarcascade se detecta el área de la cara.

3 Si existe un modelo entrenado con LBPH, se compara y se valida la identidad del empleado.

4 Una vez validado, el sistema muestra en la interfaz el nombre del empleado y en consola se imprime el resultado.

5 La sesión de captura se detiene automáticamente después de la validación.

Estructura del Proyecto

├── src/
│   ├── app_gradio.py               # Interfaz principal en Gradio
│   └── enroll_lbph.py              # funciones de entrenamiento
├── data/
│   ├── empleados/
│   │   └── ID_name_lastname       # Carpeta de fotos del empleado
│   │       ├── img1.png            # Foto del empleado
│   │       └── img2.png            # Foto del empleado
│   └── modelos/
│       ├── lbph.yml                # Modelo entrenado
│       └── label_map.npy           # Diccionario de etiquetas
└── README.md

⚙️ Requisitos:

    - Python 3.9 o superior
    - pip install opencv-contrib-python numpy

🧪 Entrenamiento del modelo (LBPH)

    1 Agrega las fotos por empleado (frontal, bien iluminadas) en:

        data/empleados/
        ├─ ID_NAME_LASTNAME/
        │ ├─ img1.jpg

    2 Entrená el modelo:

        python -m src.enroll_lbph
        
        se generaran los archivos data/modelos/lbph.yml y data/modelos/label_map.npy


▶️ Cómo levantar la aplicación

    1 Desde la raíz del proyecto, ejecutá:

    - python -m src.app_gradio

    2 Por defecto, la aplicación se abre en:

    - http://127.0.0.1:7860

Como inicar el reconocimiento facial en el navegador:

Pasos de unica vez: 

    1 Brindar permisos de camara

    2 Encender camara -> click en "Click to Access WebCam"

    3 Iniciar capura de imagen -> click "Grabar"

Comenzar con el reconocimiento facial:

    - Comenzar reconocimiento  -> click en boton: "Comenzar reconocimiento"

--------------------------------------------------------------------------------------

uvicorn src.app_api:app --reload
levantar el backend primero y luego abrir index.html en el navegador.