
import shelve

dat="./extenciones.dat"
contenedor_extensiones="./archivos_predeterminado.txt"
with open(contenedor_extensiones,"r",encoding="utf-8") as archivo_abierto:
    print(archivo_abierto.readlines()); 
