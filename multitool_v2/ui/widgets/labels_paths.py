from tkinter import Label
from tkinter import Frame
from ui.theme.theme_default import LABEL_PATHS_STYLE
class LabelsPaths(Label):
    
    def __init__(self,seccion:str,contenedor:Frame,posrely:float):
        super().__init__(text=seccion,master=contenedor)
        self.config(cnf=LABEL_PATHS_STYLE)
        self.configuracion_place = {"rely":posrely}
    
    @property
    def get_configuracion(self):
        return self.configuracion_place