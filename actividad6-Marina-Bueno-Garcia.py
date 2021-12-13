"""
NOMBRE      : MARINA BUENO GARCÍA
CORREO      : marinbue@ucm.es
EJERCICIO   : 7.10
CLASE       : ALCP1
DESCRIPCIÓN : Utilizar el método p − 1 de Pollard para factorizar
N = 1542201487980564464479858919567403438179217763219681634914787749213
utilizando B = 100. ¿Cómo se puede calcular gcd((a^β) − 1, N) de forma eficiente?
"""

import random
import math
from math import ceil

def gcd_binario (x , y ): # (x,y) != (0 ,0)
    x = abs( x )
    y = abs( y )
    xespar = x %2 == 0
    yespar = y %2 == 0
    if x == 0: # caso base : gcd (0,y)=y
        m = y
    elif y == 0: # caso base : gcd(x,0)= x
        m = x
    elif xespar and yespar :
        m = 2 * gcd_binario ( x //2 , y //2)
    elif xespar :
        m = gcd_binario ( x //2 , y )
    elif yespar :
        m = gcd_binario (x , y //2)
    elif x > y :
        m = gcd_binario (y , x - y )
    else :
        m = gcd_binario (x , y - x )
    return m

def es_primo ( x ): # x >= 0
    if x < 2:
        return False
    else :
        raiz = raiz_cuadrada( x )
        y = 2
        while y <= raiz :
            if x % y == 0:
                return False
            y += 1
    return True

def raiz_cuadrada(x): # x >= 0
    izq = 0
    der = x +1
    while izq < der -1: # buscamos en [izq ,der)
        med = ( izq + der )//2
        if med * med <= x :
            izq = med
        else :
            der = med
    return izq

def pollard(N,B):
    a = random.randint(1,N-1) #devuelve una muestra de la distribución uniforme discreta en [1,N-1]
    if (gcd_binario(a, N) != 1):
        x = gcd_binario(a,N)
        print("N = ", x, "*", N//x)
    else:
        beta = 1
        p = 2
        while (p <= B): #calculamos beta
            if (es_primo(p)):
                beta *= p**ceil(math.log(N,p))
            p += 1
        g = gcd_binario(pow(a,beta,N)-1, N) # calculamos mcd modulo N
        if (g > 1 and g < N):
            print("N = ", g, "*", N//g)
        else:
            pollard(N,B) # si g<=1 o g>= N vuelve a llamar a la función

pollard(1542201487980564464479858919567403438179217763219681634914787749213,100)