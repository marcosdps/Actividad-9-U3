from claseAuto import Auto
from claseAutoNuevo import Nuevo
from claseAutoUsado import Usado
from claseLista import Lista
from claseNodo import Nodo
from claseObjectEncoder import ObjectEncoder
from claseInterfaz import Iauto
from claseTest import TestListaAutos
import unittest



if __name__ == "__main__":
    print("--------------PROBANDO!-----------------")
    lista = Lista()
    jsonf = ObjectEncoder()
    interfaz = """\n---------MENU DE OPCIONES---------
    -1- Añadir nuevo Auto al principio de lista
    -2- Añadir nuevo Auto al final de lista
    -3- Añadir un auto en una posicion determinada
    -4- Mostrar tipo de datos de auto de posicion deseada
    -5- Mostrar datos de un auto
    -6- Modificar precio base de un vehiculo
    -7- Buscar Auto mas economico
    -8- Listar datos de autos
    -9- Guardar datos en archivo JSON
    -10- Leer datos del archivo JSON
    -11- Probar funciones con test
    -0- SALIR"""
    print(interfaz)
    opcion = int(input("Ingrese una opcion: "))
    while opcion != 0:
        match opcion:
            case 1:
                tipoAuto = int(input("Auto nuevo(1) o Auto Usado(2)?: "))
                lista.añadirNuevoAuto(tipoAuto, "principio")
            case 2:
                tipoAuto = int(input("Auto nuevo(1) o Auto Usado(2)?: "))
                lista.añadirNuevoAuto(tipoAuto, "final")
            case 3:
                tipoAuto = int(input("Auto nuevo(1) o Auto Usado(2)?: "))
                lista.añadirNuevoAuto(tipoAuto, "posicion")
            case 4:
                posicion = int(input("Ingresar posicion: "))
                lista.mostrarAutoDePosicionDeseada(posicion)
            case 5:
                posicion = int(input("Ingrese la posicion del auto: "))
                Iauto(lista).mostrarAuto(posicion)
            case 6:
                patente = input("Ingrese la patente del vehiculo: ")
                lista.modificarPrecioBase(patente)
            case 7:
                lista.buscarAutoMasEconomico()
            case 8:
                lista.listarDatosAutos()
            case 9:
                d = lista.toJSON()
                jsonf.guardarJSONArchivo(d)
            case 10:
                diccionario = jsonf.leerJSONArchivo()
                print(diccionario)
                jsonf.decodificador(diccionario, lista)
            case 11:
                unittest.main()

        print(interfaz)
        opcion = int(input("Ingrese una opcion: "))