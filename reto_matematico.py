# Crear una función que recibe como parámetro un string. Este string contiene una 
# fórmula matemática. La función debe de validar que los parentesis, corchetes y llaves
# sean correctos y tengan una estructura y orden válido. Retorna True si la validación 
# es exitosa, False de lo contrario
# ( 1 + 2 ) * ( 6 * 4 ) => True
# ( x + [z-3] * { 4 + 5 * (y - 7)} ) => True
# ( x + z / [ y * z} + 7 ) => False

def validaExpresion(expresion) :
    caracteres = Pila()
    for c in expresion :
        if c == "(" or c == "[" or c == "{":
            nuevoNodo = Node(c)
            caracteres.push(nuevoNodo)
        if c == ")" or c == "]" or c == "}":
            tope = caracteres.top 
            if tope == None:
                return False
            else: 
                if (tope.caracter == "(" and c == ")") or (tope.caracter == "[" and c == "]") or (tope.caracter == "{" and c == "}"):
                    caracteres.pop()
                else :
                    return False

    if caracteres.top == None:
        return True
    else:
        return False



print( validaExpresion( ") 1 + 2 ) * ( 6 * 4 )" ) )