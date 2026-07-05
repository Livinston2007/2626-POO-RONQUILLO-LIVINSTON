from modelos.producto import Producto

class Platillo(Producto):
    def __init__(self, nombre, precio, disponibilidad, calorias, tiempo_preparacion):
        # Utilizamos super() para invocar el constructor de la clase padre
        super().__init__(nombre, precio, disponibilidad)
        self.calorias = calorias
        self.tiempo_preparacion = tiempo_preparacion  # Tiempo en minutos

    # Sobrescribimos el método mostrar_informacion() (Polimorfismo)
    def mostrar_informacion(self):
        # Obtenemos la información básica de la clase padre
        info_base = super().mostrar_informacion()
        # Añadimos la información específica del platillo
        return f"{info_base} | Tipo: Platillo | Calorías: {self.calorias} kcal | Prep: {self.tiempo_preparacion} min"
