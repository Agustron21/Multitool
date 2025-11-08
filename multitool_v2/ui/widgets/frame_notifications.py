from tkinter import Frame
from tkinter import Tk
from ui.theme.theme_default import FRAME_NOTIFICATION_STANDARD
class FrameNotify(Frame):
    #* hacer que mediantee sea mas grave el asunto cambie el color y el borde sea mas grueso
    #* incluido el grosor de la fuente
    def __init__(self,contenedor:Tk):
        super().__init__(master=contenedor)
        self.config(cnf=FRAME_NOTIFICATION_STANDARD)
        self.configuracion_place={"anchor":"w","rely":0.5,"relx":0.5,"relwidth":0.25,"bordermode":"inside"}
    @property
    def get_configuracion(self):
        return self.configuracion_place
    