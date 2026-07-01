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

# funcion escoger opción menú:
def escoger_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción del menú: "))
            if opcion > 0 and opcion < 7:
                return opcion
            else:
                print("Error, debe ingresar una opción del 1 al 6.")
        except ValueError:
            print("Error, debe ingresar sólo números, no letras.")

# funcion validar modelo:
# las funciones aquí son como las funciones matemáticas donde el dato que reciben en () le aplicarán el proceso
def validar_modelo(modelo):
    if modelo.strip() == "":
        return False
    else:
        return True
    
# funcion validar anio:
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
def agregar_vehiculo(coleccion):
    while True:
        modelo = input("Ingrese el modelo a agregar: ")
        if validar_modelo(modelo):
            break
        else:
            print("Error, el modelo no puede estar vacío o ser sólo espacios en blanco.")
    while True:
        try:
            anio = int(input("Ingrese el año del modelo: "))
            if validar_anio(anio):
                break
            else:
                print("Error, el año debe ser mayor que 1900.")
        except ValueError:
            print("Error, el año debe ser un número entero.")
    while True:
        try:
            precio = float(input("Ingrese el precio del modelo: "))
            if validar_precio(precio):
                break
            else:
                print("Error, el precio debe ser mayor que cero.")
        except ValueError:
            print("Error, el precio debe ser un número entero o decimal.")
    vehiculo = {
        "Modelo": modelo,
        "Año": anio,
        "Precio": precio,
        "Disponible": False
    }
    coleccion.append(vehiculo)

# funcion 2 buscar índice:
def buscar_indice(coleccion, modelo):
    for indice in range(len(coleccion)):
        if coleccion[indice]["Modelo"] == modelo:
            return indice
    return -1

# funcion 4 actualizar disponibilidad:
def actualizar_disponibilidad(coleccion):
    for vehiculo in coleccion:
        if vehiculo["Año"] >= 2020:
            vehiculo["Disponible"] = True
        else:
            vehiculo["Disponible"] = False 

# funcion disponible:
def disponible(vehiculo):
    if vehiculo["Disponible"] == False:
        return "NO DISPONIBLE"
    else:
        return "DISPONIBLE"

# programa principal:
coleccion = []
while True:
    mostrar_menu()
    opcion_elegida = escoger_opcion()
    match opcion_elegida:
        case 1:
            agregar_vehiculo(coleccion)
        case 2:
            if len(coleccion) == 0:
                print("Error, no hay vehículos registrados.")
            else:
                while True:
                    modelo = input("Ingrese modelo a buscar: ")
                    if modelo.strip() == "":
                        print("Error, el modelo no puede estar en blanco o ser solo espacios.")
                    else:
                        indice = buscar_indice(coleccion, modelo)
                        if indice == -1:
                            print("Error, modelo no encontrado.")
                            break
                        else:
                            print("Modelo encontrado.")
                            print(f"Modelo: {coleccion[indice]["Modelo"]}.")
                            print(f"Año: {coleccion[indice]["Año"]}.")
                            print(f"Precio: {coleccion[indice]["Precio"]}.")
                            print(f"Disponible: {coleccion[indice]["Disponible"]}.")
                            break
        case 3:
            if len(coleccion) == 0:
                print("Error, no hay vehículos registrados.")
            else:
                while True:
                    modelo = input("Ingrese el modelo a eliminar: ")
                    if modelo.strip() == "":
                        print("Error, el modelo no puede estar en blanco o ser solo espacios.")
                    else:
                        indice = buscar_indice(coleccion, modelo)
                        if indice == -1:
                            print("Error, modelo no encontrado.")
                            break
                        else:
                            print(f"Modelo {coleccion[indice]["Modelo"]} eliminado con éxito.")
                            del(coleccion[indice])
                            break
                            # primero el msj de éxito y después borrar, sino el msj no encuentra el indice porque
                            # se eliminó antes del msj
        case 4:
            if len(coleccion) == 0:
                print("Error, no hay vehículos registrados.")
            else:
                actualizar_disponibilidad(coleccion)
                print("Disponibilidad actualizada con éxito.")
        case 5:
            if len(coleccion) == 0:
                print("Error, no hay vehículos registrados.")
            else:
                actualizar_disponibilidad(coleccion)
                print("=== LISTA DE VEHICULOS ===")
                for vehiculo in coleccion:
                    estado = disponible(vehiculo)
                    print(f"Modelo: {vehiculo["Modelo"]}.")
                    print(f"Año: {vehiculo["Año"]}.")
                    print(f"Precio: {vehiculo["Precio"]}.")
                    print(f"Disponible: {estado}.")
                    print("********************************************")
        case 6:
            print("Gracias por usar el sistema. Vuelva Pronto.")
            break