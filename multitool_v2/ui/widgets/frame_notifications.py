from tkinter import Frame
from tkinter import Tk
from ui.theme.theme_default import FRAME_NOTIFICATION_STANDARD,FRAME_NOTIFICATION_ALERT,FRAME_NOTIFICATION_INVALID,FRAME_NOTIFICATION_VALID
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
    @classmethod
    def set_mode_valid(cls):
        cls.config(FRAME_NOTIFICATION_VALID)
    @classmethod
    def set_mode_invalid(cls):
        cls.config(FRAME_NOTIFICATION_INVALID)
    @classmethod
    def set_mode_alert(cls):
        cls.config(FRAME_NOTIFICATION_ALERT)
    