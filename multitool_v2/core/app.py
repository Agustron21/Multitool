import tkinter.ttk as ttk
import subprocess as sb
import tkinter as tk
import re as regex
import shelve
from ui.views.main_windows import VentanaPrincipal
from ui.widgets.frame_paths import FramePaths
from ui.widgets.labels_paths import LabelsPaths
# from carga_datos import carga_dat
archivo_extesiones="./extenciones.dat" #* la idea es deserializar este archivo para que nosotros podamos tener de referencia todos las extensiones que permitiremos copiar y pegar
#? meter una progressbar
#? historial de ultimos path colocados (ultimos 5 pares)
#? una forma de poder filtrar que archivos quiero o no incluir

def ejecuto_el_script(origen,destino): #* esto tambien debo de modificar para cada sistema operativo
    ejecutando=sb.Popen(["powershell.exe","-ExecutionPolicy","Bypass","-File","D:\\proyectos\\repositorio_remoto\\localnetbook\\Gui\\proyectos_propios\\copiar_pegar_imagenes.ps1","-lugar_origen",origen,"-lugar_destino",destino],shell=True)#*esto es como escribir en la consola la ejecución



ventana1=VentanaPrincipal()


C_pathError=tk.StringVar(value="")
C_origen=tk.StringVar(value="")
C_destino=tk.StringVar(value="")
C_inclusion=tk.StringVar(value="")
C_entryExtension=tk.BooleanVar()
C_notextension=tk.BooleanVar()
C_extensiones_incluidas=list()
c_extensiones_a_incluir=list()
#*contenedor para el contenido principal
# seccion_paths=tk.Frame(ventana1,width=450,height=200,bg="ligthgrey")
# seccion_paths.place(relx=0.25,rely=0.25)
seccion_paths=FramePaths(ventana1)
seccion_paths.place(seccion_paths.get_configuracion)

#*los label con los titulo para las cajas
# titulo_origen=tk.Label(seccion_paths,text="Ingrese la direccion completa del directorio origen",bg="lightgrey",font=("Arial","12"))
# titulo_destino=tk.Label(seccion_paths,text="Ingrese la direccion completa del directorio destino",bg="lightgrey",font=("Arial","12"))
titulo_origen=LabelsPaths(seccion="ruta origen",contenedor=seccion_paths,posrely=0.20)
titulo_destino=LabelsPaths(seccion="ruta destino",contenedor=seccion_paths,posrely=0.45)
titulo_origen.place(titulo_origen.get_configuracion)
titulo_destino.place(titulo_destino.get_configuracion)

#*label de notificacion
notificacion=tk.Label(seccion_paths,textvariable=C_notificacion,bg="lightgrey")
notificacion.place(relx=0.45)

#*label del error de regex
tituloErrorrEgex=tk.Label(seccion_paths,textvariable=C_pathError,bg="lightgrey")
tituloErrorrEgex.place(rely=0.10)


def crear_seccion_extensiones():
    
    if  C_notextension.get() == True:
        toplavel_extension = tk.Toplevel(ventana1);
        toplavel_extension.geometry("700x500");
        toplavel_extension.title("Seccion Extension");
        toplavel_extension.resizable(False,False);
        extensiones_incluidas= tk.Listbox(toplavel_extension,listvariable=C_extensiones_incluidas,justify="center");
        extensiones_incluidas.insert("end","hola")
        extensiones_incluidas.insert("end","Papu")
        extensiones_incluidas.insert("end","sasu")
        extensiones_a_incluir=tk.Listbox(toplavel_extension,listvariable=c_extensiones_a_incluir,justify="center",);
        extensiones_a_incluir.insert("end",'Chau')
        extensiones_a_incluir.place(relx=0.66,rely=0.50,relwidth=0.40)
        extensiones_incluidas.place(relx=0.33,rely=0.50,relwidth=0.40)
        extensiones_a_incluir
        #*seguir por el camino de arriba

#*CheckButton
crear_seccion_extensiones=tk.Checkbutton(ventana1,text="Extensiones a incluir",variable=C_notextension,command=crear_seccion_extensiones);
crear_seccion_extensiones.pack();

def sacar_error(event):
    C_pathError.set("");
    tituloErrorrEgex.config(bg="lightgrey");

#*funcion para encontrar el espacio prohibido en destino
def corrigiendo_destino(*args):
    patron_correccion=regex.compile(r"\s+")
    string_Pura=str(C_destino.get());
    correccion_completada=regex.search(patron_correccion,string_Pura)
    if correccion_completada != None:
        C_pathError.set("los espacios estan prohibidos");
        tituloErrorrEgex.config(bg="red")
    else:
        C_pathError.set("")
        tituloErrorrEgex.config(bg="lightgrey")

#*funcion para encontrar el espacio prohibido en origen
def corrigiendo_origen(*args):
    patron_correccion=regex.compile(r"\s+") #!rechequear
    string_Pura=str(C_origen.get());
    correccion_completada=regex.search(patron_correccion,string_Pura)
    if correccion_completada == None:
        C_pathError.set("La direccion es valida")
        tituloErrorrEgex.config(bg="green")
    else:
        C_pathError.set("los espacios estan prohibidos");
        tituloErrorrEgex.config(bg="red")

#def corrigiendo(*args):
    


#*funcion main
def iniciar_proceso(event):
    #*parte core
    comprobacion_origen=C_origen.get()!=""
    comprobacion_destino=C_destino.get()!=""
    if (comprobacion_destino and comprobacion_origen) == True:
        C_notificacion.set("Gracias por confiar <3")
        notificacion.config(bg="green")
        ejecuto_el_script(C_origen.get(),C_destino.get());
    elif comprobacion_destino == False and comprobacion_origen == False:
        C_notificacion.set("* Ambos casilleros estan vacios por favor rellenelos")
        notificacion.config(bg="red")
    elif (comprobacion_destino == True or comprobacion_origen == False) or (comprobacion_destino == False or comprobacion_origen == True):
        C_notificacion.set("* Rellene el casillero faltante por favor")
        notificacion.config(bg="yellow")


#*cajas de texto
direccion_origen=tk.Entry(seccion_paths,width=100,textvariable=C_origen)
direccion_destino=tk.Entry(seccion_paths,width=100,textvariable=C_destino)
#inclusion_extensiones=tk.Entry(ventana1,width=50,textvariable=C_inclusion)
direccion_origen.place(rely=0.35)
direccion_destino.place(rely=0.60)
#inclusion_extensiones.place(relx=0.60)


#*eventos de las cajas
for widget in (direccion_destino,direccion_origen):
    widget.bind("<Return>",iniciar_proceso)
    widget.bind("<FocusOut>",sacar_error)



#for item_analizado in (C_origen,C_destino):
#    item_analizado.trace_add("write",corrigiendo)
#*seguimiento de las cajas
C_origen.trace_add("write",corrigiendo_origen)
C_destino.trace_add("write",corrigiendo_destino)

ventana1.mainloop()