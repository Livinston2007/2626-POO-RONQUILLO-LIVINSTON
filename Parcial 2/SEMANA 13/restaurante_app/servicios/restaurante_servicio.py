from __future__ import annotations

try:
    from restaurante_app.modelos.producto import Producto
    from restaurante_app.modelos.usuario import Usuario
    from restaurante_app.servicios.archivo_servicio import ArchivoServicio
except ImportError:  # pragma: no cover
    from modelos.producto import Producto
    from modelos.usuario import Usuario
    from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """Expone la lógica del negocio del restaurante para usuarios y productos."""

    def __init__(self, archivo_servicio: ArchivoServicio | None = None) -> None:
        self.archivo_servicio = archivo_servicio or ArchivoServicio()
        self.productos: list[Producto] = self.archivo_servicio.cargar_productos()
        self.usuarios: list[Usuario] = self.archivo_servicio.cargar_usuarios()

    def validar_acceso(self, usuario: str, contrasena: str) -> bool:
        usuario_normalizado = usuario.strip().lower()
        contrasena_normalizada = contrasena.strip()

        if not usuario_normalizado or not contrasena_normalizada:
            return False

        for usuario_registrado in self.usuarios:
            if usuario_registrado.usuario.lower() == usuario_normalizado:
                return usuario_registrado.contrasena == contrasena_normalizada
        return False

    def listar_usuarios(self) -> list[Usuario]:
        return list(self.usuarios)

    def listar_productos(self) -> list[Producto]:
        return list(self.productos)

    def obtener_total_productos(self) -> int:
        return len(self.productos)

    def obtener_total_usuarios(self) -> int:
        return len(self.usuarios)

    def buscar_producto_por_codigo(self, codigo: str) -> Producto | None:
        for producto in self.productos:
            if producto.codigo.lower() == codigo.strip().lower():
                return producto
        return None

    def buscar_usuario_por_nombre(self, usuario: str) -> Usuario | None:
        for usuario_registrado in self.usuarios:
            if usuario_registrado.usuario.lower() == usuario.strip().lower():
                return usuario_registrado
        return None
