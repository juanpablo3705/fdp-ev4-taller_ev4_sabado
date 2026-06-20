# funcion mostrar menu:
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehículos")
    print("6. Salir")
    print("=====================================")

# funcion ingresar opcion:
def ingresar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción del menú: "))
            if (opcion >= 1) and (opcion <= 6):
                return opcion
            else:
                print("Error, debe ingresar una opcion del 1 a 6.")
        except ValueError:
            print("Error, debe ingresar números no letras")

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

# funcion 1 agregar vehiculo:
def agregar_vehiculo(coleccion_vehiculos):
    while True:
        modelo = input("Ingrese el modelo: ")
        if validar_modelo(modelo):
            break
        else:
            print("Error, el modelo no puede estar vacío.")
    while True:
        try:
            anio = int(input("Ingrese el año: "))
            if anio > 1900:
                break
            else:
                print("Error, el año debe ser mayor a 1900.")
        except ValueError:
            print("Error, el año no deben ser letras.")
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            if precio > 0:
                break
            else:
                print("Error, el precio debe ser mayor que cero.")
        except ValueError:
            print("Error, el precio no deben ser letras.")
    vehiculos ={
        "modelo": modelo,
        "año": anio,
        "precio": precio,
        "disponible": False
    }
    coleccion_vehiculos.append(vehiculos)
    print(f"Modelo {modelo} agregado correctamente.")

# funcion 2 buscar_indice:
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
    # no es asi:
    #    for vehiculo in coleccion_vehiculos:
    #        if coleccion_vehiculos[vehiculo]["año"] >= 2020:
    #            coleccion_vehiculos[vehiculo]["disponible"] = True
    #        else:
    #            coleccion_vehiculos[vehiculo]["disponible"] = False
    # porque vehiculo no es un indice, sino que es directamente el diccionario

# programa principal:
coleccion_vehiculos = []
while True:
    mostrar_menu()
    opcion_elegida = ingresar_opcion()
    match opcion_elegida:
        case 1:
            agregar_vehiculo(coleccion_vehiculos)
        case 2:
            modelo = input("Ingrese modelo a buscar: ")
            posicion = buscar_indice(coleccion_vehiculos, modelo)
            if posicion == -1:
                print(f"Error, modelo {modelo} no encontrado.")
            else:
                print(f"Modelo encontrado.")
                print(f"Posición: {posicion}")
                print(f"Modelo :{modelo}")
                print(f"Año: {coleccion_vehiculos[posicion]["año"]}")
                print(f"Precio: {coleccion_vehiculos[posicion]["precio"]}")
                print(f"Disponible: {coleccion_vehiculos[posicion]["disponible"]}")
        case 3:
            modelo = input("Ingrese el modelo a buscar: ")
            posicion = buscar_indice(coleccion_vehiculos, modelo)
            if posicion == -1:
                print(f"Error, modelo {modelo} no encontrado.")
            else:
                coleccion_vehiculos.pop(posicion)
                print(f"Modelo {modelo} eliminado correctamente.")
        case 4:
            actualizar_disponibilidad(coleccion_vehiculos)
            print("Disponibilidad actualizada con éxito.")
        case 5:
            actualizar_disponibilidad(coleccion_vehiculos)
            print("=== LISTA DE VEHICULOS ===")
            for vehiculo in coleccion_vehiculos:
                if (vehiculo["disponible"]) == True:
                    estado = "DISPONIBLE"
                else:
                    estado = "NO DISPONIBLE"
                print(f"Modelo: {vehiculo["modelo"]}")
                print(f"Año: {vehiculo["año"]}")
                print(f"Precio: {vehiculo["precio"]}")
                print(f"Disponibilidad: {estado}")
        case 6:
            print("Gracias por usar el sistema. Vuelva Pronto.")
            break