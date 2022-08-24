/* Recibimos un número y regresamos el factorial de este (return)
1! = 1*1 = 1
2! = 2*1 = 2
3! = 3*2*1 = 6
4! = 4*3*2*1 = 24
 */

function factorial(number){
    var factorial_result = 1;
    if (number == 0){
        return 0
    }
    for (let i=number; i > 1; i--){
        factorial_result *= i
    }
    return factorial_result
}

console.log(factorial(4))