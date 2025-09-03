# TP-inicial-reconocimiento-facial

📊 Análisis de Producción y Asistencia

Este proyecto permite analizar datos de producción, empleados y asistencia en una panadería/repostería ficticia.
Mediante un menú interactivo, se pueden generar visualizaciones y estadísticas sobre la producción diaria, desperdicio, desempeño de empleados y asistencia.

🛠️ Tecnologías utilizadas

Python 3.9+
pandas → manejo y análisis de datos tabulares
matplotlib → generación de gráficos
seaborn → visualización estadística avanzada

📂 Estructura del proyecto

Datos de Producción: información sobre cantidad producida, desperdicio, tiempo operativo y empleados asignados.
Datos de Empleados: registro de legajos, nombres, puestos, turnos y sectores.
Datos de Asistencia: control de ingreso, salida, horas trabajadas y posibles fraudes.
Menú interactivo: permite acceder a distintos análisis y gráficos.

📋 Funcionalidades principales

📈 Producción total diaria (todos los productos)

📊 Producción promedio por producto

🥖 Desperdicio total vs producción efectiva

🚮 Porcentaje de desperdicio por producto

👨‍🍳 Producción promedio diaria por empleado

🔄 Promedio de asignación de empleados por producto

⏱️ Promedio de horas trabajadas por empleado

⚠️ Intentos de fraude o irregularidades en asistencia

📤 Exportación de datos a Excel

❌ Salir del sistema

▶️ Pasos para ejecutar el proyecto
1. Clonar o descargar el repositorio

2. Crear y activar un entorno virtual
python -m venv 

3. Instalar dependencias necesarias
pip install pandas matplotlib seaborn openpyxl

4. Ejecutar el script
python visualizacion.py
