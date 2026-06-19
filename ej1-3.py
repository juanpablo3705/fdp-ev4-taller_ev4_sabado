# funcion mostrar menú:
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehículos")
    print("6. Salir")
    print("=====================================")

# funcion ingresar opción:
def elegir_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción del menú: "))
            if (opcion >= 1) and (opcion <= 6):
                return opcion
            else:
                print("Error, debe elegir una opción del 1 al 6.")
        except ValueError:
            print("Error, debe ingresar números, no letras.")

# funcion validar modelo:
def validar_modelo(modelo):
    if modelo.strip() == "":
        return False
    else:
        return True
    
# funcion validar año:
def validar_anio(anio):
    if anio > 1900:
        return True
    else:
        return False

# funcion validar precio:
def validar_precio(precio):
    if precio > 0:
        return True
    else:
        return False
        
# funcion 1 agregar vehículo:
def agregar_vehiculo(coleccion_vehiculos):
    while True:
        modelo = input("Ingrese el modelo del vehículo: ").lower()
        if not validar_modelo(modelo):
            print("Error, el modelo no puede estar vacío.")
        else:
            break
    while True:
        try:
            anio = int(input("Ingrese el año del vehículo: "))
            if not validar_anio(anio):
                print("Error, el año debe ser mayor a 1900.")
            else:
                break
        except ValueError:
            print("Error, no deben ser letras.")
    while True:
        try:
            precio = float(input("Ingrese el precio del vehículo: "))
            if not validar_precio(precio):
                print("Error, el precio debe ser mayor que cero.")
            else:
                break
        except ValueError:
            print("Error, no debe ingresar letras.")
    vehiculo = {
        "modelo": modelo,
        "año": anio,
        "precio": precio,
        "disponible": False
    }
    coleccion_vehiculos.append(vehiculo)
    print(f"Modelo {modelo} agregado con éxito.")

# funcion 2 buscar indice:
def buscar_indice(coleccion_vehiculos, modelo):
    for indice in range(len(coleccion_vehiculos)):
        if coleccion_vehiculos[indice]["modelo"] == modelo:
            return indice
    return -1

# funcion 4 actualizar disponibilidad:
def actualizar_disponibilidad(coleccion_vehiculos):
    for vehiculo in coleccion_vehiculos:
        if vehiculo["año"] >= 2020:
            vehiculo["disponible"] = True
        else:
            vehiculo["disponible"] = False

# PROGRAMA PRINCIPAL:
coleccion_vehiculos = []

while True:
    mostrar_menu()
    opcion_elegida = elegir_opcion()
    match opcion_elegida:
        case 1:
            agregar_vehiculo(coleccion_vehiculos)
        case 2:
            if len(coleccion_vehiculos) == 0:
                print("Error, debe primero agregar un vehiculo.")
            else:
                modelo = input("Ingrese el modelo a buscar: ")
                posicion = buscar_indice(coleccion_vehiculos, modelo)
                if posicion == -1:
                    print(f"Error, el modelo {modelo} no se ha encontrado.")
                else:
                    print(f"Vehículo {modelo} encontrado.")
                    print(f"Posición: {posicion}.")
                    print(f"Modelo: {coleccion_vehiculos[posicion]["modelo"]}")
                    print(f"Año: {coleccion_vehiculos[posicion]["año"]}")
                    print(f"Precio: {coleccion_vehiculos[posicion]["precio"]}")
        case 3:
            modelo = input("Ingrese el vehiculo a eliminar: ")
            posicion = buscar_indice(coleccion_vehiculos, modelo)
            if posicion == -1:
                print(f"Error, el modelo {modelo} no existe.")
            else:
                coleccion_vehiculos.pop(posicion)
                print(f"El modelo {modelo} ha sido eliminado.")
        case 4:
            actualizar_disponibilidad(coleccion_vehiculos)
            print("Disponibilidad actualizada con exito.")
        case 5:
            actualizar_disponibilidad(coleccion_vehiculos)
            for vehiculo in coleccion_vehiculos:
                if vehiculo["disponible"]:
                    estado = "DISPONIBLE"
                else:
                    estado = "NO DISPONIBLE"
                print(f"Modelo: {vehiculo["modelo"]}")
                print(f"Año: {vehiculo["año"]}")
                print(f"Precio: {vehiculo["precio"]}")
                print(f"Disponibilidad: {estado}")
        case 6:
            print("Saliendo...")
            break