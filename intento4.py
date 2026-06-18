import funciones as fn

coleccion_vehiculos = []

while True:

    fn.menu()
    opcionMenu = fn.opcion_menu()

    match opcionMenu:

        case 1:
            fn.agregar_vehiculo(coleccion_vehiculos)
        case 2:

            buscar = input("Ingrese el modelo que desea buscar: ").lower()
            posicion = fn.buscar_vehiculo(coleccion_vehiculos, buscar)

            if posicion != -1:

                vehiculo = coleccion_vehiculos[posicion]

                print("---- VEHICULO ENCONTRADO ----")
                print(f"Modelo: {buscar} / Año: {vehiculo["año"]} / Precio: {vehiculo["precio"]} / Disponible: {vehiculo["disponible"]}")
                print("")      
            else:
                print("Vehiculo no encontrado.")

        case 3:

            eliminar = input("Que modelo desea eliminar: ").lower()
            posicion = fn.buscar_vehiculo(coleccion_vehiculos, eliminar)

            if posicion != -1:

                coleccion_vehiculos.pop(posicion)
                print(f"Vehiculo {eliminar} eliminado éxitosamente!")
            else:
                print(f"El vehiculo {eliminar} no se encuentra registrado.")

        case 4:
            fn.actualizar_disponibilidad(coleccion_vehiculos)
            print("--- VEHICULOS ACTUALIZADOS! ---")

        case 5:
            fn.mostrar_vehiculos(coleccion_vehiculos)
        case 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
            break
        case _:
            print("ERROR: Ingrese una opcion dentro del menu (1-6)")
            

                    
