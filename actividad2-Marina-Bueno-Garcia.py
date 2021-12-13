"""
NOMBRE      : MARINA BUENO GARCÍA
CORREO      : marinbue@ucm.es
EJERCICIO   : 2.4
CLASE       : ALCP1
DESCRIPCIÓN : Se tienen inicialmente 100 cajas (colocadas en círculo) con una bola en cada una. 
En cada turno, se extraen todas las bolas de una caja y se las coloca, una a una, en las siguientes 
cajas avanzando en sentido horario. El siguiente turno comienza en la caja donde se colocó la última bola
del paso anterior. ¿En qué turno se repite la configuración inicial por primera vez?
"""

"""Función que devuelve True si la lista a está llena de unos y False si encuentra un número distinto de 1"""

def inicial_conf(a):
    i = 0
    while i < len(a):
        if (a[i] != 1):
            return (False)
        i += 1
    return (True)

"""Incicializamos las variables """
n = 1000;            # número de cajas
initial_box = 0     # caja donde se colocó la ultima bola
i = 0               # índice de la lista
turno = 1           # turnos
a = [1]*n           # lista con n unos

""" Mientras que no volvamos a tener la configuración inicial, con excepción del primer turno,
vamos repartiendo las bolas una a una hasta que se reparten todas (la caja se queda vacía). 
Cuando esto ocurre pasamos al siguiente turno que comienza en la última caja donde se colocó una bola"""

while(not inicial_conf(a) or turno == 1):
    if a[initial_box]:
        i += 1
        i = i % n
        a[i] += 1
        a[initial_box] -= 1
    else:
        turno += 1
        initial_box = i
print("La configuración inicial se repite en el", turno,"º turno")

