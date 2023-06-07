

class Auto:
    __modelo: str
    __cantPuertas: int
    __color: str
    __precioBase: float

    def __init__(self, modelo=None, cantPuertas=None, color=None, precioBase=None):
        self.__modelo = modelo
        self.__cantPuertas = cantPuertas
        self.__color = color
        self.__precioBase = float(precioBase)

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                            modelo=self.__modelo,
                            cantPuertas=self.__cantPuertas,
                            color=self.__color,
                            precioBase=self.__precioBase
            )
        )
        return d

    def __str__(self) -> str:
        return f"{self.__modelo} {self.__cantPuertas} {self.__color} {self.__precioBase}"

    def getPrecioBase(self):
        return self.__precioBase