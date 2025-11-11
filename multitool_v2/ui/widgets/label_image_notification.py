from tkinter import Label
from tkinter import Frame
from ui.theme.theme_default import LABEL_IMAGE_NOTIFICATION
from PIL import ImageTk
from ui.assets.image_factory.factorys import FactImgNotify

class LabelImgNotify(Label):
    def __init__(self,contenedor=Frame):
        super().__init__(master=contenedor,cnf=LABEL_IMAGE_NOTIFICATION)
        self.imagenes=FactImgNotify.create_imgs()
        self.config_place={"rely":0.5,"relx":0.5}
    
    def change_mod(self,mode:str):
        """valores mode: warning, cancel or validate """
        self.config(image=ImageTk.PhotoImage(self.imagenes[mode]))
    
    @property
    def get_configuracion_place(self):
        return self.config_place