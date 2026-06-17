# funciones programa principal:

def menu_principal():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehículos")
    print("6. Salir")
    print("=====================================")

def opcion_menu():
    while True:
        try:
            opcion = int(input("Ingrese una opción del menú: "))
            if (opcion >= 1) and (opcion <= 6):
                return opcion # esta funcion entrega opcion 1-6 a quien la reciba (seleccion)
            else:
                print("Error, debe ingresar una opción del 1 al 6.")
                # no va nada acá porque el ciclo continúa y pide ingreso denuevo
        except ValueError:
            print("Error, sólo debe ingresar números, no letras.")

# funcion 1 agregar vehiculo:

def agregar_vehiculo(lista_vehiculos): # lista_vehiculos es lo que entrega esta funcion
    modelo = input("Ingrese el modelo del vehículo: ")
    anio = input("Ingrese el año del vehículo: ")
    precio = input("Ingrese el precio del vehículo: ")
    modelo_valido = validacion_modelo(modelo) # recogo en la variable modelo_valido el retorno de la funcion
    anio_valido = validacion_anio(anio) # este retorno es un True o un False según la validacion
    precio_valido = validacion_precio(precio) # este true o false se usará ahora en la validacion con msj de error:
    if modelo_valido and anio_valido and precio_valido:
        # entonces agrego los datos a un diccionario para cada vehiculo:
        diccionario_vehiculo = { # inicializo el diccionario con claves establecidas:
            "Modelo": modelo, # no es modelo_valido porque eso sería un true o false solamente
            "Año": anio,
            "Precio": precio,
            "Disponible": False # el enunciado pide disponibilidad, parte en false porque no estaría hasta que esté
        }
    # y ahora agrego cada vehiculo a la lista de vehiculos totales.
    # este ejercicio es una sola gran lista que contiene un diccionario por cada vehículo:
        lista_vehiculos.append(diccionario_vehiculo) # lista_vehiculos es la lista general de diccionarios
        print("Vehículo agregado correctamente.")
    else:
        print("Error, debe ingresar los requisitos para ingresar un vehículo.")


def validacion_modelo(modelo): # hay que llamar a la variable que se valida (modelo)
    if (modelo == "") or (modelo.strip() == ""):
        # no va el mensaje de error acá porque el enunciado lo dice
        return False
    else:
        return True # se cumplen las condiciones, es true
    
def validacion_anio(anio):
    try: # es un dato numerico asi que se valida con try/except para evitar letras
        anio_int = int(anio) # transformar el año en int para validarlo ahora, porque no lo hice en el input
        if anio_int > 1900:
            return True
        else:
            return False
    except ValueError:
        return False # los mensajes de error no van dentro de esta funcion
    
def validacion_precio(precio):
    try:
        precio_int = float(precio) # float porque el enunciado dice decimal (?)
        if precio_int > 0:
            return True
        else:
            return False
    except ValueError:
        return False







# programa principal:

lista_vehiculos = [] # inicializo vacía la gran lista de vehículos que contendrá diccionarios de cada modelo

while True:

    menu_principal()
    seleccion = opcion_menu()

    match seleccion:
        case 1:
            agregar_vehiculo()
        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
            print("Gracias por usar el sistema. Vuelva Pronto.")
            break