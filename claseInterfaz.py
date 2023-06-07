from zope.interface import Interface


class Iauto(Interface):
    def insertarAuto(self, posicion, auto):
        pass
    def agregarAuto(self, auto):
        pass
    def mostrarAuto(self, posicion):
        pass
