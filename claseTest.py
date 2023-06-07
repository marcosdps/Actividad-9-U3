from claseLista import Lista
from claseAuto import Auto
from claseAutoNuevo import Nuevo
from claseAutoUsado import Usado
import unittest
import os

class TestListaAutos(unittest.TestCase):
    def setUp(self):
        self.__lista = Lista()
        self.__autoNuevo1 = Nuevo("ModeloNuevo1",5,"ColorNuevo1",150000, "VersionNuevo1")
        self.__lista.agregarAuto(self.__autoNuevo1)
        self.__autoUsado1 = Usado("ModeloUsado1", 5, "ColorUsado1", 100000, "PatenteUsada1", 2015, 21231)
        self.__lista.agregarAuto(self.__autoUsado1)
        self.__autoNuevo2 = Nuevo("ModeloNuevo2",5,"ColorNuevo2",150000, "VersionNuevo2")
        self.__lista.agregarAuto(self.__autoNuevo2)
        self.__autoUsado2 = Usado("ModeloUsado2", 5, "ColorUsado2", 350000, "PatenteUsada2", 2022, 11231)
        self.__lista.agregarAuto(self.__autoUsado2)
        
    def test_agregarAuto(self):
        print("\n\n-------> Probando metodo agregarAuto")
        tipoAuto = int(input("Auto nuevo(1) o Auto Usado(2)?: "))
        autoTest = self.__lista.añadirNuevoAuto(tipoAuto, "principio")
        self.__lista.agregarAuto(autoTest)
        self.__lista.listarDatosAutos()
        print("Funcionamiento correcto------> OK")
        
    def test_insertarAuto(self):
        print("\n\n-------> Probando metodo insertarAuto")
        unAutoInsertado = Nuevo("insertado",2,"ColorInsertado",25000,"VersionInsertadaDeElla")
        posicion = int(input("Posicion: "))
        self.__lista.insertarAuto(posicion,unAutoInsertado)
        self.__lista.listarDatosAutos()


