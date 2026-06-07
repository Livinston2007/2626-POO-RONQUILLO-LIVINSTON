class CuentaBancaria:
	"""Clase que representa una cuenta bancaria sencilla."""

	def __init__(self, titular: str, numero: str, saldo: float = 0.0):
		self.titular = titular
		self.numero = numero
		self.saldo = float(saldo)

	def depositar(self, monto: float) -> None:
		if monto <= 0:
			raise ValueError("El monto a depositar debe ser mayor que 0")
		self.saldo += monto

	def retirar(self, monto: float) -> bool:
		if monto <= 0:
			raise ValueError("El monto a retirar debe ser mayor que 0")
		if monto > self.saldo:
			return False
		self.saldo -= monto
		return True

	def transferir(self, monto: float, otra_cuenta: "CuentaBancaria") -> bool:
		if self.retirar(monto):
			otra_cuenta.depositar(monto)
			return True
		return False

	def mostrar_saldo(self) -> str:
		return f"Titular: {self.titular} | Cuenta: {self.numero} | Saldo: ${self.saldo:.2f}"

	def __str__(self) -> str:
		return self.mostrar_saldo()


if __name__ == "__main__":
	# Ejemplo de uso
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

