"""
Recibir un número entero y vamos a imprimir la serie fibonacci hasta esta posición
El número recibido es la cantidad de números que debemos imprimir
Serie fibonacci: comenzando en 0 y 1 sumamos vamos sumando los dos últimos números
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
"""
def fibonacci(n):
    a = 0
    b = 1
    if n < 2:
        print(a)
    elif n == 2:
        print("0 \n1")
    else:
        print(0)
        for number in range(n-1):
            new_number = a + b
            b = a
            a = new_number
            print(new_number)


fibonacci(1)
print("-o-"*20)
fibonacci(2)
print("-o-"*20)
fibonacci(5)
print("-o-"*20)

