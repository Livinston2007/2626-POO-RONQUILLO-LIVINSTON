# Archivo: mascota.py
# Clase Mascota para el Programa 2: Programación Orientada a Objetos

class Mascota:
    """
    Clase que representa una mascota.
    Demuestra los conceptos de POO: clase, objeto, atributos, métodos y abstracción.
    """
    
    # Atributos de clase (compartidos por todas las instancias)
    cantidad_mascotas = 0
    
    def __init__(self, nombre, especie, edad):
        """
        Constructor de la clase Mascota.
        
        Args:
            nombre (str): Nombre de la mascota
            especie (str): Especie de la mascota (perro, gato, ave, etc.)
            edad (int/float): Edad de la mascota en años
        """
        # Atributos de instancia
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        
        # Incrementar contador de mascotas
        Mascota.cantidad_mascotas += 1
    
    def mostrar_informacion(self):
        """
        Método que muestra la información de la mascota de forma organizada.
        """
        print("\n" + "="*50)
        print(f"INFORMACIÓN DE LA MASCOTA")
        print("="*50)
        print(f"Nombre:  {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad:    {self.edad} años")
        print("="*50)
    
    def hacer_sonido(self):
        """
        Método que emite el sonido característico de la mascota según su especie.
        Demuestra la abstracción: diferentes especies hacen diferentes sonidos.
        """
        sonidos = {
            "perro": "¡Guau guau!",
            "gato": "¡Miau miau!",
            "ave": "¡Pío pío!",
            "pajaro": "¡Pío pío!",
            "pájaro": "¡Pío pío!",
            "conejo": "¡Squeak squeak!",
            "hamster": "¡Squeak squeak!",
            "tortuga": "(sonido silencioso)",
            "pez": "(sonido silencioso)"
        }
        
        especie_lower = self.especie.lower()
        sonido = sonidos.get(especie_lower, "¡Hace un sonido!")
        
        print(f"\n{self.nombre} ({self.especie}) dice: {sonido}")
    
    def envejecer(self):
        """
        Método que incrementa la edad de la mascota.
        """
        self.edad += 1
        print(f"\n{self.nombre} ahora tiene {self.edad} años.")
    
    def cambiar_nombre(self, nuevo_nombre):
        """
        Método que cambia el nombre de la mascota.
        
        Args:
            nuevo_nombre (str): Nuevo nombre para la mascota
        """
        nombre_anterior = self.nombre
        self.nombre = nuevo_nombre
        print(f"\nEl nombre de {nombre_anterior} ha sido cambiado a {self.nombre}.")
    
    @staticmethod
    def obtener_cantidad_mascotas():
        """
        Método estático que retorna la cantidad total de mascotas creadas.
        """
        return Mascota.cantidad_mascotas
    
    def __str__(self):
        """
        Método especial que retorna una representación en texto de la mascota.
        """
        return f"{self.nombre} ({self.especie}, {self.edad} años)"
    
    def __repr__(self):
        """
        Método especial que retorna una representación más detallada de la mascota.
        """
        return f"Mascota(nombre='{self.nombre}', especie='{self.especie}', edad={self.edad})"
