def mostrar_menu():
    print("--MENU--")
    print("1. Agregar Libro")
    print("2. Buscar Libro")
    print("3. Eliminar Libro")
    print("4. Registrar préstamo")
    print("5. Mostrar Libros")
    print("6. Salir")


def leer_opcion():
    while True: 
        try:
            opcion = int(input("Ingrese su opción: "))
            break
        except ValueError:
            print("Error, debe ingresar un número!")
    return opcion

def agregar_libro(libros):
    titulo = input("Ingrese titulo del libro: ")
    if not validar_texto(titulo):
        print("Error, el título no puede estar vacío")
        return
    
    autor = input("Ingrese nombre del autor: ")
    if not validar_texto(autor):
        print("Error, el autor no puede estar vacío")
        return
    while True:
        try:
            anio = int(input("Ingrese año de publicación: "))
            if not validar_anio(anio):
                print("Error ,el año debe esar entre 1000 y 2025")
                return
            break
        except ValueError:
            print("Error, debe ingresar un valor entero")
    
    libro = {
        "titulo" : titulo.strip(),
        "autor" : autor.strip(),
        "año" : anio,
        "prestado" : False
    }

    libros.append(libro)
    print(f"Libro {titulo} registrado correctamente!")


def validar_anio(valor):
    return 1000 <= valor <= 2025
    #if valor >= 1000 and valor <= 2025:
    #    return True


def validar_texto(valor):
    return len(valor.strip()) > 0 # return true

def buscar_libro(libros,titulo):
    for i in range(len(libros)):
        if libros[i]["titulo"] == titulo:
            return i
    return -1

def registrar_prestamos(libros):
    for libro in libros:
        if libro["año"] >= 2000:
            libro["prestado"] = True
        else:
            libro["prestado"] = False

def mostrar_libros(libros):
    registrar_prestamos(libros) # actualiza el estado del libro

    if len(libros) == 0:
        print("No hay libros")
        return
    print("--LISTA DE LIBROS--")

    for libro in libros:
        if libro["prestado"] == True:
            estado = "DISPONIBLE PARA PRESTAMO"
        else:
            estado = "SOLO CONSULTA EN SALA"

        print("Titulo: ",libro["titulo"])
        print("Autor: ",libro["autor"])
        print("Año: ",libro["año"])
        print("Estado: ",estado)
        print("*"*20)

#principal
libros = []
while True:
    mostrar_menu()
    op = leer_opcion()

    if op == 1:
        agregar_libro(libros)
    elif op == 2: 
        titulo = input("Ingrese el titulo a buscar: ")
        pos = buscar_libro(libros,titulo)
        print("La posición es: ",pos)
        if pos != -1:
            libro = libros[pos]
            print(f"Titulo: {libro["titulo"]}")
            print(f"Autor: {libro["autor"]}")
            print(f"Año: {libro["año"]}")
            print(f"Prestado: {libro["prestado"]}")
            
        else:
            print(f"El libro:{titulo} no se encuentra registrado ")

    elif op == 3:
        titulo = input("Ingrese titulo a eliminar: ")
        pos = buscar_libro(libros,titulo)
        if pos != 1:
            libros.pop(pos)
            print(f"Libro {titulo} eliminado correctamente")
        else:
            print(f"Libro {titulo} no se encuentra registrado")

    elif op == 4:
        registrar_prestamos(libros)
        print("Disponibilidad de préstamos actualizada correctamente")

    elif op == 5:
        mostrar_libros(libros)

    elif op == 6:
        print("Saliendo")
        break
    else:
        print("Opción no válida!")



    