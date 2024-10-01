
class Espacio:
    def __init__(self, id_espacio, categoria, max_personas, nombre_espacio, precio_hora, estado_espacio="Disponible"):
        self.id_espacio = id_espacio              
        self.categoria = categoria                
        self.max_personas = max_personas          
        self.nombre_espacio = nombre_espacio       
        self.precio_hora = precio_hora            
        self.estado_espacio = estado_espacio       

    def __str__(self):
        return (f"Detalles del espacio:\n"
                f"ID: {self.id_espacio}\n"
                f"Nombre: {self.nombre_espacio}\n"
                f"Categoría: {self.categoria}\n"
                f"Capacidad máxima: {self.max_personas}\n"
                f"Tarifa por hora: ${self.precio_hora:.2f}\n"
                f"Estado: {self.estado_espacio}\n")

    
    def marcar_disponible(self):
        self.estado_espacio = "Disponible"
        print(f"El espacio {self.id_espacio} está disponible para reservas.")

   
    def marcar_reservado(self):
        self.estado_espacio = "Reservado"
        print(f"El espacio {self.id_espacio} ha sido reservado.")
