from claseAuto import Auto
from datetime import datetime

class Usado(Auto):
    __patente: str
    __ano: int
    __kilometraje: float

    def __init__(self, modelo=None, cantPuertas=None, color=None, precioBase=None, patente=None, ano=None, kilometraje=None):
        super().__init__(modelo, cantPuertas, color, precioBase)
        self.__patente = patente
        self.__ano = ano
        self.__kilometraje = kilometraje

    def __str__(self) -> str:
        return f"{super().__str__()} {self.__patente} {self.__ano} {self.__kilometraje}"

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                            modelo=self._Auto__modelo,  
                            cantPuertas =self._Auto__cantPuertas,
                            color =self._Auto__color,
                            precioBase =self._Auto__precioBase,
                            patente=self.__patente,
                            ano=self.__ano,
                            kilometraje=self.__kilometraje
            )
        )
        return d

    
    def getPatente(self):
        return self.__patente
    
    def modificarPrecio(self):
        self.__precioBase = float(input("Ingrese nuevo precio base: "))
        self.importe()
        
    def importe(self):
        importe = self.__precioBase-(self.__precioBase*(0.01*(datetime.now().year - self.__ano)))
        if self.__kilometraje > 100000:
            importe -= self.__precioBase*0.02
        return importe
       