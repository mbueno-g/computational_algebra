'''    
AUTHOR       : MARINA BUENO GARCÍA
EMAIL        : marinbue@ucm.es
EXERCISE     : 1.5
CLASS        : ALCP1
DESCRIPTION  : La constante de Champernowne es el número irracional que se obtiene al concatenar todos los números naturales, del siguiente modo: 0.1234567891011121314151617181920212223... Sea d_n el dígito que ocupa el lugar n-ésimo. Calcular
                                    d_1 · d_10 · d_100 · d_1000 · d_10000 * d_100000 * d_1000000
'''

i = ''          # string con los decimales de la constante de Champernowne
cont_num = 1    # contador de números de 1 al 1000000
cont_digit = 0  # contador de dígitos

while (cont_digit < 1000000):
    i += str(cont_num) 
    cont_digit += len(str(cont_num))
    cont_num += 1;
print("El resultado de multiplicar d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000 es:", int(i[0])*int(i[9])*int(i[99])*int(i[999])*int(i[9999])*int(i[99999])*int(i[999999]))
