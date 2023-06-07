from claseNodo import Nodo
from claseAutoNuevo import Nuevo
from claseAutoUsado import Usado
from claseInterfaz import Iauto
from zope.interface import implementer
from datetime import datetime

@implementer(Iauto)
class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0
    
    def toJSON(self):
        diccionario = {}
        nodo = self.__comienzo
        i = 0
        for nodo in self:
            diccionario[i] = nodo.toJSON()
            if nodo.getSiguiente() is not None:
                diccionario[i]['siguiente'] = id(nodo.getSiguiente())
            else:
                diccionario[i]['siguiente'] = None
            i +=1
        return diccionario

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else: 
            self.__indice +=1
            nodoActual = self.__actual
            self.__actual = self.__actual.getSiguiente()
            return nodoActual
        
    def getTope(self):
        return self.__tope

    #implementado por interface
    def agregarAuto(self, auto):
        nodo = Nodo(auto)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        if self.__tope == None:
            self.__tope = 0
        self.__tope +=1

    def agregarAutoFinal(self, auto):
        if self.__comienzo == None:
            print("LISTA VACIA, SE COLOCARÁ AL PRINCIPIO DE LA MISMA")
            self. agregarAuto(auto)
        else:
            nodoAguardar = Nodo(auto)
            for nodo in self:
                if nodo.getSiguiente() == None:
                    nodoAguardar.setSiguiente(nodo.getSiguiente())
                    nodo.setSiguiente(nodoAguardar)
            self.__tope +=1

    #implementado por interface 
    def insertarAuto(self, posicion, auto):
        if posicion <= self.__tope:
            nodoAguardar = Nodo(auto)
            backUpTope = self.__tope
            self.__tope = posicion-1
            for nodo in self:
                if self.__indice == self.__tope :
                    nodoAguardar.setSiguiente(nodo.getSiguiente())
                    nodo.setSiguiente(nodoAguardar)
            self.__tope = backUpTope +1
        else: print("IMPOSIBLE INGRESAR EN UN AUTO")

    #implementado por interface 
    def mostrarAuto(self, posicion):
        if posicion <= self.__tope:
            backUpTope = self.__tope
            self.__tope = posicion
            for nodo in self:
                if self.__tope == posicion:
                    print(nodo.getDato())
            self.__tope = backUpTope


    def listarDatosAutos(self):
        for nodo in self:
            print(nodo.getDato())

    def añadirNuevoAuto(self, tipoAuto, agregar):
        print("Ingreso de datos")
        modelo = input("Modelo: ")
        cantPuertas = int(input("Cantidad de puertas: "))
        color = input("Color: ")
        precioBase = float(input("Precio base: "))
        if tipoAuto == 1:
            version = input("Version: ")
            unAuto = Nuevo(modelo, cantPuertas, color, precioBase, version)
        elif tipoAuto == 2:
            patente = input("Patente: ")
            ano = int(input("Año: "))
            kilometraje = float(input("Kilometraje: "))
            unAuto = Usado(modelo, cantPuertas, color, precioBase, patente, ano, kilometraje)
        if agregar == "principio":
            Iauto(self).agregarAuto(unAuto)
        elif agregar == "final":
            self.agregarAutoFinal(unAuto)
        elif agregar == "posicion":
            posicion = int(input("Ingrese la posicion que desea agregar un auto: "))
            Iauto(self).insertarAuto(unAuto, posicion)
            
    def mostrarAutoDePosicionDeseada(self,posicion):
        backUpTope = self.__tope
        self.__tope = posicion
        for nodo in self:
            if self.__indice == self.__tope:
                print(type(nodo.getDato()))
        self.__tope = backUpTope

    def modificarPrecioBase(self, patente):
        i=0
        for nodo in self:
            auto = nodo.getDato()
            if isinstance(auto, Usado):
                auto.modificarPrecio()
                return
            
    def buscarAutoMasEconomico(self):
        elMasBarato = 100000000
        for nodo in self:
            auto=nodo.getDato()
            if auto.getPrecioBase() < elMasBarato:
                elMasBarato = auto.getPrecioBase()
                indice = self.__indice
        print(f"el mas barato está en posicion {indice}")
        backUpTope = self.__tope
        self.__tope = indice
        for nodo in self:
            if self.__indice == self.__tope:
                autoMasEconomico = nodo.getDato()
                print(autoMasEconomico)
                print(autoMasEconomico.importe())
        self.__tope = backUpTope

        