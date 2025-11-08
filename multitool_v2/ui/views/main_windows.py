from tkinter import Tk
from ui.theme.theme_default import FAMILY_FONT_NOTIFICATIONS
from ui.theme.theme_default import ESTILO_MAIN_WINDOW
class VentanaPrincipal(Tk):
    def __init__(self):
        super().__init__()
        self.title("Multitool")
        self.geometry("1920x1080") # default
        self.minsize=320
        self.maxsize=1080 #* a chekear 
        self.iconbitmap("D:\\proyectos\\multitool\\V2\\ui\\assets\\image\\caja-herramiento.ico")        
        self.config(cnf=ESTILO_MAIN_WINDOW)
        self.resizable(True,True)