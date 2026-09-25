from __future__ import annotations

import tkinter as tk
from pathlib import Path
from tkinter import ttk

try:
    from restaurante_app.servicios.restaurante_servicio import RestauranteServicio
except ImportError:  # pragma: no cover
    from servicios.restaurante_servicio import RestauranteServicio


class MainView(ttk.Frame):
    """Pantalla principal con navegación, productos, usuarios y ventas."""

    def __init__(self, parent: tk.Misc, restaurante_servicio: RestauranteServicio, on_logout) -> None:
        super().__init__(parent)
        self.restaurante_servicio = restaurante_servicio
        self.on_logout = on_logout
        self.configure(padding=15)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        navigation = ttk.Frame(self, padding=(0, 0, 15, 0))
        navigation.grid(row=0, column=0, sticky="ns")
        navigation.columnconfigure(0, weight=1)

        assets_dir = Path(__file__).resolve().parent.parent / "assets"
        logo_path = assets_dir / "logo_restaurante.png"
        self.logo_image = tk.PhotoImage(file=str(logo_path)) if logo_path.exists() else None

        if self.logo_image is not None:
            tk.Label(navigation, image=self.logo_image, bg="#eef4ff", relief="flat", padx=12, pady=8).grid(
                row=0, column=0, pady=(0, 10), sticky="ew"
            )
        ttk.Label(navigation, text="Menú", font=("Segoe UI", 14, "bold")).grid(row=1, column=0, pady=(0, 15), sticky="w")
        ttk.Button(navigation, text="Productos", command=self.mostrar_productos).grid(row=2, column=0, sticky="ew", pady=(0, 8))
        ttk.Button(navigation, text="Usuarios", command=self.mostrar_usuarios).grid(row=3, column=0, sticky="ew", pady=(0, 8))
        ttk.Button(navigation, text="Ventas", command=self.mostrar_ventas).grid(row=4, column=0, sticky="ew", pady=(0, 8))
        ttk.Button(navigation, text="Cerrar sesión", command=self.on_logout).grid(row=5, column=0, sticky="ew", pady=(16, 0))

        content = ttk.Frame(self)
        content.grid(row=0, column=1, sticky="nsew")
        content.columnconfigure(0, weight=1)
        content.rowconfigure(0, weight=1)

        self.productos_frame = ttk.Frame(content)
        self.usuarios_frame = ttk.Frame(content)
        self.ventas_frame = ttk.Frame(content)
        self.panels = {"productos": self.productos_frame, "usuarios": self.usuarios_frame, "ventas": self.ventas_frame}

        for panel in self.panels.values():
            panel.grid(row=0, column=0, sticky="nsew")

        self._construir_panel_productos()
        self._construir_panel_usuarios()
        self._construir_panel_ventas()
        self.mostrar_productos()

    def _construir_panel_productos(self) -> None:
        title = ttk.Label(self.productos_frame, text="Gestión de productos", font=("Segoe UI", 16, "bold"))
        title.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 12))

        form = ttk.LabelFrame(self.productos_frame, text="Formulario de producto")
        form.grid(row=1, column=0, sticky="ew", padx=(0, 12), pady=(0, 12))
        form.columnconfigure(1, weight=1)

        labels = [
            ("codigo", "Código", 0),
            ("nombre", "Nombre", 1),
            ("categoria", "Categoría", 2),
            ("precio", "Precio", 3),
            ("stock", "Stock", 4),
        ]
        self.product_fields = {}
        for key, label_text, row in labels:
            ttk.Label(form, text=f"{label_text}:").grid(row=row, column=0, padx=(12, 8), pady=6, sticky="w")
            entry = ttk.Entry(form)
            entry.grid(row=row, column=1, padx=(0, 12), pady=6, sticky="ew")
            self.product_fields[key] = entry

        actions = ttk.Frame(self.productos_frame)
        actions.grid(row=2, column=0, sticky="ew", pady=(0, 12))
        for index, (text, command) in enumerate(
            [
                ("Registrar", self.registrar_producto),
                ("Buscar", self.buscar_producto),
                ("Actualizar", self.actualizar_producto),
                ("Eliminar", self.eliminar_producto),
                ("Limpiar", self.limpiar_formulario),
            ]
        ):
            ttk.Button(actions, text=text, command=command).grid(row=0, column=index, padx=(0, 8), sticky="ew")

        self.estado_label = ttk.Label(self.productos_frame, text="", foreground="darkgreen")
        self.estado_label.grid(row=3, column=0, sticky="w", pady=(0, 8))

        tabla = ttk.LabelFrame(self.productos_frame, text="Listado de productos")
        tabla.grid(row=4, column=0, sticky="nsew")
        tabla.columnconfigure(0, weight=1)
        tabla.rowconfigure(0, weight=1)

        columns = ("codigo", "nombre", "categoria", "precio", "stock")
        self.product_table = ttk.Treeview(tabla, columns=columns, show="headings")
        for column in columns:
            self.product_table.heading(column, text=column.upper())
        self.product_table.column("codigo", width=100)
        self.product_table.column("nombre", width=180)
        self.product_table.column("categoria", width=110)
        self.product_table.column("precio", width=90)
        self.product_table.column("stock", width=70)
        self.product_table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    def _construir_panel_usuarios(self) -> None:
        ttk.Label(self.usuarios_frame, text="Consulta de usuarios", font=("Segoe UI", 16, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 12))
        frame = ttk.LabelFrame(self.usuarios_frame, text="Usuarios registrados")
        frame.grid(row=1, column=0, sticky="nsew")
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        self.user_table = ttk.Treeview(frame, columns=("usuario", "nombre", "contrasena"), show="headings")
        self.user_table.heading("usuario", text="USUARIO")
        self.user_table.heading("nombre", text="NOMBRE")
        self.user_table.heading("contrasena", text="CONTRASEÑA")
        self.user_table.column("usuario", width=150)
        self.user_table.column("nombre", width=220)
        self.user_table.column("contrasena", width=160)
        self.user_table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    def _construir_panel_ventas(self) -> None:
        ttk.Label(self.ventas_frame, text="Ventas del restaurante", font=("Segoe UI", 16, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 12))

        form = ttk.LabelFrame(self.ventas_frame, text="Registrar nueva venta")
        form.grid(row=1, column=0, sticky="ew", pady=(0, 12))
        form.columnconfigure(1, weight=1)

        ttk.Label(form, text="Usuario:").grid(row=0, column=0, padx=(12, 8), pady=8, sticky="w")
        self.usuario_combo = ttk.Combobox(form, state="readonly", width=40)
        self.usuario_combo.grid(row=0, column=1, padx=(0, 12), pady=8, sticky="ew")

        ttk.Label(form, text="Producto:").grid(row=1, column=0, padx=(12, 8), pady=8, sticky="w")
        self.producto_combo = ttk.Combobox(form, state="readonly", width=40)
        self.producto_combo.grid(row=1, column=1, padx=(0, 12), pady=8, sticky="ew")

        ttk.Button(form, text="Registrar venta", command=self.registrar_venta).grid(row=2, column=1, sticky="e", padx=(0, 12), pady=(6, 10))

        self.ventas_estado_label = ttk.Label(self.ventas_frame, text="", foreground="darkgreen")
        self.ventas_estado_label.grid(row=2, column=0, sticky="w", pady=(0, 8))

        tabla = ttk.LabelFrame(self.ventas_frame, text="Historial de ventas")
        tabla.grid(row=3, column=0, sticky="nsew")
        tabla.columnconfigure(0, weight=1)
        tabla.rowconfigure(0, weight=1)

        self.ventas_table = ttk.Treeview(tabla, columns=("usuario", "producto", "fecha"), show="headings")
        self.ventas_table.heading("usuario", text="USUARIO")
        self.ventas_table.heading("producto", text="PRODUCTO")
        self.ventas_table.heading("fecha", text="FECHA")
        self.ventas_table.column("usuario", width=160)
        self.ventas_table.column("producto", width=260)
        self.ventas_table.column("fecha", width=180)
        self.ventas_table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self._cargar_combos_ventas()
        self._cargar_ventas_tabla()

    def mostrar_productos(self) -> None:
        self._mostrar_panel("productos")
        self._cargar_productos_tabla()

    def mostrar_usuarios(self) -> None:
        self._mostrar_panel("usuarios")
        self._cargar_usuarios_tabla()

    def mostrar_ventas(self) -> None:
        self._mostrar_panel("ventas")
        self._cargar_combos_ventas()
        self._cargar_ventas_tabla()

    def _mostrar_panel(self, nombre: str) -> None:
        for panel_name, panel in self.panels.items():
            if panel_name == nombre:
                panel.grid()
            else:
                panel.grid_remove()

    def _cargar_productos_tabla(self) -> None:
        for item in self.product_table.get_children():
            self.product_table.delete(item)

        for producto in self.restaurante_servicio.listar_productos():
            self.product_table.insert(
                "",
                tk.END,
                values=(producto.codigo, producto.nombre, producto.categoria, f"${producto.precio:.2f}", producto.stock),
            )

    def _cargar_usuarios_tabla(self) -> None:
        for item in self.user_table.get_children():
            self.user_table.delete(item)

        for usuario in self.restaurante_servicio.listar_usuarios():
            self.user_table.insert("", tk.END, values=(usuario.usuario, usuario.nombre, usuario.contrasena))

    def _cargar_combos_ventas(self) -> None:
        usuarios = [usuario.usuario for usuario in self.restaurante_servicio.listar_usuarios()]
        productos = [f"{producto.codigo} - {producto.nombre}" for producto in self.restaurante_servicio.listar_productos()]
        self.usuario_combo["values"] = usuarios
        self.producto_combo["values"] = productos

        if usuarios:
            self.usuario_combo.set(usuarios[0])
        else:
            self.usuario_combo.set("")

        if productos:
            self.producto_combo.set(productos[0])
        else:
            self.producto_combo.set("")

    def _cargar_ventas_tabla(self) -> None:
        for item in self.ventas_table.get_children():
            self.ventas_table.delete(item)

        for venta in self.restaurante_servicio.listar_ventas():
            producto = self.restaurante_servicio.buscar_producto_por_codigo(venta.producto_codigo)
            nombre_producto = producto.nombre if producto is not None else venta.producto_codigo
            self.ventas_table.insert("", tk.END, values=(venta.usuario, nombre_producto, venta.fecha))

    def _leer_producto_formulario(self) -> dict[str, str | float | int]:
        return {
            "codigo": self.product_fields["codigo"].get().strip(),
            "nombre": self.product_fields["nombre"].get().strip(),
            "categoria": self.product_fields["categoria"].get().strip(),
            "precio": self.product_fields["precio"].get().strip(),
            "stock": self.product_fields["stock"].get().strip(),
        }

    def _mostrar_estado(self, mensaje: str, es_error: bool = False) -> None:
        self.estado_label.config(text=mensaje, foreground="red" if es_error else "darkgreen")

    def _mostrar_estado_venta(self, mensaje: str, es_error: bool = False) -> None:
        self.ventas_estado_label.config(text=mensaje, foreground="red" if es_error else "darkgreen")

    def limpiar_formulario(self) -> None:
        for entry in self.product_fields.values():
            entry.delete(0, tk.END)
        self.product_fields["codigo"].focus_set()

    def registrar_producto(self) -> None:
        datos = self._leer_producto_formulario()
        try:
            self.restaurante_servicio.registrar_producto(
                codigo=datos["codigo"],
                nombre=datos["nombre"],
                categoria=datos["categoria"],
                precio=datos["precio"],
                stock=datos["stock"],
            )
            self.limpiar_formulario()
            self._cargar_productos_tabla()
            self._mostrar_estado("Producto registrado correctamente.")
            self._cargar_combos_ventas()
        except ValueError as error:
            self._mostrar_estado(str(error), es_error=True)

    def buscar_producto(self) -> None:
        codigo = self.product_fields["codigo"].get().strip()
        if not codigo:
            self._mostrar_estado("Debe ingresar un código para buscar.", es_error=True)
            return

        producto = self.restaurante_servicio.buscar_producto_por_codigo(codigo)
        if producto is None:
            self._mostrar_estado(f"No se encontró el producto {codigo}.", es_error=True)
            return

        self.product_fields["codigo"].delete(0, tk.END)
        self.product_fields["codigo"].insert(0, producto.codigo)
        self.product_fields["nombre"].delete(0, tk.END)
        self.product_fields["nombre"].insert(0, producto.nombre)
        self.product_fields["categoria"].delete(0, tk.END)
        self.product_fields["categoria"].insert(0, producto.categoria)
        self.product_fields["precio"].delete(0, tk.END)
        self.product_fields["precio"].insert(0, str(producto.precio))
        self.product_fields["stock"].delete(0, tk.END)
        self.product_fields["stock"].insert(0, str(producto.stock))
        self._mostrar_estado(f"Producto {producto.codigo} encontrado.")

    def actualizar_producto(self) -> None:
        datos = self._leer_producto_formulario()
        if not datos["codigo"]:
            self._mostrar_estado("Debe ingresar el código del producto a actualizar.", es_error=True)
            return

        try:
            self.restaurante_servicio.actualizar_producto(
                codigo=datos["codigo"],
                nombre=datos["nombre"],
                categoria=datos["categoria"],
                precio=float(datos["precio"]) if str(datos["precio"]).strip() else None,
                stock=int(datos["stock"]) if str(datos["stock"]).strip() else None,
            )
            self._mostrar_estado("Producto actualizado correctamente.")
            self._cargar_productos_tabla()
            self._cargar_combos_ventas()
        except (TypeError, ValueError) as error:
            self._mostrar_estado(str(error), es_error=True)

    def eliminar_producto(self) -> None:
        codigo = self.product_fields["codigo"].get().strip()
        if not codigo:
            self._mostrar_estado("Debe ingresar un código para eliminar.", es_error=True)
            return

        try:
            self.restaurante_servicio.eliminar_producto(codigo)
            self.limpiar_formulario()
            self._cargar_productos_tabla()
            self._mostrar_estado(f"Producto {codigo} eliminado.")
            self._cargar_combos_ventas()
        except ValueError as error:
            self._mostrar_estado(str(error), es_error=True)

    def registrar_venta(self) -> None:
        usuario = self.usuario_combo.get().strip()
        producto = self.producto_combo.get().strip()
        if not usuario:
            self._mostrar_estado_venta("Debe seleccionar un usuario.", es_error=True)
            return
        if not producto:
            self._mostrar_estado_venta("Debe seleccionar un producto.", es_error=True)
            return

        codigo_producto = producto.split(" - ", 1)[0].strip()
        try:
            self.restaurante_servicio.registrar_venta(usuario=usuario, producto=codigo_producto)
            self._mostrar_estado_venta("Venta registrada correctamente.")
            self._cargar_ventas_tabla()
            self._cargar_combos_ventas()
        except ValueError as error:
            self._mostrar_estado_venta(str(error), es_error=True)
