import random as rnd
import numpy as np
import math as math

def quitar_ceros(f):
	c = len(f) - 1
	while (f[c] == 0 and c > 0):
		c -= 1
	return f[0:c+1]

def pol_coef(a, i):
    if i >= len(a):
        return 0
    return a[i]

def pol_sumar(a, b, p):
    return [(pol_coef(a,i)+pol_coef(b,i))%p for i in range(max(len(a),len(b)))]

def pol_restar(a, b, p):
    return [(pol_coef(a,i)-pol_coef(b,i))%p for i in range(max(len(a),len(b)))]
    
def pol_multiplicar_escalar(a, k, p):
    return [(k*pol_coef(a,i))%p for i in range(len(a))]

def pol_multiplicar_escuela(a, b, p):
    c = []
    for i in range(len(b)):
        aux = pol_sumar(c[i:], pol_multiplicar_escalar(a, b[i], p), p)
        c = c[:i] + aux
    return c

def pol_multiplicar_karatsuba(a, b, p):
    n = len(a)
    m = len(b)
    if n < m:
        a, b = b, a
        n, m = m, n
    if m <= 10:
        prod = pol_multiplicar_escuela(a, b, p)
    elif m <= n//2:
        c0 = pol_multiplicar_karatsuba(a[:n//2], b, p)
        c1 = pol_multiplicar_karatsuba(a[n//2:], b, p)
        c1 = pol_sumar(c1, c0[n//2:], p)
        prod = c0[:n//2] + c1
    else:
        c0 = pol_multiplicar_karatsuba(a[:n//2], b[:n//2], p)
        c2 = pol_multiplicar_karatsuba(a[n//2:], b[n//2:], p)
        s1 = pol_sumar(a[:n//2], a[n//2:], p)
        s2 = pol_sumar(b[:n//2], b[n//2:], p)
        c1 = pol_multiplicar_karatsuba(s1, s2, p)
        s3 = pol_sumar(c0, c2, p)
        c1 = pol_restar(c1, s3, p)
        c1 = pol_sumar(c1, c0[n//2:], p)
        c2 = pol_sumar(c2, c1[n//2:], p)
        prod = c0[:n//2] + c1[:n//2] + c2
    return prod 

def pol_multiplicar_escalar(a, k, p):
    return [(k*pol_coef(a,i))%p for i in range(len(a))]

def negaconv(a,b,p):
	n = len(a)
	if len(b) != n:
		print(...)
	c = [0 for i in range(n)]
	for i in range(n):
		signo=1
		for j in range(n):
			c[i]=(c[i]+(signo)*a[j]*b[i-j])%p
			if j== n-1 or i-j==0:
				signo = -1
	return c
	
def shift(fi,i):
	fi_shift = [0 for i in range(len(fi))]
	for j in range(0,len(fi)):
		fi_shift[(j+i)%(len(fi))]=(pow(-1,(j+i)//(len(fi))))*fi[j]
	return fi_shift	

def beta(f_tilde,xi):
	beta_f = [[0 for i in range(len(f_tilde[0]))] for j in range(len(f_tilde))]
	for j in range (len(f_tilde)):
		beta_f[j]=shift(f_tilde[j],xi*j) 
	return beta_f

def beta_i(f_tilde,xi,n2):
	beta_f = [[0 for i in range(len(f_tilde[0]))] for j in range(len(f_tilde))]
	for j in range (len(f_tilde)):
		beta_f[j]=shift(f_tilde[j],xi*((2*n2)-j)) 
	return beta_f

def mult_ss_mod(f,g,k,p):
	if(k <=2):
		w = negaconv(f,g,p)
		return quitar_ceros(w)
	else:
		k1=k//2
		k2=k-k1
		n1=2**k1
		n2=2**k2
		f1 = [[0 for i in range(n1)] for j in range(n2)]
		g1 = [[0 for i in range(n1)] for j in range(n2)]
		f_tilde = [[0 for i in range(2*n1)] for j in range(n2)]
		g_tilde = [[0 for i in range(2*n1)] for j in range(n2)]
		for i in range(n2):
			f1[i]=f[i * n1:((i + 1) * n1)]
			g1[i]=g[i * n1:((i + 1) * n1)]
			f_tilde[i]=f1[i]+[0]*n1
			g_tilde[i]=g1[i]+[0]*n1
		#print(f_tilde)
		beta_f_tilde=beta(f_tilde,(2*n1)//n2)
		beta_g_tilde=beta(g_tilde,(2*n1)//n2)
		#print(beta_f_tilde)
		fft_b_f_tilde = fft(beta_f_tilde, (4*n1)//n2,p)
		fft_b_g_tilde = fft(beta_g_tilde, (4*n1)//n2,p)
		#print(fft_b_f_tilde)
		h=[]
		for i in range(n2):
			h += [mult_ss_mod(fft_b_f_tilde[i],fft_b_g_tilde[i],1+k1,p)]
		#print("h", h)
		h2 = fft(h,((4*n1)//n2)*(n2-1),p)
		for i in range(n2):
			h2[i]=pol_multiplicar_escalar(h2[i], n2**(p-2), p)
		#print("h2", h2)
		h1=beta_i(h2,(2*n1)//n2, n2)
		#print(h1)
		for s in range(0,len(h1)):
			h1[s] += [0 for j in range(0,pow(2,k)-(2*n1))]
		#print("h1",h1)
		h=beta(h1,n1)
		#print(h)
		#print("len h", len(h[0]), 4*n1)
		res = [0 for i in range(4*n1)]
		for i in range(n2):
			res = pol_sumar(res,h[i],p)
		#print("res", res)
		return quitar_ceros(res)
		

def mult_pol_mod(f,g,p):
	f = quitar_ceros(f)
	g = quitar_ceros(g)
	if(p==2):
		return ("Errore: numero primo introducido debe ser distinto de 2")
	k=0
	deg_f = len(f)-1
	deg_g = len(g)-1
	while(deg_f + deg_g >= pow(2,k)):
		k += 1
	f+=[0 for i in range(pow(2,k)-len(f))]
	g+=[0 for i in range(pow(2,k)-len(g))]
	print("k", k)
	return mult_ss_mod(f,g,k,p)

#shift dei coefficienti per la radice dell'unità (ricorda di cambiare di segno)

# algoritmo de Cooley-Tuckey para calcular DFT_n(p)
# n = len(p) debe ser una potencia de 2 y xi debe ser # una raız n-esima primitiva de la unidad
def fft(f, xi,p): #stiamo passando 4*n1/n2 come xi
	n = len(f) 
	if n == 1:
		return f
	f_even = [[0 for i in range(len(f[0]))] for j in range(n//2)]
	f_odd = [[0 for i in range(len(f[0]))] for j in range(n//2)]
	for i in range(n//2):
		f_even[i] = f[2*i]
		f_odd[i] = f[(2*i)+1] 
	a_even = fft(f_even, xi*2,p) 
	a_odd = fft(f_odd, xi*2,p)
	a = [[0 for i in range(len(f[0]))] for j in range(n)]
	for i in range(n//2):
		a[i] = pol_sumar(a_even[i],shift(a_odd[i],xi*i),p) #non possiamo farlo così
		#a[i + n//2] = pol_sumar(a_even[i],shift(a_odd[i],xi*(i+len(f[0]))),p)
		a[i + (n//2)] = pol_restar(a_even[i],shift(a_odd[i],xi*i),p)
		#chiamiamo ricorsivamente mult_ss_mod con k=1+k1 (n1=2^k1.. 2n1=2^(k1+1))
		#si k<2 negaconvolucion che sarebbe moltiplicare normalmente e cambiare di segno
	#print("a",a )
	return a
	
#print(mult_pol_mod([1,2,3],[4,5],7))
#print(mult_pol_mod([1, 0], [3, 0], 7))
#print(mult_ss_mod([1,1,1,1,1,0,0,0], [1,1,1,1,1,0,0,0],3, 7))
#print(mult_ss_mod([1,2,3,4], [4,5,6,6], 2, 7) )
#print(mult_pol_mod([4, 5, 1, 0, 0, 0, 0, 0, 0], [3, 4, 4, 0, 0, 0, 0, 0, 0], 7))#[5, 3, 4, 3, 4]
#print(mult_pol_mod([3, 0, 1], [1, 5, 5], 7)) #h1 [3, 1, 2, 5, 5]
#print(mult_pol_mod([4, 1], [1, 1], 7))
#mult_pol_mod([4, 0, 2, 3, 4, 1, 3, 0, 6, 1, 1, 5, 0, 6, 6, 5, 1], [6, 5, 5, 6, 3, 5, 0, 0, 6, 4, 4, 2, 6, 5, 6, 4, 1], 7)
#mult_ss_mod([3], [0], 0, 13)
#print(mult_pol_mod([1, 6, 2, 5, 6], [2, 5, 0, 3, 5], 7)) # [2, 3, 6, 2, 4, 3, 4, 1, 2]