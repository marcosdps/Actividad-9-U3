from claseAuto import Auto

class Nuevo(Auto):
    __marca = "Nissan"
    __version : str


    def __init__(self, modelo=None, cantPuertas=None, color=None, precioBase=None, version=None, marca="Nissan"):
        super().__init__(modelo, cantPuertas, color, precioBase)
        self.__marca = marca
        self.__version = version

    def __str__(self) -> str:
        return f"{super().__str__()} {self.__marca} {self.__version}"
    
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                        modelo=self._Auto__modelo,  
                        cantPuertas =self._Auto__cantPuertas,
                        color =self._Auto__color,
                        precioBase =self._Auto__precioBase,
                        marca=self.__marca,
                        version=self.__version
            )
        )
        return d
    
    def importe(self):
        importe = self.__precioBase + (self.__precioBase*0.1)
        if self.__modelo == "full":
            importe += self.__precioBase*0.02
        return importe