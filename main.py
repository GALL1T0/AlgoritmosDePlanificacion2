class Proceso:
    def __init__(self, nombre, tiempo, prioridad):
        self.nombre = nombre
        self.tiempo = tiempo
        self.prioridad = prioridad


# Función para cargar procesos desde un archivo
def cargar_procesos_desde_archivo(nombre_archivo):
    procesos = []
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")
                nombre = datos[0]
                tiempo = int(datos[1])
                prioridad = int(datos[2])
                procesos.append(Proceso(nombre, tiempo, prioridad))
    except FileNotFoundError:
        print("El archivo especificado no existe.")
    return procesos


# Función para agregar un nuevo proceso
"""def agregar_proceso():
    nombre = input("Ingrese el nombre del proceso: ")
    tiempo = int(input("Ingrese el tiempo de duración del proceso: "))
    prioridad = int(input("Ingrese la prioridad del proceso: "))
    posicion = input("¿Agregar al principio o al final? (P/A): ").lower()
    if posicion == "p":
        procesos.insert(0, Proceso(nombre, tiempo, prioridad))
    else:
        procesos.append(Proceso(nombre, tiempo, prioridad))"""


# Función para simular el algoritmo Round Robin
def round_robin(procesos, quantum):
    procesos = procesos.copy()
    tiempo_total = 0
    resultado = []

    while procesos:
        proceso_actual = procesos.pop(0)
        if proceso_actual.tiempo > quantum:
            proceso_actual.tiempo -= quantum
            tiempo_total += quantum
            procesos.append(proceso_actual)
        else:
            tiempo_total += proceso_actual.tiempo
            resultado.append((proceso_actual.nombre, tiempo_total))

    return resultado


# Función para simular el algoritmo SJF
def sjf(procesos):
    procesos.sort(key=lambda x: x.tiempo)
    tiempo_total = 0
    resultado = []

    for proceso in procesos:
        resultado.append((proceso.nombre, tiempo_total))
        tiempo_total += proceso.tiempo

    return resultado



# Función para simular el algoritmo FIFO
def fifo(procesos):
    tiempo_total = 0
    resultado = []

    for proceso in procesos:
        tiempo_total += proceso.tiempo
        resultado.append((proceso.nombre, tiempo_total))

    return resultado


# Función para simular el algoritmo de prioridades
def prioridades(procesos):
    procesos.sort(key=lambda x: x.prioridad)
    tiempo_total = 0
    resultado = []

    for proceso in procesos:
        tiempo_total += proceso.tiempo
        resultado.append((proceso.nombre, tiempo_total))

    return resultado


# Función para simular un algoritmo de administración de procesos
def simular_algoritmo(procesos, algoritmo):
    if algoritmo == "RR":
        quantum = int(input("Ingrese el quantum para Round Robin: "))
        resultado = round_robin(procesos.copy(), quantum)
    elif algoritmo == "SJF":
        resultado = sjf(procesos.copy())
    elif algoritmo == "FIFO":
        resultado = fifo(procesos.copy())
    elif algoritmo == "PRI":
        resultado = prioridades(procesos.copy())
    else:
        print("Algoritmo no válido.")
        return

    for proceso, tiempo in resultado:
        print(f"{proceso}: Tiempo total = {tiempo} unidades de tiempo")


# Ciclo principal
procesos = []
while True:
    print("\n1. Cargar procesos desde archivo")
    print("2. Simular un algoritmo de administración de procesos")
    print("3. Salir")

    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == "1":
        archivo_nombre = input("Ingrese el nombre del archivo con los procesos: ")
        procesos.extend(cargar_procesos_desde_archivo(archivo_nombre))
    elif opcion == "2":
        if not procesos:
            print("No hay procesos para simular. Por favor, cargue o agregue procesos primero.")
        else:
            algoritmo = input("Seleccione el algoritmo (RR/SJF/FIFO/PRI): \n").upper()
            simular_algoritmo(procesos, algoritmo)
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Intente de nuevo.")

print("Hasta luego!")
