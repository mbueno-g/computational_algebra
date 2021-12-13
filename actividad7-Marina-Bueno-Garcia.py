"""
NOMBRE      : MARINA BUENO GARCÍA
CORREO      : marinbue@ucm.es
EJERCICIO   : 8.5
CLASE       : ALCP1
DESCRIPCIÓN : Escribir un programa que genere números de 300 dígitos decimales al azar (dígito a dígito), que aplique
el test de Solovay-Strassen con k = 20 y que se detenga al encontrar un entero que pase el test, es
decir, uno que sea "probablemente primo". ¿Cuántos enteros fueron explorados hasta conseguir el
resultado? ¿Qué pasa si se repite el experimento varias veces?
"""

import math
import random
import matplotlib.pyplot as plot

# Función que calcula el símbolo de jacobi    
def jacobi(a,n):
    result = 1
    while a!= 0:
        while a%2 == 0:
            a//= 2
            if n%8 == 3 or n%8 == 5:
                result = -result
        a , n = n , a
        if a%4 == 3 and n%4 == 3:
            result = -result
        a%=n
    if n == 1:
        return result
    else:
        return 0

# Si alguna de las k pruebas devuelve que N es compuesto entonces N es compuesto
def test_solovay_strassen(N, k):
    if (N % 2 == 0):
        return ("N es compuesto")
    while (k > 0):
        a = random.randint(1,N-1) #devuelve una muestra de la distribución uniforme discreta en [1,N-1]
        gcd = math.gcd(a,N)
        j = jacobi(a,N)
        p = pow(a, (N-1)//2, N)
        if (p == N - 1):
            p = -1
        if (gcd != 1 or j != p):
            return ("N es compuesto")
        k -=1
    return ("N es probablemente primo")

# Función que genera un número de hasta n dígitos (dígito a dígito) (ya que incluimos el 0)
def generar_numero(n):
    N = 0
    while (n > 0):
        a = random.randint(0,9)
        N = 10*N + a
        n -= 1
    return (N)

# Función que encuentra un número de n dígitos que es probablemente primo
def generar_primo(n,k):
    N = generar_numero(n)
    cnt = 0
    while (test_solovay_strassen(N,k) == "N es compuesto"):
        cnt += 1
        N = generar_numero(n) #generamos un nuevo número
    return (N, cnt)

# Función que muestra un histograma de número de intentos necesarios
# para encontrar un primo de 300 dígitos que pasa el test 20 veces
def generar_histograma():
    k = 2000
    result = []
    while (k > 0):
        N, cnt = generar_primo(300,20)
        result.append(cnt)
        k -= 1
    plot.hist(result, 15, color='#F2AB6D', ec="black")
    plot.title('Histograma de cnt - MarinaBuenoGarcía')
    plot.xlabel('Cnt')
    plot.ylabel('Frecuencia')