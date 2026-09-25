from __future__ import annotations

import tkinter as tk
from pathlib import Path
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
        self.columnconfigure(0, weight=1)

        assets_dir = Path(__file__).resolve().parent.parent / "assets"
        logo_path = assets_dir / "logo_restaurante.png"
        self.logo_image = tk.PhotoImage(file=str(logo_path)) if logo_path.exists() else None

        if self.logo_image is not None:
            tk.Label(self, image=self.logo_image, bg="#f7f9ff", relief="flat").grid(row=0, column=0, pady=(0, 10))

        title = ttk.Label(self, text="Restaurante App", font=("Segoe UI", 18, "bold"))
        title.grid(row=1, column=0, pady=(0, 20))

        subtitle = ttk.Label(self, text="Iniciar sesión")
        subtitle.grid(row=2, column=0, pady=(0, 16))

        form = ttk.Frame(self, padding=18)
        form.grid(row=3, column=0, sticky="ew")
        form.columnconfigure(0, weight=1)

        ttk.Label(form, text="Usuario:").grid(row=0, column=0, sticky="w")
        self.usuario_entry = ttk.Entry(form, width=35)
        self.usuario_entry.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        self.usuario_entry.insert(0, "admin")

        ttk.Label(form, text="Contraseña:").grid(row=2, column=0, sticky="w")
        self.contrasena_entry = ttk.Entry(form, width=35, show="*")
        self.contrasena_entry.grid(row=3, column=0, sticky="ew", pady=(0, 10))
        self.contrasena_entry.insert(0, "1234")

        self.mensaje_label = ttk.Label(form, text="", foreground="red")
        self.mensaje_label.grid(row=4, column=0, sticky="w", pady=(5, 10))

        login_button = ttk.Button(form, text="Ingresar", command=self.validar_login)
        login_button.grid(row=5, column=0, sticky="ew")

        quick_button = ttk.Button(form, text="Usar admin por defecto", command=self.autocompletar_admin)
        quick_button.grid(row=6, column=0, sticky="ew", pady=(8, 0))

        self.usuario_entry.focus_set()

    def autocompletar_admin(self) -> None:
        self.usuario_entry.delete(0, tk.END)
        self.usuario_entry.insert(0, "admin")
        self.contrasena_entry.delete(0, tk.END)
        self.contrasena_entry.insert(0, "1234")
        self.mensaje_label.config(text="")

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
