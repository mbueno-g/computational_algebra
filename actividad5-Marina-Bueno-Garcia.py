"""
NOMBRE      : MARINA BUENO GARCÍA
CORREO      : marinbue@ucm.es
EJERCICIO   : 6.6
CLASE       : ALCP1
DESCRIPCIÓN : Un entero N >= 2 se  dice pseudoprimo de Fermat en base a, 
para a ∈ Z coprimo con N, si a^(N−1) ≡ 1 (mod N). Se dice que N es pseudoprimo 
de Fermat fuerte si es pseudoprimo en cualquier base a coprimo con N. 
El teorema de Euler-Fermat muestra que todo primo es pseudoprimo de Fermat fuerte, 
pero lamentablemente la recíproca no es cierta. Los números compuestos N ≥ 2
que son pseudoprimos de Fermat fuertes se llaman números de Carmichael. 
Escribir un programa en Python3 que determine los 10 primeros números de Carmichael
"""

import time; 

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


def es_primo (x): # x >= 0
    if x < 2:
        return False
    else :
        raiz = raiz_cuadrada(x)
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

def multiplicar_mod(a, b, N): # 0 <= a,b < N, N >= 1
    c = a * b
    c %= N
    return c

def potencia_mod(a, k, N): # 0 <= a < N, k >= 0 , N >= 2
    if k == 0: # caso base (k = 0)
        r = 1 # convencion : 0^0 = 1
    elif k % 2 == 0: # k es par (k > 0)
        r = potencia_mod (a , k //2 , N )
        r = multiplicar_mod (r , r , N )
    else : # k es impar (k > 0)
        r = potencia_mod (a , k -1 , N )
        r = multiplicar_mod (a , r , N )
    return r

#Función que verifica si un número N es pseudoprimo para
# cualquier base a coprimo con N 
def pseudoprimo_fermat_fuerte(N):
    a = 2;
    while (a <= N):
        if (gcd_binario(a,N) == 1 and potencia_mod(a, N-1, N) != 1):
            return False
        a += 1
    return True

# Buscamos números compuestos (no primos) que sean 
# pseudoprimos de Fermat fuertes = números de Carmichael
def first_ten_carmichael():
    carmichael = []
    N = 2
    while (1): # bucle infinito que termina cuando hemos encontrado los 10 primeros números de Carmichael 
        if (not es_primo(N) and pseudoprimo_fermat_fuerte(N)):
            carmichael.append(N);
            if (len(carmichael) == 10):
                return carmichael
        if (N==2):
            N += 1
        else:
            N += 2

#inicio = time.time()
print("Los primeros 10 números de Carmichael son: ", first_ten_carmichael());
#fin = time.time()
#tiempo = fin-inicio
#print(tiempo)