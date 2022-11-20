from Nodo import Nodo
class ListaEncadenada:
    def __init__(self):
        self.head = None

    def insertaNodo(self, nuevoNodo):
        if self.head == None: 
            self.head = nuevoNodo
        else:
            aux = self.head 
            while aux.next != None:
                aux = aux.next
            aux.next = nuevoNodo

    def imprimeLista(self):
        aux = self.head
        while aux != None:
            print(aux.nombre)
            aux = aux.next

    def eliminaNodo(self, id): 
        if self.head == None:
            print("Lista vacía")
        else:
            aux = self.head
            if aux.id == id:
                self.head = aux.next
                aux.next = None 
            else:
                prevAux = aux 
                while aux.next != None:
                    prevAux = aux
                    aux = aux.next
                    if aux.id == id:
                        prevAux.next = aux.next
                        aux.next = None