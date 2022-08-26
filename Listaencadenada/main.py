from Nodo import Nodo
from ListaEncadenada import ListaEncadenada

listaPersonas = ListaEncadenada()

persona1 = Nodo("Juana", 1)
persona2 = Nodo("Elena", 2)
persona3 = Nodo("Pedro", 3)
persona4 = Nodo("Pablo", 4)

listaPersonas.insertaNodo(persona1)
listaPersonas.insertaNodo(persona2)
listaPersonas.insertaNodo(persona3)
listaPersonas.insertaNodo(persona4)

listaPersonas.imprimeLista()
listaPersonas.eliminaNodo(1)
print("-o-"*20)
listaPersonas.imprimeLista()