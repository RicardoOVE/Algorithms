"""
Escribir una función la cual reciba una palabra y nos regrese True o False si la palabra es o no palíndromo
Ejemplos de palíndromos: oso, salas, seres, radar
"""

def palindromo(word):
    drow = []
    for letter in word:
        drow.insert(0,letter)
    if word == ''.join(drow):
        return True
    else:
        return False

print(f"Palabra: oso Resultado: {palindromo('oso')}")
print(f"Palabra: casa Resultado: {palindromo('casa')}")
