from claseAuto import Auto

class Nodo:
    __auto : Auto
    __siguiente: object

    def __init__(self, auto):
        self.__auto = auto
        self.__siguiente = None

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                            auto = self.__auto.toJSON()
            )
        )
        return d
    

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__auto