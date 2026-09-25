from __future__ import annotations

try:
    from restaurante_app.modelos.producto import Producto
    from restaurante_app.modelos.usuario import Usuario
    from restaurante_app.modelos.venta import Venta
    from restaurante_app.servicios.archivo_servicio import ArchivoServicio
except ImportError:  # pragma: no cover
    from modelos.producto import Producto
    from modelos.usuario import Usuario
    from modelos.venta import Venta
    from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """Centraliza la lógica del negocio, validaciones y persistencia."""

    def __init__(self, archivo_servicio: ArchivoServicio | None = None) -> None:
        self.archivo_servicio = archivo_servicio or ArchivoServicio()
        self.productos: list[Producto] = self.archivo_servicio.cargar_productos()
        self.usuarios: list[Usuario] = self.archivo_servicio.cargar_usuarios()
        self.ventas: list[Venta] = self.archivo_servicio.cargar_ventas()

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

    def listar_ventas(self) -> list[Venta]:
        return list(self.ventas)

    def obtener_total_productos(self) -> int:
        return len(self.productos)

    def obtener_total_usuarios(self) -> int:
        return len(self.usuarios)

    def obtener_total_ventas(self) -> int:
        return len(self.ventas)

    def buscar_producto_por_codigo(self, codigo: str) -> Producto | None:
        codigo_normalizado = codigo.strip().lower()
        for producto in self.productos:
            if producto.codigo.lower() == codigo_normalizado:
                return producto
        return None

    def buscar_usuario_por_nombre(self, usuario: str) -> Usuario | None:
        usuario_normalizado = usuario.strip().lower()
        for usuario_registrado in self.usuarios:
            if usuario_registrado.usuario.lower() == usuario_normalizado:
                return usuario_registrado
        return None

    def registrar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int,
    ) -> Producto:
        codigo_normalizado = (codigo or "").strip()
        if not codigo_normalizado:
            raise ValueError("El código del producto no puede estar vacío.")
        if self.buscar_producto_por_codigo(codigo_normalizado):
            raise ValueError(f"El producto con código {codigo_normalizado} ya existe.")

        producto = Producto(
            codigo=codigo_normalizado,
            nombre=nombre,
            categoria=categoria,
            precio=precio,
            stock=stock,
        )
        self.productos.append(producto)
        self.archivo_servicio.guardar_productos(self.productos)
        return producto

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str | None = None,
        categoria: str | None = None,
        precio: float | None = None,
        stock: int | None = None,
    ) -> Producto:
        codigo_normalizado = (codigo or "").strip()
        producto = self.buscar_producto_por_codigo(codigo_normalizado)
        if producto is None:
            raise ValueError(f"No existe un producto con el código {codigo_normalizado}.")

        if nombre is not None:
            producto.nombre = nombre.strip()
            if not producto.nombre:
                raise ValueError("El nombre del producto no puede estar vacío.")

        if categoria is not None:
            producto.categoria = categoria.strip()
            if not producto.categoria:
                raise ValueError("La categoría del producto no puede estar vacía.")

        if precio is not None:
            precio_numerico = float(precio)
            if precio_numerico < 0:
                raise ValueError("El precio del producto no puede ser negativo.")
            producto.precio = precio_numerico

        if stock is not None:
            stock_numerico = int(stock)
            if stock_numerico < 0:
                raise ValueError("El stock del producto no puede ser negativo.")
            producto.stock = stock_numerico

        self.archivo_servicio.guardar_productos(self.productos)
        return producto

    def eliminar_producto(self, codigo: str) -> Producto:
        codigo_normalizado = (codigo or "").strip()
        producto = self.buscar_producto_por_codigo(codigo_normalizado)
        if producto is None:
            raise ValueError(f"No existe un producto con el código {codigo_normalizado}.")

        self.productos.remove(producto)
        self.archivo_servicio.guardar_productos(self.productos)
        return producto

    def registrar_venta(self, usuario: str, producto: str) -> Venta:
        usuario_normalizado = (usuario or "").strip()
        producto_normalizado = (producto or "").strip()

        if not usuario_normalizado:
            raise ValueError("Debe seleccionar un usuario para la venta.")
        if not producto_normalizado:
            raise ValueError("Debe seleccionar un producto para la venta.")

        usuario_registrado = self.buscar_usuario_por_nombre(usuario_normalizado)
        if usuario_registrado is None:
            raise ValueError(f"El usuario {usuario_normalizado} no existe en el sistema.")

        producto_seleccionado = self.buscar_producto_por_codigo(producto_normalizado)
        if producto_seleccionado is None:
            raise ValueError(f"El producto {producto_normalizado} no existe en el sistema.")
        if producto_seleccionado.stock <= 0:
            raise ValueError(f"El producto {producto_seleccionado.nombre} no tiene stock disponible.")

        venta = Venta(
            usuario=usuario_registrado.usuario,
            producto_codigo=producto_seleccionado.codigo,
        )
        self.ventas.append(venta)
        producto_seleccionado.stock -= 1
        self.archivo_servicio.guardar_ventas(self.ventas)
        self.archivo_servicio.guardar_productos(self.productos)
        return venta
