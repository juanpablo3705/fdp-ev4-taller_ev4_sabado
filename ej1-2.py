# funcion imprimir menu:
def menu_principal():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehículos")
    print("6. Salir")
    print("=====================================")

# funcion elegir opcion del menu:
def elegir_opcion():
    while True:
        try:
            opcion_elegida = int(input("Ingrese una opcion del menú: "))
            if (opcion_elegida > 0) and (opcion_elegida < 7):
                return opcion_elegida
            else:
                print("Error, debe elegir una opcion del 1 al 6.")
        except ValueError:
            print("Error, debe ingresar sólo números, no letras.")

# funcion validar ingreso de modelo:
def validar_modelo(modelo):
    if modelo.strip() == "":
        return False
    else:
        return True
    
# funcion validar ingreso de año:
def validar_anio(anio):
    try:
        if anio <= 1900:
            return False
        else:
            return True
    except ValueError:
        return False

# funcion validar ingreso de precio:
def validar_precio(precio):
    try:
        if precio > 0:
            return True
        else:
            return False
    except ValueError:
        return False

# funcion case 1 agregar vehiculo:
def agregar_vehiculo(coleccion_vehiculos):
    modelo = input("Ingrese modelo del vehículo: ")
    anio = int(input("Ingrese año del vehículo: "))
    precio = float(input("Ingrese precio del vehículo: "))
    modelo_validado = validar_modelo(modelo)
    anio_validado = validar_anio(anio)
    precio_validado = validar_precio(precio)
    if modelo_validado and anio_validado and precio_validado:
        vehiculo = {
            "modelo": modelo,
            "año": anio,
            "precio": precio,
            "disponible": False
        }
        coleccion_vehiculos.append(vehiculo)
        print("Vehículo agregado correctamente.")
    else:
        print("Error, debe cumplir las condiciones del registro.")

# funcion case 2 buscar indice:
def buscar_indice(coleccion_vehiculos, modelo):
    for indice in range(len(coleccion_vehiculos)):
        if coleccion_vehiculos[indice]["modelo"] == modelo:
            return indice
    return -1 # va fuera del ciclo for así la funcion no termina con el return después de un resultado
        
# funcion case 3 eliminar vehículo no es necesaria.

# funcion case 4 actualizar disponibilidad:
def actualizar_disponibilidad(coleccion_vehiculos):
    if len(coleccion_vehiculos) == 0:
        print("Error, no hay vehículos registrados.")
        return
    for vehiculo in coleccion_vehiculos: # por que no es "range(len(coleccion_vehiculos))" en vez de solo "coleccion_vehiculos"?
        if vehiculo["año"] >= 2020:
            vehiculo["disponible"] = True
        else:
            vehiculo["disponible"] = False

# funcion case 5 mostrar vehículos:
def mostrar_vehículos(coleccion_vehiculos):
    if len(coleccion_vehiculos) == 0:
        print("Error, no hay vehículos registrados.")
        return
    actualizar_disponibilidad(coleccion_vehiculos)
    print("Actualizando disponibilidad... ... éxito.")
    print("Mostrando vehículos y su disponibilidad:")
    for vehiculo in coleccion_vehiculos:
        if vehiculo["disponible"] == True:
            estado = "DISPONIBLE"
        else:
            estado = "NO DISPONIBLE"
        print(f"Modelo: {vehiculo["modelo"]}") # recuerda usar " " al llamar un elemento del diccionario !!!!
        print(f"Año: {vehiculo["año"]}")
        print(f"Precio: {vehiculo["precio"]}")
        print(f"Disponibilidad: {estado}")

# PROGRAMA PRINCIPAL:

coleccion_vehiculos = []

while True:

    menu_principal()
    opcion = elegir_opcion() # el retorno de la funcion elegir_opcion debe caer en una variable (opcion)

    match opcion:
        case 1:
            agregar_vehiculo(coleccion_vehiculos)
        case 2:
            if len(coleccion_vehiculos) == 0:
                print("Error, debe primero agregar un vehículo.")
            else:
                modelo = input("Ingrese modelo a buscar: ")
                posicion = buscar_indice(coleccion_vehiculos, modelo)
                if posicion == -1:
                    print(f"Error, modelo {modelo} no encontrado.")
                else:
                    print(f"Posición: {posicion}.")
                    print(f"Modelo: {coleccion_vehiculos[posicion]["modelo"]}.")
                    print(f"Año: {coleccion_vehiculos[posicion]["año"]}.")
                    print(f"Precio: {coleccion_vehiculos[posicion]["precio"]}.")
        case 3:
            if len(coleccion_vehiculos) == 0:
                print("Error, debe primero agregar un vehículo.")
            else:
                modelo = input("Ingrese vehículo a eliminar: ")
                posicion = buscar_indice(coleccion_vehiculos, modelo)
                if posicion == -1:
                    print(f"Error, el modelo {modelo} no está agregado.")
                else:
                    coleccion_vehiculos.pop(posicion)
                    print(f"Éxito, el modelo {modelo} ha sido eliminado.")
        case 4:
            actualizar_disponibilidad(coleccion_vehiculos)
            print("Disponibilidad actualizada con éxito.")
        case 5:
            mostrar_vehículos(coleccion_vehiculos)
        case 6:
            print("Saliendo...")
            break