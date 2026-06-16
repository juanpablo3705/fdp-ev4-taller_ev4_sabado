def mostrarMenu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehículos")
    print("6. Salir")
    print("=====================================")

def solicitarOpcion():
    while True:
        try:
            opcion = int(input("Ingresa la opción a ejecutar: "))

            if opcion < 0 or opcion > 6:
                print("Ingrese una opción valida (1-6)")
            else:
                return opcion
        except ValueError:
            print("Ingrese una opción valida (1-6)")

def validarModelo(modeloValidar):
    if modeloValidar.strip() == "":
        return False # no cumple la validación
    else:
        return True # cumple la validación
    
def validarAnio(anioValidar):
    try:
        anioValidar = int(anioValidar)

        if anioValidar <= 1900:
            return False # No cumple la validación
        else:
            return True # Si cumple la validación

    except ValueError:
        return False # no cumple la validación
    
def validarPrecio(precioValidar):
    try:
        precioValidar = float(precioValidar)

        if precioValidar <= 0:
            return False # no cumple la validación
        else:
            return True # Si cumple la validación

    except ValueError:
        return False # no cumple la validación

def agregarVehiculo(lista):
    
    modelo = input("Ingrese el modelo del vehiculo (no debe estar vacío): ")
    anio = input("Ingrese el año de fabricación del vehiculo (> 1900): ")
    precio = input("Ingrese el precio del vehiculo (> 0): ")

    # OPCIONAL: VALIDAR SI EXISTE PREVIAMENTE EL MODELO
    posicion = buscarVehiculo(lista, modelo)

    if posicion != -1:
        print(f"El vehiculo ya existe para el modelo {modelo}")
        
        return
    # OPCIONAL: VALIDAR SI EXISTE PREVIAMENTE EL MODELO

    modeloValido = validarModelo(modelo) # True o False
    anioValido = validarAnio(anio) # True o False
    precioValido = validarPrecio(precio) # True o False

    if modeloValido == True and anioValido == True and precioValido == True:
        vehiculo = {
            "modelo": modelo,
            "anio": int(anio),
            "precio": float(precio),
            "disponible": False
        }

        lista.append(vehiculo)

        print("Vehiculo agregado correctamente.")
    else:
        print("Los datos ingresados no cumplen con las validaciones")


def buscarVehiculo(lista, modelo):

    for indice, vehiculo in enumerate(lista):
        if vehiculo["modelo"] == modelo:
            return indice # indice donde se encontro

    return -1 # Si no encuentra devolver -1

def actualizarVehiculos(lista):

    for vehiculo in lista:
        if vehiculo["anio"] >= 2020:
            vehiculo["disponible"] = True
        else:
            vehiculo["disponible"] = False

    print("Se actualizaron los registros de vehiculos")

def mostrarVehiculos(lista):

    if len(lista) == 0:
        print("No existen vehiculos registrados aún")
        return

    actualizarVehiculos(lista)

    print("=== LISTA DE VEHICULOS ===")
    for vehiculo in lista:
        print(f"Modelo: {vehiculo['modelo']}")
        print(f"Precio: {vehiculo['precio']}")
        print(f"Año: {vehiculo['anio']}")

        if vehiculo['disponible']:
            print(f"Disponible?: DISPONIBLE")
        else:
            print(f"Disponible?: NO DISPONIBLE")


########## Codigo principal ##############

listaVehiculos = []

while True:

    mostrarMenu()

    opcionSeleccionada = solicitarOpcion()

    if opcionSeleccionada == 1:
        agregarVehiculo(listaVehiculos)

    elif opcionSeleccionada == 2:

        modeloBuscado = input("Ingresa el modelo de vehiculo a buscar: ")

        posicion = buscarVehiculo(listaVehiculos, modeloBuscado)  

        if posicion != -1:
            print(f"Vehiculo encontrado en la posición {posicion}")

            vehiculoEncontrado = listaVehiculos[posicion]

            print(f"Modelo: {vehiculoEncontrado['modelo']}")
            print(f"Precio: {vehiculoEncontrado['precio']}")
            print(f"Año: {vehiculoEncontrado['anio']}")

            if vehiculoEncontrado['disponible']:
                print(f"Disponible?: DISPONIBLE")
            else:
                print(f"Disponible?: NO DISPONIBLE")
        else:
            print(f"El vehículo '{modeloBuscado}' no se encuentra registrado.")

    elif opcionSeleccionada == 3:
        modeloBuscado = input("Ingresa el modelo de vehiculo a buscar: ")

        posicion = buscarVehiculo(listaVehiculos, modeloBuscado)

        if posicion != -1:
            listaVehiculos.pop(posicion)

            print(f"Vehiculo con modelo '{modeloBuscado}' eliminado")
        else:
            print(f"El vehículo '{modeloBuscado}' no se encuentra registrado.")

    elif opcionSeleccionada == 4:
        actualizarVehiculos(listaVehiculos)
    
    elif opcionSeleccionada == 5:
        mostrarVehiculos(listaVehiculos)

    elif opcionSeleccionada == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break
