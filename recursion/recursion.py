#Clase recursión

def hello(cantidad):
    if cantidad > 0:
        print('Hello!')
        return hello(cantidad-1)

#hello(2)

#RETO #1 Función de cuenta regresiva la cual reciba un número e imprima los númers desde el que recibe hasta el 0.
#Ej. recibo 10,
#Imprimir:
#10 #9 #8 #7 #6 #5 #4 #3 #2 #1 #0

def cuenta_regresiva(numero):
    if numero >= 0:
        print(numero)
        cuenta_regresiva(numero-1)

#cuenta_regresiva(5)

#SIGMA - Recibe un número y va sumando todos los números anteriores
#sigma(5): 5 + 4 + 3 + 2 + 1 = 15

def sigma(num):
    if num == 1:
        return 1
    else:
        return num + sigma(num-1)

#print(sigma(5))

#RETO GRUPAL: Función factorial recursiva. Crear una función que reciba un número y regrese el número factorial
#factorial(4) -> 4 * 3 * 2 * 1 

def factorial(numero):
    if numero == 1:
        return 1
    return numero * factorial(numero-1)

print(factorial(4))

