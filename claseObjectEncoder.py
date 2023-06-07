import json
from claseAuto import Auto
from claseAutoNuevo import Nuevo
from claseAutoUsado import Usado
from claseNodo import Nodo
from claseLista import Lista

class ObjectEncoder:
    def guardarJSONArchivo(self, diccionario):
        with open("autos.json", "w", encoding="UTF-8")as archi:
            json.dump(diccionario, archi, indent=4)
            archi.close

    
    def leerJSONArchivo(self):
        with open("autos.json", "r", encoding="UTF-8") as archi:
            diccionario=json.load(archi)
            archi.close()
        return diccionario
    
    def decodificador(self, diccionario, lista):
        for key in diccionario:
            datos = diccionario[key]["__atributos__"]["auto"]
            atributos = datos["__atributos__"]
            if datos["__class__"]=="Nuevo":
                auto = Nuevo(**atributos)
            else:
                auto=(Usado(**atributos))
            lista.agregarAuto(auto)

    #el key es el numero "0", "1" , "2" que enumera las distintas intancias de clases del archivo
    
        