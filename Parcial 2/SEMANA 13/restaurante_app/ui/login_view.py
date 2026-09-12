from __future__ import annotations

import tkinter as tk
from tkinter import ttk

try:
    from restaurante_app.servicios.restaurante_servicio import RestauranteServicio
except ImportError:  # pragma: no cover
    from servicios.restaurante_servicio import RestauranteServicio


class LoginView(ttk.Frame):
    """Pantalla de acceso con usuario y contraseña."""

    def __init__(self, parent: tk.Misc, restaurante_servicio: RestauranteServicio, on_login) -> None:
        super().__init__(parent)
        self.restaurante_servicio = restaurante_servicio
        self.on_login = on_login

        self.configure(padding=30)

        title = ttk.Label(self, text="Restaurante App", font=("Segoe UI", 18, "bold"))
        title.pack(pady=(0, 20))

        subtitle = ttk.Label(self, text="Iniciar sesión")
        subtitle.pack(pady=(0, 20))

        ttk.Label(self, text="Usuario:").pack(anchor="w")
        self.usuario_entry = ttk.Entry(self, width=35)
        self.usuario_entry.pack(fill="x", pady=(0, 10))

        ttk.Label(self, text="Contraseña:").pack(anchor="w")
        self.contrasena_entry = ttk.Entry(self, width=35, show="*")
        self.contrasena_entry.pack(fill="x", pady=(0, 10))

        self.mensaje_label = ttk.Label(self, text="", foreground="red")
        self.mensaje_label.pack(anchor="w", pady=(5, 10))

        login_button = ttk.Button(self, text="Ingresar", command=self.validar_login)
        login_button.pack(fill="x", pady=(10, 0))

    def validar_login(self) -> None:
        usuario = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get().strip()

        if not usuario or not contrasena:
            self.mensaje_label.config(text="Debe completar usuario y contraseña.")
            return

        if not self.restaurante_servicio.validar_acceso(usuario, contrasena):
            self.mensaje_label.config(text="Credenciales incorrectas.")
            self.contrasena_entry.delete(0, tk.END)
            self.usuario_entry.focus_set()
            return

        self.mensaje_label.config(text="")
        self.contrasena_entry.delete(0, tk.END)
        self.usuario_entry.delete(0, tk.END)
        self.on_login()
