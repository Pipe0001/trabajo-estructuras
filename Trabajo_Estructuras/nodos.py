from salas import *

class NodoSala:
    def __init__(self, sala):
        self.sala = sala
        self.siguiente = None

class ListaSalas:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def esta_vacia(self):
        return self.inicio is None

    def agregar_al_final(self, sala):
        nuevo_nodo = NodoSala(sala)
        if self.esta_vacia():
            self.inicio = self.fin = nuevo_nodo
        else:
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo

    def recorrer(self):
        actual = self.inicio
        while actual is not None:
            print(f"Sala: {actual.sala}")
            actual = actual.siguiente

    def eliminar_ultima(self):
        if self.esta_vacia():
            print("No hay salas para eliminar.")
            return
        
        actual = self.inicio
        if actual.siguiente is None:
            self.inicio = self.fin = None
        else:
            while actual.siguiente != self.fin:
                actual = actual.siguiente
            actual.siguiente = None
            self.fin = actual

    def agregar_al_inicio(self, sala):
        nuevo_nodo = NodoSala(sala)
        if self.esta_vacia():
            self.inicio = self.fin = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.inicio
            self.inicio = nuevo_nodo

    def eliminar_primera(self):
        if self.esta_vacia():
            print("La lista de salas está vacía.")
            return
        self.inicio = self.inicio.siguiente
        if self.inicio is None:
            self.fin = None

    def buscar_por_tipo(self, tipo):
        actual = self.inicio
        salas_encontradas = []
        while actual is not None:
            if actual.sala.tipo == tipo:
                salas_encontradas.append(actual.sala)
            actual = actual.siguiente
        
        if salas_encontradas:
            print(f"Salas del tipo '{tipo}':")
            for sala in salas_encontradas:
                print(sala)
        else:
            print(f"No se encontraron salas del tipo '{tipo}'.")

    def buscar_por_capacidad(self, capacidad_min):
        actual = self.inicio
        resultado = []
        while actual is not None:
            if actual.sala.capacidad_maxima >= capacidad_min:
                resultado.append(actual.sala)
            actual = actual.siguiente

        if resultado:
            for sala in resultado:
                print(sala)
        else:
            print(f"No hay salas con capacidad mínima de {capacidad_min} personas.")

    def eliminar_sala_por_id(self, id_sala):
        if self.esta_vacia():
            print("No hay salas registradas.")
            return

        if self.inicio.sala.id_sala == id_sala:
            self.inicio = self.inicio.siguiente
            if self.inicio is None:
                self.fin = None
            print(f"Sala con ID {id_sala} eliminada.")
            return

        actual = self.inicio
        anterior = None

        while actual is not None:
            if actual.sala.id_sala == id_sala:
                if anterior is not None:
                    anterior.siguiente = actual.siguiente
                if actual == self.fin:
                    self.fin = anterior
                print(f"Sala con ID {id_sala} eliminada.")
                return
            anterior = actual
            actual = actual.siguiente

        print(f"No se encontró una sala con ID {id_sala}.")

    def listar_salas_disponibles(self):
        actual = self.inicio
        disponibles = False
        print("Salas disponibles:")
        while actual is not None:
            if actual.sala.estado.lower() == "disponible":
                print(f"ID: {actual.sala.id_sala}, Nombre: {actual.sala.nombre}")
                disponibles = True
            actual = actual.siguiente

        if not disponibles:
            print("No hay salas disponibles.")

    def listar_salas_reservadas(self):
        actual = self.inicio
        reservadas = False
        print("Salas reservadas:")
        while actual is not None:
            if actual.sala.estado.lower() == "reservada":
                print(f"ID: {actual.sala.id_sala}, Nombre: {actual.sala.nombre}")
                reservadas = True
            actual = actual.siguiente

        if not reservadas:
            print("No hay salas reservadas.")

    def cancelar_reserva(self):
        actual = self.inicio
        reservadas = []

        while actual is not None:
            if actual.sala.estado.lower() == "reservada":
                reservadas.append(actual.sala)
            actual = actual.siguiente

        if not reservadas:
            print("No hay salas reservadas para cancelar.")
            return

        print("Salas reservadas disponibles para cancelar:")
        for sala in reservadas:
            print(f"ID: {sala.id_sala}, Nombre: {sala.nombre}")

        id_cancelar = int(input("Ingrese el ID de la sala a cancelar: "))
        for sala in reservadas:
            if sala.id_sala == id_cancelar:
                sala.estado = "disponible"
                print(f"Reserva de la sala {sala.nombre} cancelada.")
                return
        print(f"Sala con ID {id_cancelar} no encontrada.")

    def reservar_sala(self):
        actual = self.inicio
        disponibles = []

        while actual is not None:
            if actual.sala.estado.lower() == "disponible":
                disponibles.append(actual.sala)
            actual = actual.siguiente

        if not disponibles:
            print("No hay salas disponibles para reservar.")
            return

        print("Salas disponibles para reserva:")
        for sala in disponibles:
            print(f"ID: {sala.id_sala}, Nombre: {sala.nombre}")

        id_reservar = int(input("Ingrese el ID de la sala que desea reservar: "))
        for sala in disponibles:
            if sala.id_sala == id_reservar:
                sala.estado = "reservada"
                print(f"La sala {sala.nombre} ha sido reservada.")
                return

        print(f"Sala con ID {id_reservar} no encontrada.")


