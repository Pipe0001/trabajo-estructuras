from nodos import *

try:
    opcion_menu = 0
    gestor_salas = ListaSalas()

    while True:
        print("\n--- MENÚ DE ADMINISTRACIÓN DE SALAS ---")
        print("1. Añadir nueva sala")
        print("2. Eliminar sala por ID")
        print("3. Ver salas disponibles")
        print("4. Ver salas reservadas")
        print("5. Realizar una reserva")
        print("6. Anular una reserva")
        print("7. Modificar una reserva")
        print("8. Buscar sala por tipo")
        print("9. Buscar sala según capacidad")
        print("10. Ver salas reservadas por tipo")
        print("11. Calcular ingresos totales")
        print("12. Salir")

        opcion_menu = input("Seleccione una opción: ")

        if opcion_menu == "1":
            id_nueva_sala = int(input("Introduzca el ID de la sala: "))
            categoria_sala = input("Indique el tipo de sala (Pequeña, Mediana, Grande): ")
            max_capacidad = int(input("Indique la capacidad máxima de la sala: "))
            nombre_sala = input("Introduzca el nombre de la sala: ")
            precio_hora = float(input("Introduzca la tarifa por hora: "))
            estado_sala = input("Estado de la sala (Disponible/Reservada): ")
            nueva_sala = Sala(id_nueva_sala, categoria_sala, max_capacidad, nombre_sala, precio_hora, estado_sala)
            gestor_salas.agregar_al_final(nueva_sala)

        elif opcion_menu == "2":
            id_eliminar = int(input("Introduzca el ID de la sala a eliminar: "))
            gestor_salas.eliminar_sala_por_id(id_eliminar)

        elif opcion_menu == "3":
            gestor_salas.mostrar_salas_disponibles()

        elif opcion_menu == "4":
            gestor_salas.mostrar_salas_reservadas()

        elif opcion_menu == "5":
            gestor_salas.reservar_una_sala()

        elif opcion_menu == "6":
            gestor_salas.anular_reserva()

        elif opcion_menu == "7":
            gestor_salas.modificar_reserva()

        elif opcion_menu == "8":
            tipo_sala = input("Introduzca el tipo de sala a buscar: ")
            gestor_salas.buscar_sala_por_tipo(tipo_sala)

        elif opcion_menu == "9":
            capacidad_minima = int(input("Introduzca la capacidad mínima de la sala: "))
            gestor_salas.buscar_sala_por_capacidad(capacidad_minima)

        elif opcion_menu == "10":
            tipo_reserva = input("Introduzca el tipo de sala reservada a visualizar: ")
            gestor_salas.mostrar_reservadas_por_tipo(tipo_reserva)

        elif opcion_menu == "11":
            total_ingresos = gestor_salas.calcular_ingresos_totales()
            print(f"El ingreso total por las salas reservadas es: ${total_ingresos:.2f}")

        elif opcion_menu == "12":
            print("Gracias por usar el sistema de administración de salas. ¡Hasta luego!")
            break

        else:
            print("Opción incorrecta. Inténtalo de nuevo.")

except ValueError:
    print("Error: Entrada no válida. Por favor, introduce los datos correctamente.")
except Exception as error:
    print(f"Ha ocurrido un error inesperado: {error}")
