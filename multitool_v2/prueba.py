# import shelve
# archivo="./extenciones.dat"
# a=[{"verdad":"si"},{"verdad":"no"},{"verdad":"quizas"}]
# shelf=shelve.open(archivo,writeback=True,protocol=2);
# shelf
#* saber todas las fuentes que se tiene en el sistema 
# import tkinter as tk
# from tkinter import font
# a=tk.Tk()
# a.withdraw()

# b=font.families()

# for i in sorted(b):
#     print(i)
# a.destroy()
#* sacar info de la configuracion actual de la pantalla
# for m in screeninfo.get_monitors():
# #     print()
# import tkinter.font
# from ui.views.main_windows import VentanaPrincipal
# import tkinter

# aa=VentanaPrincipal()
# aa.config(background="#000000")
# label=tkinter.Label(master=aa,font=("Cascadia",20),background="#ffffff",text="hola huevones")
# label.place(relx=0.5,rely=0.5)
# b=tkinter.font.families()
# for i in sorted(b):
#     print(i)
# aa.after(ms=10000,func=lambda n:print("hola"))
# aa.mainloop()


# sistema=platform.system()
# a=platform.version()
# if sistema == "Windows":
#     print("estamos en windows")
#     print(sistema)
#     print(a)
# print("hola")
# from configparser import ConfigParser
# class asad():
#     HOLA="D:\\proyectos\\proyectX\\multitool_v2\\config\\config.ini"
#     a=ConfigParser()
#     a.read(filenames=HOLA,encoding="UTF-8")
#     @classmethod
#     def save(cls):
#         with open(file=cls.HOLA,mode="w",encoding="UTF-8") as config_file:
#             cls.a.write(config_file)
#             print("guarde cambios")
    
#     @classmethod
#     def prueba(cls):
#         t= cls.a
#         # t["hola"]={
#         #     "p":1,
#         #     "p2":2
#         # }
#         # cls.save()
#         if t.has_section("hola"):
#             print("sigue abierto")
    
# asad.prueba()
# from PIL import ImageTk, ImageColor,Image
# from tkinter import Tk,Label
# from tkinter.ttk import Labelframe 
# b=Labelframe()
# png="D:\\proyectos\\proyectX\\multitool_v2\\ui\\assets\\image\\imagenPrueba.jpg"
# ventana_principal=Tk()
# # ventana_principal.geometry("1920x1080")
# imagen=ImageTk.PhotoImage(Image.open(png).resize((320,200)))

# label= Label(text="hola men ",image=imagen,compound="center",justify="center")
# label.grid()
# label.config()
# ventana_principal.mainloop()

from subprocess import Popen,PIPE

a=Popen(["Powershell.exe","Get-ChildItem","-Path","D:\\proyectos\\proyectX\\multitool_v2\\ui\\assets\\image"],stdout=PIPE)
for i in a.stdout:
    print(i)
