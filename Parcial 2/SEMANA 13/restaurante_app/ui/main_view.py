from __future__ import annotations

import tkinter as tk
from tkinter import ttk

try:
    from restaurante_app.servicios.restaurante_servicio import RestauranteServicio
except ImportError:  # pragma: no cover
    from servicios.restaurante_servicio import RestauranteServicio


class MainView(ttk.Frame):
    """Pantalla principal con información del restaurante."""

    def __init__(self, parent: tk.Misc, restaurante_servicio: RestauranteServicio, on_logout) -> None:
        super().__init__(parent)
        self.restaurante_servicio = restaurante_servicio
        self.on_logout = on_logout

        self.configure(padding=15)

        header = ttk.Label(self, text="Panel principal", font=("Segoe UI", 16, "bold"))
        header.pack(anchor="w", pady=(0, 10))

        actions = ttk.Frame(self)
        actions.pack(fill="x", pady=(0, 10))

        ttk.Button(actions, text="Productos", command=self.mostrar_productos).pack(side="left", padx=(0, 10))
        ttk.Button(actions, text="Usuarios", command=self.mostrar_usuarios).pack(side="left", padx=(0, 10))
        ttk.Button(actions, text="Ventas (pendiente)", state="disabled").pack(side="left", padx=(0, 10))
        ttk.Button(actions, text="Cerrar sesión", command=self.on_logout).pack(side="right")

        info_frame = ttk.LabelFrame(self, text="Información")
        info_frame.pack(fill="both", expand=True)

        self.info_text = tk.Text(info_frame, wrap="word", height=18, width=100)
        self.info_text.pack(fill="both", expand=True, padx=10, pady=10)
        self.info_text.config(state="disabled")

        self.mostrar_productos()

    def _set_text(self, texto: str) -> None:
        self.info_text.config(state="normal")
        self.info_text.delete("1.0", tk.END)
        self.info_text.insert(tk.END, texto)
        self.info_text.config(state="disabled")

    def mostrar_productos(self) -> None:
        productos = self.restaurante_servicio.listar_productos()
        if not productos:
            self._set_text("No hay productos registrados.")
            return

        contenido = ["PRODUCTOS REGISTRADOS\n"]
        for producto in productos:
            contenido.append(f"- {producto.mostrar_informacion()}\n")
        contenido.append(f"\nTotal: {len(productos)}")
        self._set_text("".join(contenido))

    def mostrar_usuarios(self) -> None:
        usuarios = self.restaurante_servicio.listar_usuarios()
        if not usuarios:
            self._set_text("No hay usuarios registrados.")
            return

        contenido = ["USUARIOS REGISTRADOS\n"]
        for usuario in usuarios:
            contenido.append(f"- {usuario.mostrar_informacion()}\n")
        contenido.append(f"\nTotal: {len(usuarios)}")
        self._set_text("".join(contenido))
