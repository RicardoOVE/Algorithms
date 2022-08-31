from Pila import Pila
from Nodo import Nodo

nodo1 = Nodo('item#1')
nodo2 = Nodo('item#2')
nodo3 = Nodo('item#3')
nodo4 = Nodo('item#4')

pila = Pila()

pila.push(nodo1)
pila.push(nodo2)
pila.push(nodo3)
pila.push(nodo4)
pila.imprimePila()
print('-o'*15)

#pila.pop()
#pila.pop()
#pila.imprimePila()
#print('-o'*15)
