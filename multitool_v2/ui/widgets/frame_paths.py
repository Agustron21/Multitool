from tkinter import Frame
class FramePaths(Frame):
    def __init__(self,contenedor):
        super().__init__(background="#3171d1",master=contenedor,bd=20,border=5,relief="groove",borderwidth=10)#width=1920/2,height=1080/3)
        self.configuracion_place = {"rely":0.5,"relx":0.5,"anchor":"center","relwidth":0.65,"relheight":0.40}
    @property
    def get_configuracion(self):
        return self.configuracion_place
