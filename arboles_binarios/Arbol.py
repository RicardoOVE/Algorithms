from Nodo import Nodo

class Arbol:

    def __init__(self):
        self.root = Nodo("")

    def insertaPalabra(self, palabra):
        nodoActual = self.root

        for letra in palabra:
            if letra in nodoActual.hijos:
                nodoActual = nodoActual.hijos[letra]
            else:
                nuevoNodo = Nodo(letra)
                nodoActual.hijos[letra] = nuevoNodo
                nodoActual = nuevoNodo
        
        nodoActual.palabra_completa = True