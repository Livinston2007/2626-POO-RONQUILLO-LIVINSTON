from __future__ import annotations

import tkinter as tk

try:
    from restaurante_app.servicios.archivo_servicio import ArchivoServicio
    from restaurante_app.servicios.restaurante_servicio import RestauranteServicio
    from restaurante_app.ui.login_view import LoginView
    from restaurante_app.ui.main_view import MainView
except ImportError:  # pragma: no cover
    from servicios.archivo_servicio import ArchivoServicio
    from servicios.restaurante_servicio import RestauranteServicio
    from ui.login_view import LoginView
    from ui.main_view import MainView


class RestauranteApp:
    """Gestiona la ventana principal y el cambio entre vistas."""

    def __init__(self, root: tk.Tk | None = None) -> None:
        self.root = root or tk.Tk()
        self.root.title("Restaurante App")
        self.root.geometry("900x600")
        self.root.minsize(700, 500)

        self.restaurante_servicio = RestauranteServicio(ArchivoServicio())

        self.login_view = LoginView(self.root, self.restaurante_servicio, self.mostrar_main)
        self.main_view = MainView(self.root, self.restaurante_servicio, self.mostrar_login)

        self.frames = {
            "login": self.login_view,
            "main": self.main_view,
        }

        self.mostrar_login()

    def mostrar_frame(self, nombre: str) -> None:
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[nombre].pack(fill="both", expand=True)

    def mostrar_login(self) -> None:
        self.mostrar_frame("login")

    def mostrar_main(self) -> None:
        self.mostrar_frame("main")
        self.main_view.mostrar_productos()

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    app = RestauranteApp()
    app.run()
