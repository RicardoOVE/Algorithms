/**
 * SUMA LOS NUMEROS IMPARES DE FIBONACCI
 * Crea una función que reciba un número máximo y sumamos todos los números 
 * impares de fibonacci siempre qu sean menores al número recibido
 * 
 * 0 1 1 2 3 5 8 13 21 34 55
 * 
 * function sumaImparesFibo(numero)
 */


function fibonacci(n){
    if(n < 2){
        return n;
    } else  {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}

function fibonacciTotal(c){
    let sum = 0;
    for (let n = 0; n < c; n++){
        if(fibonacci(n) %2 != 0){
            sum += fibonacci(n);
        }
    }
    console.log(sum)
}
// 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
// 5 -> 5
// 6 -> 10
// fibonacciTotal(6)

function sumaImparesFibo(numero){
    let numero_anterior = 0;
    let numero_actual = 1;
    let suma = 0;

    while (numero_actual <= numero){
        if(numero_actual %2 !== 0){
            suma += numero_actual;
        }
        temporal = numero_actual;
        numero_actual += numero_anterior;
        numero_anterior = temporal;
    }
    return suma;
}

console.log(sumaImparesFibo(5));

/**
 * MAXIMO COMUN DIVISOR
 * Crea una función que reciba dos números y regrese el máximo
 * común divisor
 * Ej: 10, 5 -> 5 es el máximo común divisor
 * 5, 2 -> 1
 * 
 * EUCLIDES
 * MCD a y b = b y RESTANTE
 * a % b = RESTANTE
 */

function maximo_comun_divisor(n1, n2){
    let residuo = n1 % n2;
    if (residuo === 0){
        return n2
    } else {
        while(residuo !== 0){
            residuo = n1 % n2;
            n1 = n2;
            n2 = residuo;
        }
        return n1;
    }
}

