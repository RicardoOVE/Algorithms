from Nodo import Nodo
class ListaEncadenada:
    def __init__(self):
        self.head = None #Porque cuando declaro por primera vez mi lista AÚN no tiene ningún nodo, la inicializamos vacía

    def insertaNodo(self, nuevoNodo):
        if self.head == None: #Mi lista está vacía
            self.head = nuevoNodo #El primer elemento lista es el nodo recibo
        else:
            aux = self.head #el primer nodo a comparar es el head (o el primero de mi lista)
            while aux.next != None: #Siempre y cuando el next de mi nodo NO sea None
                aux = aux.next #aux ahora es el siguiente nodo
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