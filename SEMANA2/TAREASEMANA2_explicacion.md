# Explicación detallada de TAREASEMANA2.py

Este documento explica, paso a paso, el código contenido en `TAREASEMANA2.py`. Está pensado para quienes recién comienzan con la Programación Orientada a Objetos (POO).

## Resumen

El programa define una clase llamada `CuentaBancaria` que modela una cuenta bancaria sencilla con:
- Atributos: titular, número de cuenta y saldo.
- Métodos: depositar, retirar, transferir, mostrar_saldo.

Al final del archivo hay un bloque `if __name__ == "__main__":` que muestra ejemplos de uso.

## Conceptos básicos de POO usados

- **Clase**: Es la plantilla o el molde (por ejemplo, `CuentaBancaria`).
- **Objeto / Instancia**: Es un ejemplar creado a partir de la clase (por ejemplo, `cuenta1`).
- **Atributos**: Datos que describe la instancia (por ejemplo, `saldo`).
- **Métodos**: Funciones que pertenecen a la clase y operan sobre sus atributos.

## Código: explicación línea por línea (o por bloques)

1) Definición de la clase

```python
class CuentaBancaria:
    """Clase que representa una cuenta bancaria sencilla."""
```

- `class CuentaBancaria:`: crea una nueva clase llamada `CuentaBancaria`.
- La cadena triple (docstring) describe brevemente la clase.

2) El constructor `__init__`

```python
    def __init__(self, titular: str, numero: str, saldo: float = 0.0):
        self.titular = titular
        self.numero = numero
        self.saldo = float(saldo)
```

- `__init__` se llama automáticamente al crear una instancia. Inicializa los atributos.
- `self` es la referencia al propio objeto (como `this` en otros lenguajes).
- `titular`, `numero`, `saldo` son parámetros que el programa pasa al crear la cuenta.
- `self.saldo = float(saldo)` convierte el saldo a número de tipo `float`.

3) Método `depositar`

```python
    def depositar(self, monto: float) -> None:
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor que 0")
        self.saldo += monto
```

- `depositar` recibe un `monto`. Si el monto no es positivo, lanza (raise) una excepción `ValueError`.
- Si el monto es válido, se suma al `self.saldo`.

4) Método `retirar`

```python
    def retirar(self, monto: float) -> bool:
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor que 0")
        if monto > self.saldo:
            return False
        self.saldo -= monto
        return True
```

- Valida que `monto` sea positivo.
- Verifica si hay saldo suficiente: si no lo hay, devuelve `False` (retirada fallida).
- Si la retirada es posible, resta el monto del saldo y devuelve `True`.

5) Método `transferir`

```python
    def transferir(self, monto: float, otra_cuenta: "CuentaBancaria") -> bool:
        if self.retirar(monto):
            otra_cuenta.depositar(monto)
            return True
        return False
```

- `transferir` intenta retirar de la cuenta origen; si `retirar` devuelve `True`, deposita en `otra_cuenta`.
- Reusa los métodos ya definidos (buena práctica: evitar duplicar lógica).

6) Método `mostrar_saldo` y `__str__`

```python
    def mostrar_saldo(self) -> str:
        return f"Titular: {self.titular} | Cuenta: {self.numero} | Saldo: ${self.saldo:.2f}"

    def __str__(self) -> str:
        return self.mostrar_saldo()
```

- `mostrar_saldo` devuelve una cadena con información formateada del estado de la cuenta.
- `__str__` permite que `print(cuenta1)` muestre la cadena devuelta por `mostrar_saldo`.
- La sintaxis `f"...{self.saldo:.2f}..."` es una f-string que formatea el número a 2 decimales.

7) Bloque principal: ejemplo de uso

```python
if __name__ == "__main__":
    cuenta1 = CuentaBancaria("Ana Pérez", "ES123456789", 500.0)
    cuenta2 = CuentaBancaria("Luis Gómez", "ES987654321", 150.0)

    print("Estado inicial:")
    print(cuenta1)
    print(cuenta2)

    print("\nAna deposita $200")
    cuenta1.depositar(200)
    print(cuenta1)

    print("\nLuis intenta retirar $200")
    ok = cuenta2.retirar(200)
    print("Retiro exitoso" if ok else "Fondos insuficientes")
    print(cuenta2)

    print("\nAna transfiere $100 a Luis")
    cuenta1.transferir(100, cuenta2)
    print(cuenta1)
    print(cuenta2)
```

- `if __name__ == "__main__":` asegura que este bloque se ejecute solo cuando el archivo se corre directamente, no cuando se importa como módulo.
- Crea dos cuentas y muestra operaciones básicas: depósito, retiro y transferencia.

## Notas y buenas prácticas para principiantes

- Manejo de dinero: usar `float` es aceptable para ejemplos, pero en proyectos reales conviene usar `Decimal` para evitar errores por redondeo.
- Validaciones: el código verifica montos negativos y fondos insuficientes, lo cual evita errores inesperados.
- Encapsulación: los atributos se acceden directamente (`self.saldo`), pero en diseños más grandes podrías usar propiedades (getters/setters) para controlar accesos.
- Reusar código: `transferir` reutiliza `retirar` y `depositar`, lo que facilita mantenimiento.

## Ejercicios sugeridos

1. Añadir una comisión por transferencia (por ejemplo 1% del monto).
2. Registrar un historial de transacciones en cada cuenta.
3. Cambiar `saldo` para usar `decimal.Decimal` y ver la diferencia en precisión.

---

Si quieres, puedo aplicar alguno de los ejercicios sugeridos y mostrarte el código modificado. También puedo añadir pruebas unitarias sencillas para practicar.
