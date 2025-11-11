from tkinter import Tk,PhotoImage
from ui.theme.theme_default import ESTILO_MAIN_WINDOW
from screeninfo import get_monitors
# from configparser import ConfigParser
class VentanaPrincipal(Tk):
    def __init__(self):
        resultado=get_monitors()
        super().__init__()
        self.title("Multitool")
        self.geometry(f"{resultado[0].width}x{resultado[0].height}") # default
        self.config(cnf=ESTILO_MAIN_WINDOW)
        self.resizable(True,True)
        self.iconphoto(True,PhotoImage(file="D:\\proyectos\\proyectX\\multitool_v2\\ui\\assets\\image\\caja-de-herramientas.png")) #esta opcion es multiplataforma
        