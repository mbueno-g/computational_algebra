"""
NOMBRE      : MARINA BUENO GARCÍA
CORREO      : marinbue@ucm.es
EJERCICIO   : 3.4
CLASE       : ALCP1
DESCRIPCIÓN : Considerar el siguiente juego de dos jugadores: partiendo de un pila de n piedras, los jugadores van (uno tras otro) quitando 1,2 o 6 piedras de la pila a su elección, hasta que el que quita la última pierde. Implementar un algoritmo recursivo es_posible_ganar_con_n_piedras(n) que determine si, partiendo de una pila de n piedras, hay estrategia ganadora.
"""

#Diccionario donde se guarda si hay estrategia ganadora para n piedras
result = {}

""" 
Variables:
    - win: variable que indica si yo gano
    - lose: variable que indica si el contrincante gana
Caso base: si recibo una piedra yo gano
Caso general: comprobamos todos las combinaciones posible cogiendo 1, 2 y 6 piedras mientras que gane el contrincante (lose=True). En el momento en el que el contrincante pierda (lose=False), hemos encontrado una estrategia ganadora.  
"""
def es_posible_ganar_con_n_piedras(n):
    if n in result.keys():
        return result[n]
    else:
        if n == 0:
            win = True
        else:
            lose = es_posible_ganar_con_n_piedras(n-1)
            if lose and n-2 >= 0:
                lose = es_posible_ganar_con_n_piedras(n-2)
                if lose and n-6 >= 0:
                    lose = es_posible_ganar_con_n_piedras(n-6)
            win = not(lose)
        result[n] = win
        return win

if __name__=="__main__":
    for i in range(1,10**6):
        es_posible_ganar_con_n_piedras(i)
    print("¿Es posible ganar con 10**6 piedras?", es_posible_ganar_con_n_piedras(10**6))


