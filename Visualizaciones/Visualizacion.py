import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#  PRODUCCIÓN 

produccion = [
    {"IDProduccion": 1, "Fecha": "2025-08-01", "Producto": "Galletas", "CantidadProducida": 1820, "Desperdicio": 96, "TiempoOperativo": "7h", "EmpleadosAsignados": [101, 102]},
    {"IDProduccion": 2, "Fecha": "2025-08-01", "Producto": "Pan", "CantidadProducida": 1660, "Desperdicio": 63, "TiempoOperativo": "5h50m", "EmpleadosAsignados": [103]},
    {"IDProduccion": 3, "Fecha": "2025-08-01", "Producto": "Tortas", "CantidadProducida": 870, "Desperdicio": 12, "TiempoOperativo": "6h30m", "EmpleadosAsignados": [104, 105]},
    {"IDProduccion": 4, "Fecha": "2025-08-01", "Producto": "Facturas", "CantidadProducida": 1886, "Desperdicio": 39, "TiempoOperativo": "5h1m", "EmpleadosAsignados": [106]},
    {"IDProduccion": 5, "Fecha": "2025-08-01", "Producto": "Bizcochuelos", "CantidadProducida": 1624, "Desperdicio": 63, "TiempoOperativo": "6h40m", "EmpleadosAsignados": [107, 108]},

    {"IDProduccion": 6, "Fecha": "2025-08-02", "Producto": "Pan", "CantidadProducida": 1740, "Desperdicio": 55, "TiempoOperativo": "6h10m", "EmpleadosAsignados": [103, 109]},
    {"IDProduccion": 7, "Fecha": "2025-08-02", "Producto": "Facturas", "CantidadProducida": 1902, "Desperdicio": 44, "TiempoOperativo": "5h20m", "EmpleadosAsignados": [110]},
    {"IDProduccion": 8, "Fecha": "2025-08-02", "Producto": "Galletas", "CantidadProducida": 1785, "Desperdicio": 81, "TiempoOperativo": "6h50m", "EmpleadosAsignados": [101, 111]},
    
    {"IDProduccion": 9, "Fecha": "2025-08-03", "Producto": "Tortas", "CantidadProducida": 905, "Desperdicio": 15, "TiempoOperativo": "6h45m", "EmpleadosAsignados": [104, 112]},
    {"IDProduccion": 10, "Fecha": "2025-08-03", "Producto": "Bizcochuelos", "CantidadProducida": 1580, "Desperdicio": 72, "TiempoOperativo": "7h", "EmpleadosAsignados": [107]},
    {"IDProduccion": 11, "Fecha": "2025-08-03", "Producto": "Pan", "CantidadProducida": 1712, "Desperdicio": 60, "TiempoOperativo": "5h55m", "EmpleadosAsignados": [103]},
    
    {"IDProduccion": 12, "Fecha": "2025-08-04", "Producto": "Facturas", "CantidadProducida": 1940, "Desperdicio": 48, "TiempoOperativo": "5h5m", "EmpleadosAsignados": [106]},
    {"IDProduccion": 13, "Fecha": "2025-08-04", "Producto": "Galletas", "CantidadProducida": 1810, "Desperdicio": 90, "TiempoOperativo": "7h10m", "EmpleadosAsignados": [101, 102]},
    {"IDProduccion": 14, "Fecha": "2025-08-04", "Producto": "Tortas", "CantidadProducida": 890, "Desperdicio": 18, "TiempoOperativo": "6h25m", "EmpleadosAsignados": [105]},
    
    {"IDProduccion": 15, "Fecha": "2025-08-05", "Producto": "Bizcochuelos", "CantidadProducida": 1650, "Desperdicio": 70, "TiempoOperativo": "6h50m", "EmpleadosAsignados": [108]},
    {"IDProduccion": 16, "Fecha": "2025-08-05", "Producto": "Pan", "CantidadProducida": 1680, "Desperdicio": 59, "TiempoOperativo": "5h45m", "EmpleadosAsignados": [103, 109]},
    {"IDProduccion": 17, "Fecha": "2025-08-05", "Producto": "Facturas", "CantidadProducida": 1875, "Desperdicio": 41, "TiempoOperativo": "5h15m", "EmpleadosAsignados": [110]},
    
    {"IDProduccion": 18, "Fecha": "2025-08-06", "Producto": "Galletas", "CantidadProducida": 1835, "Desperdicio": 94, "TiempoOperativo": "7h5m", "EmpleadosAsignados": [101, 111]},
    {"IDProduccion": 19, "Fecha": "2025-08-06", "Producto": "Pan", "CantidadProducida": 1722, "Desperdicio": 62, "TiempoOperativo": "6h", "EmpleadosAsignados": [103]},
    {"IDProduccion": 20, "Fecha": "2025-08-06", "Producto": "Tortas", "CantidadProducida": 920, "Desperdicio": 16, "TiempoOperativo": "6h40m", "EmpleadosAsignados": [104, 112]},
    
    {"IDProduccion": 21, "Fecha": "2025-08-07", "Producto": "Facturas", "CantidadProducida": 1915, "Desperdicio": 43, "TiempoOperativo": "5h25m", "EmpleadosAsignados": [106]},
    {"IDProduccion": 22, "Fecha": "2025-08-07", "Producto": "Bizcochuelos", "CantidadProducida": 1605, "Desperdicio": 67, "TiempoOperativo": "6h55m", "EmpleadosAsignados": [107, 108]},
    {"IDProduccion": 23, "Fecha": "2025-08-07", "Producto": "Galletas", "CantidadProducida": 1790, "Desperdicio": 88, "TiempoOperativo": "7h", "EmpleadosAsignados": [101, 102]},
    
    {"IDProduccion": 24, "Fecha": "2025-08-08", "Producto": "Pan", "CantidadProducida": 1695, "Desperdicio": 61, "TiempoOperativo": "5h40m", "EmpleadosAsignados": [103]},
    {"IDProduccion": 25, "Fecha": "2025-08-08", "Producto": "Tortas", "CantidadProducida": 915, "Desperdicio": 14, "TiempoOperativo": "6h20m", "EmpleadosAsignados": [104]},
    {"IDProduccion": 26, "Fecha": "2025-08-08", "Producto": "Facturas", "CantidadProducida": 1932, "Desperdicio": 46, "TiempoOperativo": "5h10m", "EmpleadosAsignados": [106]},
]

df_produccion = pd.DataFrame(produccion)

#  EMPLEADOS

empleados = [
    {"Legajo": 101, "Nombre": "Juan", "Apellido": "Pérez", "DNI": "30111222", "Puesto": "Panadero", "Turno": "Mañana", "Sector": "Horno"},
    {"Legajo": 102, "Nombre": "María", "Apellido": "López", "DNI": "29444555", "Puesto": "Ayudante", "Turno": "Mañana", "Sector": "Horno"},
    {"Legajo": 103, "Nombre": "Carlos", "Apellido": "Gómez", "DNI": "28777888", "Puesto": "Panadero", "Turno": "Tarde", "Sector": "Masa"},
    {"Legajo": 104, "Nombre": "Laura", "Apellido": "Martínez", "DNI": "31222333", "Puesto": "Pastelera", "Turno": "Mañana", "Sector": "Repostería"},
    {"Legajo": 105, "Nombre": "Diego", "Apellido": "Fernández", "DNI": "27666999", "Puesto": "Ayudante", "Turno": "Mañana", "Sector": "Repostería"},
    {"Legajo": 106, "Nombre": "Sofía", "Apellido": "Ramírez", "DNI": "29888777", "Puesto": "Pastelera", "Turno": "Tarde", "Sector": "Facturas"},
    {"Legajo": 107, "Nombre": "Martín", "Apellido": "Suárez", "DNI": "30555111", "Puesto": "Pastelero", "Turno": "Mañana", "Sector": "Bizcochos"},
    {"Legajo": 108, "Nombre": "Ana", "Apellido": "Torres", "DNI": "32233444", "Puesto": "Ayudante", "Turno": "Mañana", "Sector": "Bizcochos"},
]

df_empleados = pd.DataFrame(empleados)

# ASISTENCIA 
asistencia = [
    {"Legajo": 101, "FechaIngreso":"2025-08-01 07:00", "FechaSalida":"2025-08-01 14:00", "HorasTrabajadas":7, "Estado":"Presente","IntentoFraude":False},
    {"Legajo": 102, "FechaIngreso":"2025-08-01 07:05", "FechaSalida":"2025-08-01 14:05", "HorasTrabajadas":7, "Estado":"Presente","IntentoFraude":False},
    {"Legajo": 103, "FechaIngreso":"2025-08-01 14:00", "FechaSalida":"2025-08-01 21:00", "HorasTrabajadas":7, "Estado":"Presente","IntentoFraude":False},
    {"Legajo": 104, "FechaIngreso":"2025-08-01 07:10", "FechaSalida":"2025-08-01 13:50", "HorasTrabajadas":6.7, "Estado":"Tarde","IntentoFraude":False},
    {"Legajo": 105, "FechaIngreso":"2025-08-01 07:05", "FechaSalida":"2025-08-01 13:55", "HorasTrabajadas":6.8, "Estado":"Presente","IntentoFraude":True},
    {"Legajo": 106, "FechaIngreso":"2025-08-01 14:05", "FechaSalida":"2025-08-01 21:00", "HorasTrabajadas":6.9, "Estado":"Presente","IntentoFraude":False},
    {"Legajo": 107, "FechaIngreso":"2025-08-01 07:00", "FechaSalida":"2025-08-01 14:00", "HorasTrabajadas":7, "Estado":"Presente","IntentoFraude":False},
    {"Legajo": 108, "FechaIngreso":"2025-08-01 07:02", "FechaSalida":"2025-08-01 14:02", "HorasTrabajadas":7, "Estado":"Presente","IntentoFraude":False},

    {"Legajo": 101, "FechaIngreso":"2025-08-02 07:00", "FechaSalida":"2025-08-02 14:00", "HorasTrabajadas":7, "Estado":"Presente","IntentoFraude":False},
    {"Legajo": 102, "FechaIngreso":"2025-08-02 07:10", "FechaSalida":"2025-08-02 14:05", "HorasTrabajadas":6.9, "Estado":"Tarde","IntentoFraude":False},
    {"Legajo": 103, "FechaIngreso":"2025-08-02 14:00", "FechaSalida":"2025-08-02 21:00", "HorasTrabajadas":7, "Estado":"Presente","IntentoFraude":True},
    {"Legajo": 104, "FechaIngreso":"2025-08-02 07:15", "FechaSalida":"2025-08-02 14:00", "HorasTrabajadas":6.75, "Estado":"Presente","IntentoFraude":False},
    {"Legajo": 105, "FechaIngreso":"2025-08-02 07:05", "FechaSalida":"2025-08-02 13:50", "HorasTrabajadas":6.75, "Estado":"Presente","IntentoFraude":False},
    {"Legajo": 106, "FechaIngreso":"2025-08-02 14:05", "FechaSalida":"2025-08-02 21:00", "HorasTrabajadas":6.9, "Estado":"Presente","IntentoFraude":False},
    {"Legajo": 107, "FechaIngreso":"2025-08-02 07:00", "FechaSalida":"2025-08-02 14:00", "HorasTrabajadas":7, "Estado":"Presente","IntentoFraude":False},
    {"Legajo": 108, "FechaIngreso":"2025-08-02 07:02", "FechaSalida":"2025-08-02 14:02", "HorasTrabajadas":7, "Estado":"Presente","IntentoFraude":True},
]

df_asistencia = pd.DataFrame(asistencia)


#  PRODUCCIÓN - EMPLEADOS

df_produccion_expandida = df_produccion.explode("EmpleadosAsignados").rename(columns={"EmpleadosAsignados":"Legajo"})
df_produccion_empleados = df_produccion_expandida.merge(df_empleados, on="Legajo", how="left")

#  VISUALIZACIONES

# Producción total por día (todos los productos)
df_total_por_dia = df_produccion.groupby("Fecha")["CantidadProducida"].sum().reset_index()

plt.figure(figsize=(10,5))
sns.lineplot(
    x="Fecha",
    y="CantidadProducida",
    data=df_total_por_dia,
    marker="o",
    color="teal"
)
plt.title("Producción total diaria (todos los productos)")
plt.xlabel("Fecha")
plt.ylabel("Cantidad Total Producida")
plt.xticks(rotation=45)
plt.show()

# Producción total por producto
df_promedio_producto = df_produccion.groupby("Producto")["CantidadProducida"].mean().reset_index()

plt.figure(figsize=(10,5))
sns.barplot(x="Producto", y="CantidadProducida", data=df_produccion, palette="Blues_d")
plt.title("Promedio de producción por producto (10 días)")
plt.ylabel("Cantidad Producida Promedio")
plt.show()

# promedio de horas trabajadas por empleado
df_promedio_horas = df_asistencia.groupby("Legajo")["HorasTrabajadas"].mean().reset_index()

plt.figure(figsize=(10,5))
sns.barplot(x="Legajo", y="HorasTrabajadas", data=df_promedio_horas, palette="Greens_d")
plt.title("Promedio de horas trabajadas por empleado")
plt.ylabel("Horas Trabajadas Promedio")
plt.show()

# Desperdicio total vs producción total 

total_producido = df_produccion["CantidadProducida"].sum()
total_desperdicio = df_produccion["Desperdicio"].sum()

plt.figure(figsize=(6,6))
plt.pie(
    [total_desperdicio, total_producido - total_desperdicio],
    labels=["Desperdicio", "Producción Efectiva"],
    autopct="%1.1f%%",
    colors=["red", "green"],
    startangle=90
)
plt.title("Desperdicio Total vs Producción Total (10 días)")
plt.show()

#  Porcentaje de desperdicio por producto 
df_desperdicio_producto = df_produccion.groupby("Producto")[["CantidadProducida","Desperdicio"]].sum().reset_index()
df_desperdicio_producto["PorcentajeDesperdicio"] = (df_desperdicio_producto["Desperdicio"] / df_desperdicio_producto["CantidadProducida"]) * 100

plt.figure(figsize=(10,6))
sns.barplot(
    x="Producto", 
    y="PorcentajeDesperdicio", 
    data=df_desperdicio_producto, 
    palette="Reds_d"
)
plt.title("Porcentaje de Desperdicio por Producto (10 días)")
plt.ylabel("Porcentaje de Desperdicio (%)")
plt.ylim(0, max(df_desperdicio_producto["PorcentajeDesperdicio"])*1.2)
plt.show()

# Producción por empleado
df_promedio_empleado = df_produccion_empleados.groupby(
    ["Legajo","Nombre","Apellido"]
)["CantidadProducida"].mean().reset_index()

plt.figure(figsize=(10,5))
sns.barplot(
    x="Legajo",
    y="CantidadProducida",
    data=df_promedio_empleado,
    palette="Purples_d"
)
plt.title("Promedio diario de producción por empleado (10 días)")
plt.ylabel("Cantidad Producida Promedio")
plt.show()

df_empleado_producto = df_produccion_empleados.groupby(["Producto", "Nombre"])["IDProduccion"].count().reset_index()
df_empleado_producto.rename(columns={"IDProduccion": "VecesTrabajadas"}, inplace=True)

num_dias = df_produccion['Fecha'].nunique()
df_empleado_producto["PromedioDiario"] = df_empleado_producto["VecesTrabajadas"] / num_dias

# Grafico de promedio diario
plt.figure(figsize=(12,6))
sns.barplot(
    x="Producto", 
    y="PromedioDiario", 
    hue="Nombre", 
    data=df_empleado_producto, 
    palette="Set2"
)
plt.title("Promedio diario de asignación de empleados por producto")
plt.ylabel("Promedio de veces asignado por día")
plt.show()

# Intentos de fraude por empleado
plt.figure(figsize=(10,5))
sns.countplot(x="Legajo", hue="IntentoFraude", data=df_asistencia, palette="Set1")
plt.title("Intentos de fraude o irregularidades por empleado")
plt.show()

