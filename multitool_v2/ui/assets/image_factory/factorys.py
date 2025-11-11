from PIL import Image,ImageColor
#* debo hacer que devuelva las imagenes ya procesadas 
class FactImgNotify():
    PATH_PIC=["D:\\proyectos\\proyectX\\multitool_v2\\ui\\assets\\image\\advertencia.png",
            "D:\\proyectos\\proyectX\\multitool_v2\\ui\\assets\\image\\cancelar.png",
            "D:\\proyectos\\proyectX\\multitool_v2\\ui\\assets\\image\\confirmar.png"]
    @staticmethod
    def create_imgs(imagenes=PATH_PIC) -> dict:
        """aqui generare los objetos imagenes para notificaciones"""
        despacho_imagen=[]
        imagenes_enpaquetadas={"warning":2,"cancel":1,"validate":0}
        for pic in imagenes:
            imagen_lista=(Image.open(pic).resize((150,150)))
            despacho_imagen.append(imagen_lista)
        item=iter(despacho_imagen)
        for clave in imagenes_enpaquetadas.keys():
            imagenes_enpaquetadas[clave]=next(item)
        return imagenes_enpaquetadas
    