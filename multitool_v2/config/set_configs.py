from configparser import ConfigParser
# pensar en hacer una clase opciones con las multiples clases
from subprocess import Popen
from os import path
class Config:
    config_class = ConfigParser()
    FILE_CONFIG = "D:\\proyectos\\multitool\\multitool_V2\\config_opened\\config_opened.ini"
    if path.exists(FILE_CONFIG):
        config_class.read(filenames=FILE_CONFIG, encoding="UTF-8")
    else:
        pass #* ejecutar un script que copie archivos de respaldo encriptado de  una carpeta a definir 
    @classmethod
    def save_change_config(cls):
        with open(cls.FILE_CONFIG, "w", encoding="UTF-8") as configfile:
            cls.config_class.write(configfile)
            

    @classmethod
    def detectar_resoluciones(cls):
        from win32api import EnumDisplaySettings
        cont = 1
        modes = []
        config_opened= cls.config_class
        while True:
            try:
                parametro = EnumDisplaySettings(None, cont)
                modes.append([parametro.PelsWidth, parametro.PelsHeight])
            except IndexError:
                break
            cont += 1
        opciones = set((w, h) for w, h in modes)
        if config_opened.has_section("Screen"):
            print("existe la seccion")
        else:
            config_opened["Screen"] = {
                "resolution": str(sorted(opciones)),
            }
        cls.save_change_config()
    
    @classmethod
    def cargar_fuentes(cls):
        from platform import system, version,mac_ver
        from ui.theme.theme_default import FAMILY_FONT_NOTIFICATIONS
        config_opened=cls.config_class
        if not config_opened.has_section("OS"):
            match system():
                case "Linux":
                    from distro import name, version
                    linux_name = name()
                    linux_version = version()
                    config_opened["OS"] = {
                        "Name": linux_name,
                        "Version": linux_version
                    }
                case "Windows":
                    win_name = "Windows" 
                    win_version = version()
                    config_opened["OS"] = {
                        "Name": win_name,
                        "Version": win_version}
                case "Darwin": #* nombre del kernel de Macos
                    macos_name= "Darwin" 
                    macos_version=mac_ver()[0]
                    config_opened["OS"]={
                        "Name":macos_name,
                        "Version":macos_version
                    }
            cls.save_change_config()
        match config_opened.get(section="OS",option="Version"):
            case "Windows":
                import ctypes
                FONT_PRIVATE = 0x10  # * indica que la font se cargue para el proceso actual
                FONT_NOT_ENLIST = 0x20  # * que no aparezca en la lista global de fuentes
                gdi32 = ctypes.WinDLL(
                    "gdi32", use_last_error=True
                )  # *gdi32 es el motor grafico de windows
                resultado = gdi32.AddFontResourceExW(
                    FAMILY_FONT_NOTIFICATIONS, FONT_PRIVATE | FONT_NOT_ENLIST, 0
                )
                if resultado > 0:  # * es mayor a 0 si cargo el font
                    print("cargo correctamente")
            case "Linux":                
                pass
            case "MacOs":
                pass
