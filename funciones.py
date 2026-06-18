# ------------------- FUNCIONES MENU PRINCIPAL ----------------------------

def menu():

    print("=== MENU PRINCIPAL ===")
    print("1. Agregar vehiculo")
    print("2. Buscar vehiculo")
    print("3. Eliminar vehiculo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehiculos ")
    print("6. Salir")
    print("======================")

def opcion_menu():

    while True:
        try:
            opcion = int(input("Ingrese una opcion del menu: "))

            if opcion > 0 and opcion <= 6:
                return opcion
            else:
                print("ERROR: Opcion invalida. (1/6)")

        except ValueError:
            print("ERROR: Debe ingresar un valor numerico.")

# ---------------- FUNCIONES VALIDACION OPCION 1 ----------------------------

def validar_modelo(modelo):

    if modelo.strip() == "":
        return False
    else:
        return True

def validar_año(año):

    try:
        año = int(año)

        if año > 1900:
            return True
        else:
            return False
    except:
        return False

def validar_precio(precio):

    try:
        precio = float(precio)

        if precio > 0:
            return True
        else:
            return False
    except:
        return False

#--------------------- FUNCIONES DEL MENU ------------------

def agregar_vehiculo(listavehiculo):

    modelo = input("Ingrese modelo del vehiculo: ").lower()
    año = input("Ingrese año del vehiculo: ")
    precio = input("Ingrese precio del vehiculo: ")

    modeloValidado = validar_modelo(modelo)
    añoValidado = validar_año(año)
    precioValidado = validar_precio(precio)

    if not modeloValidado:
        print("El modelo no debe quedar vacio o estar repetido.")
    if not añoValidado:
        print("Año debe ser mayor que 1900.")
    if not precioValidado:
        print("Precio debe ser mayor que 0.")

    if modeloValidado and añoValidado and precioValidado:

        vehiculo = {
            "modelo" : modelo,
            "año" : int(año),
            "precio" : float(precio),
            "disponible" : False
        }

        listavehiculo.append(vehiculo)
        print("Vehiculo agregado éxitosamente!")
        print("")
    else:
        print("No se pudo agregar el vehiculo.")

def buscar_vehiculo(lista, modelo):

    for indice, vehiculo in enumerate(lista):

        if vehiculo["modelo"] == modelo:
            return indice
    return -1

def actualizar_disponibilidad(lista):

    for vehiculo in lista:

        if vehiculo["año"] >= 2020:
            vehiculo["disponible"] = True
        else:
            vehiculo["disponible"] = False

def mostrar_vehiculos(lista):

    if len(lista) == 0:
        print("No hay vehiculos registrados.")
        return
    
    actualizar_disponibilidad(lista)

    print("--- LISTA DE VEHICULOS ---")
    
    for vehiculo in lista:

        estado = "DISPONIBLE" if vehiculo["disponible"] else "NO DISPONIBLE"

        print(f"Modelo: {vehiculo["modelo"]}")
        print(f"Año: {vehiculo["año"]}")
        print(f"Precio: {vehiculo["precio"]}")
        print(f"Disponible: {estado}")
        print("=============================")

#------------------- FIN FUNCIONES ----------------------------------------