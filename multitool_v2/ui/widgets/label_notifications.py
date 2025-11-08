from tkinter import Label
from tkinter import Frame
from tkinter import StringVar
from ui.theme.theme_default import LABEL_NOTIFICATION_ALERT,LABEL_NOTIFICATION_INVALID,LABEL_NOTIFICATION_VALID
class LabelNotifications(Label):
    def __init__(self,contenedor:Frame):
        self.control_var_label=StringVar(value="")
        self.configuracion_place={"rely":"0.5"}
        super().__init__(textvariable=self.control_var_label,master=contenedor)
    
    @property
    def get_configuracion(self):
        return self.configuracion_place
    
    def msg_notify_valid(self):
        self.control_var_label="Las rutas ingresadas son validas"
        self.config(cnf=LABEL_NOTIFICATION_VALID)
    
    def msg_notify_invalid(self):
        self.control_var_label="Una de las rutas ingresadas es invalida"
        self.config(cnf=LABEL_NOTIFICATION_INVALID)

    def msg_notify_alert(self):
        self.control_var_label="Para continuar ingrese ambas rutas"
        self.config(cnf=LABEL_NOTIFICATION_ALERT)