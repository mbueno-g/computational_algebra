"""
NOMBRE      : MARINA BUENO GARCÍA
CORREO      : marinbue@ucm.es
EJERCICIO   : 4.4
CLASE       : ALCP1
DESCRIPCIÓN : Implementar el algoritmo de Strassen para multiplicar matrices
de nxn reduciendo recursivamente a n/2xn/2. Esto requiere añadir filas/columnas
de ceros cuando las matrices no sean potencia de 2. 
Implementar un programa que haga una gráfica de n vs tiempo en segundos para 
distintos valores de n en donde se pueda ver la asintótica de la complejidad
"""

import random as rnd
import matplotlib.pyplot as plt
import time

#Funcion que añade una fila y una columna de ceros
def add_column_row(A,B):
    n = len(A)
    for i in A:
        i.append(0)
    for j in B:
        j.append(0)
    A.append([0]*(n+1))
    B.append([0]*(n+1))
    return A,B

#Función que elinima n filas y columnas
def del_column_row(C,n):
    len_c = len(C)
    for i in C:
        for j in range (0,n):
            i.pop(len_c-j-1)
    for j in range (0,n):
        C.pop(len_c-j-1)
    return C

#Función que divide una matriz A de orden nxn en 4 submatrices
# de orden n/2xn/2
def submatrix(A):
    rows = len(A)
    columns = len(A[0])
    A11,A12,A21,A22 = [],[],[],[]
    A11 = [M[:rows//2] for M in A[:columns//2]]
    A12 = [M[rows//2:] for M in A[:columns//2]]
    A21 = [M[:rows//2] for M in A[columns//2:]]
    A22 = [M[rows//2:] for M in A[columns//2:]]    
    return A11,A12,A21,A22

#Función que convierte 4 matrices n/2xn/2 en una sola matriz nxn
def submatrix_reverse(A11,A12,A21,A22,n):
    C = []
    rows1 = len(A11)
    rows2 = len(A21)
    for i in range(rows1):
        C.append(A11[i]+A12[i])
    for j in range(rows2):
        C.append(A21[j]+A22[j])
    return (C)

#Función que suma/resta matrices
def sum_matrix(A,B,op):
    n = len(A)
    result = []
    for i in range (0,n):
        aux = []
        for j in range(0,n):
            if op == '+':
                s = A[i][j] + B[i][j]
            else:
                s = A[i][j] - B[i][j]
            aux.append(s)
        result.append(aux)
    return result

#Función que devuelve si un número es potencia de 2
def IsPowerOfTwo(x):
    return (x != 0) and ((x & (x - 1)) == 0)

#Algoritmo de Strassen para matrices de tamño nxn
def mult_strassen(A,B):
    n = len(A)
    if (n == 1): #Caso base: matriz 1x1
        C = [[A[0][0]*B[0][0]]]
        return (C)
    else: #Caso general
        potencia2 = IsPowerOfTwo(n)
        i = 0; #contabiliza cuantas filas/columnas de ceros se han añadido
        #Añade filas y columnas de ceros hasta que tenga como orden una potencia de 2
        while (not IsPowerOfTwo(n) and n != 1):
            A,B = add_column_row(A,B)
            n += 1
            i += 1
        A11,A12,A21,A22 = submatrix(A)
        B11,B12,B21,B22 = submatrix(B)
        M1 = mult_strassen(sum_matrix(A11,A22,'+'),sum_matrix(B11,B22,'+'))
        M2 = mult_strassen(sum_matrix(A21,A22,'+'),B11)
        M3 = mult_strassen(A11,sum_matrix(B12,B22,'-'))
        M4 = mult_strassen(A22,sum_matrix(B21,B11,'-'))
        M5 = mult_strassen(sum_matrix(A11,A12,'+'),B22)
        M6 = mult_strassen(sum_matrix(A21,A11,'-'),sum_matrix(B11,B12,'+'))
        M7 = mult_strassen(sum_matrix(A12,A22,'-'),sum_matrix(B21,B22,'+'))
        C11 = sum_matrix(sum_matrix(sum_matrix(M1,M4,'+'),M5,'-'),M7,'+')
        C12 = sum_matrix(M3,M5,'+')
        C21 = sum_matrix(M2,M4,'+')
        C22 = sum_matrix(sum_matrix(sum_matrix(M1,M2,'-'),M3,'+'),M6,'+')
        C = submatrix_reverse(C11,C12,C21,C22,n)
        if not potencia2:
            C = del_column_row(C,i)
        return C



max_nxn_matrix =  30
min_nxn_matrix = 2
step = 1

nxn = [] #ordenes de las matrices
tiempo = []

n = min_nxn_matrix
while n <= max_nxn_matrix:
    matrix1 = []
    matrix2 = []
    for i in range (0,n):
        aux1 = []
        aux2 = []
        for j in range(0,n):
            aux1.append(rnd.randint(0,100))
            aux2.append(rnd.randint(0,100))
        matrix1.append(aux1)
        matrix2.append(aux2)
    ini = time.time()
    C = mult_strassen(matrix1, matrix2)
    fin = time.time()
    t = fin - ini
    tiempo += [t]
    nxn += [n]
    n += step
plt.plot(nxn, tiempo, "b-")
plt.xlabel('Orden matriz nxn')
plt.ylabel('Tiempo (seg)')
plt.show()
