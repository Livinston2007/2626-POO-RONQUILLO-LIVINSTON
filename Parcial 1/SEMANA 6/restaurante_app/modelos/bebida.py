from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, precio, disponibilidad, volumen_ml, tipo_bebida):
        # Utilizamos super() para invocar el constructor de la clase padre
        super().__init__(nombre, precio, disponibilidad)
        self.volumen_ml = volumen_ml
        self.tipo_bebida = tipo_bebida  # Por ejemplo: 'Fría', 'Caliente', 'Alcohólica'

    # Sobrescribimos el método mostrar_informacion() (Polimorfismo)
    def mostrar_informacion(self):
        # Obtenemos la información básica de la clase padre
        info_base = super().mostrar_informacion()
        # Añadimos la información específica de la bebida
        return f"{info_base} | Tipo: Bebida ({self.tipo_bebida}) | Volumen: {self.volumen_ml} ml"
