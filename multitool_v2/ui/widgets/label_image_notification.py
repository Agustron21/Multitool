from tkinter import Label
from tkinter import Frame
from PIL import ImageTk
from assets.image_factory.factorys import FactImgNotify
class LabelImgNotify(Label):
    def __init__(self,contenedor=Frame):
        super().__init__(master=contenedor)
        self.imagenes=FactImgNotify.create_imgs()
        self.config_place={"pady":0.5,"padx":0.5}
    
    def change_mod(self,mode="warning"| "validate" | "cancel"):
        self.config(image=ImageTk.PhotoImage(self.imagenes[mode]))
    
    @property
    def get_configuracion_place(self):
        return self.config_place