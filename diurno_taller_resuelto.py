# Sistema de gestión de vehículos de un concesionario.
# Los datos se guardan en una lista; cada vehículo es un diccionario con sus campos.


# --- MENÚ ---
# Función sin parámetros ni retorno: solo muestra las opciones en pantalla.
def mostrarMenu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehículos")
    print("6. Salir")
    print("=====================================")

# Lee la opción del usuario y la valida. Retorna un número entre 1 y 6.
# El try/except evita que el programa falle si el usuario ingresa texto.
def solicitarOpcion():
    while True:
        try:
            opcion = int(input("Ingrese la opción a realizar: "))

            if opcion > 0 and opcion <= 6:
                return opcion
            else:
                print("Ingrese una opción valida de menú (1-6)")  
        except ValueError:
            print("Ingrese una opción valida de menú")

# --- VALIDACIONES ---
# Cada función recibe un dato y retorna True si es válido, False si no lo es.
# Los mensajes de error se muestran en agregarVehiculo, no aquí.

def validaModelo(modelo):
    # strip() elimina espacios al inicio y al final; si queda vacío, no es válido.
    if modelo.strip() == "":
        return False
    else:
        return True
    
def validarAnio(anio):
    try:
        anioNumerico = int(anio)

        if anioNumerico <= 1900:
            return False
        else:
            return True
    except ValueError:
        return False
    
def validarPrecio(precio):
    try:
        precioDecimal = float(precio)

        if precioDecimal > 0:
            return True
        else:
            return False

    except ValueError:
        return False

# --- OPERACIONES CON LA LISTA ---

# Recibe la lista por parámetro y agrega un nuevo vehículo si los datos son válidos.
def agregarVehiculo(listaVehiculo):
    
    modelo = input("Ingresa el modelo del vehiculo (sin espacios): ")
    anio = input("Ingresa el año de fabricación del vehiculo (mayor a 1900): ")
    precio = input("Ingresa el precio del vehiculo (mayor a 0):")

    modeloValido = validaModelo(modelo) # true o un false
    anioValido = validarAnio(anio) # true o un false
    precioValido = validarPrecio(precio) # true o un false

    # Solo se guarda si las tres validaciones pasan (operador and).
    if modeloValido and anioValido and precioValido:

        # Diccionario con los campos del vehículo. "disponible" inicia en False.
        vehiculo = {
            "modelo": modelo, 
            "anio": int(anio),
            "precio": float(precio),
            "disponible": False
        }

        # append agrega el diccionario al final de la lista.
        listaVehiculo.append(vehiculo)
        print("Vehiculo agregado correctamente")
    else:
        print("Los datos no cumplen con los valores correctos")

# Recorre la lista y retorna la posición (índice) del modelo encontrado.
# Si no existe, retorna -1. El programa principal decide qué hacer con ese valor.
def buscarVehiculo(lista, modelo):

    # 0: { ... }
    # 1: { ... }
    
    #for vehiculo in lista:
     #   if modelo == vehiculo["modelo"]:
      #      return lista.index(vehiculo)

    # enumerate devuelve el índice y el elemento en cada vuelta del ciclo.
    for indice, vehiculo in enumerate(lista):
        if modelo == vehiculo["modelo"]:
            return indice
        
    return -1
        
# Recorre todos los vehículos y actualiza "disponible" según el año (>= 2020 → True).
def actualizarDisponibilidad(lista):

    for vehiculo in lista:

        if vehiculo["anio"] >= 2020:
            vehiculo["disponible"] = True
        else:
            vehiculo["disponible"] = False


# Primero actualiza disponibilidad, luego muestra cada vehículo con el formato pedido.
def mostrarTodosVehiculos(lista_vehiculos):
    actualizarDisponibilidad(lista_vehiculos)

    print("=== LISTA DE VEHICULOS ===")
    
    if len(lista_vehiculos) == 0:
        print("No hay vehículos registrados en el concesionario.")
        print("********************************************")
    else:
        for vehiculo in lista_vehiculos:
            if vehiculo["disponible"]:
                estado_texto = "DISPONIBLE"
            else:
                estado_texto = "NO DISPONIBLE"
                
            print(f"Modelo: {vehiculo['modelo']}")
            print(f"Año: {vehiculo['anio']}")
            print(f"Precio: {vehiculo['precio']}")
            print(f"Estado: {estado_texto}")
            print("********************************************")

# --- PROGRAMA PRINCIPAL ---
# Colección de vehículos: lista vacía al inicio, se llena con cada registro nuevo.
listadoVehiculosAlmacenados = []

# Ciclo infinito: muestra menú, lee opción y ejecuta la acción correspondiente.
while True:

    mostrarMenu()

    opcionSeleccionada = solicitarOpcion()

    if opcionSeleccionada == 1:
        agregarVehiculo(listadoVehiculosAlmacenados)
    
    elif opcionSeleccionada == 2:
        modeloBuscado = input("Ingresa el modelo a buscar: ")

        posicionVehiculo = buscarVehiculo(listadoVehiculosAlmacenados, modeloBuscado)

        # posicionVehiculo >= 0 significa que se encontró en la lista.
        if posicionVehiculo >= 0:

            print("********************************************")
            print("Vehiculo encontrado en la posición: ", posicionVehiculo)
            print(f"Modelo: {listadoVehiculosAlmacenados[posicionVehiculo]['modelo']}")
            print(f"Año: {listadoVehiculosAlmacenados[posicionVehiculo]['anio']}")
            print(f"Precio: {listadoVehiculosAlmacenados[posicionVehiculo]['precio']}")
            print(f"Estado: {listadoVehiculosAlmacenados[posicionVehiculo]['disponible']}")
            print("********************************************")
        else:
            print(f"El vehículo '{modeloBuscado}' no se encuentra registrado.") 


    elif opcionSeleccionada == 3:
        modeloBuscado = input("Ingresa el modelo a buscar: ")

        posicionVehiculo = buscarVehiculo(listadoVehiculosAlmacenados, modeloBuscado)

        if posicionVehiculo >= 0:
            # pop elimina el elemento en esa posición de la lista.
            listadoVehiculosAlmacenados.pop(posicionVehiculo)
        else:
            print(f"El vehículo '{modeloBuscado}' no se encuentra registrado.") 

    elif opcionSeleccionada == 4:

        actualizarDisponibilidad(listadoVehiculosAlmacenados)

    elif opcionSeleccionada == 5:
        mostrarTodosVehiculos(listadoVehiculosAlmacenados)

    elif opcionSeleccionada == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break
