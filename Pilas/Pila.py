from Nodo import Nodo

class Pila:
    def __init__(self):
        self.top = None

    #Función push que ingrese un nuevo nodo a mi pila
    def push(self, nuevoNodo):
        nuevoNodo.next = self.top
        self.top = nuevoNodo

    #Función imprimePila que te imprima en orden todos los nodos
    def imprimePila(self):
        aux = self.top
        while aux != None:
            print(aux.valor)
            aux = aux.next

    #Función pop que te elimina el elemento que tengo más arriba de mi pila
    def pop(self):
        aux = self.top
        if aux != None:
            self.top = aux.next
            aux.next = None

