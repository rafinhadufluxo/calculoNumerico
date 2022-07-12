#Regra dos Trapézios + Algoritmo em Python


import math

def trapz(f,a,b,n): # regra do trapezio
    h =(b -a) /n
    soma = 0
    for k in range(1,n):
        soma +=f(a+k*h)
    soma *=2
    soma +=(f(a) + f(b))
    return (h/2) * soma


def f(x): # coloque a funcao aqui!
    return math.exp(-x ** 2)
    

a, b = 0, 1
n = 1_000_000 # numero de interações

r = trapz(f,a,b,n)
print('exp:\t\t',r)

def g (x):
    return math.cos(x ** 2)

a = 0
b = math.pi /2
n = 100

r = trapz(g,a,b,n)
print('cos (x^2):\t', r)
