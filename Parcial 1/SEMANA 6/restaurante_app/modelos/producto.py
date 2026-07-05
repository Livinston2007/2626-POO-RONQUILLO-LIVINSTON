class Producto:
    def __init__(self, nombre, precio, disponibilidad=True):
        self.nombre = nombre
        self.__precio = precio  # Atributo encapsulado (privado)
        self.disponibilidad = disponibilidad

    # Método de acceso (getter) para el precio
    def obtener_precio(self):
        return self.__precio

    # Método de modificación (setter) para el precio con validación
    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
            print(f"Precio de '{self.nombre}' actualizado a ${self.__precio:.2f}.")
        else:
            print(f"Error: El precio para '{self.nombre}' no puede ser negativo o cero.")

    # Método general que será sobrescrito
    def mostrar_informacion(self):
        estado = "Disponible" if self.disponibilidad else "Agotado"
        return f"Producto: {self.nombre} | Precio: ${self.__precio:.2f} | Estado: {estado}"
