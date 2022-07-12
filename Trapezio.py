import math

def simps(f,a,b,n):
    h = (b-a)/n
    particao = [a + k * h for k in range(n+1)]
    particao_odd = [a + k * h for k in range(1, n+1, 2)]
    particao_even = [a + k * h for k in range(2, n+1, 2)]


#a,b=0,1
#n =8 # numero de sub-intervalos
#h = (b-a)/n
#particao = [a + k * h for k in range(n+1)]
#particao_odd = [a + k * h for k in range(1, n+1, 2)]
#particao_even = [a + k * h for k in range(2, n+1, 2)]

print(particao)
print(particao_odd)
print(particao_even)

def f(x):
    return x ** x

a, b = 0,1
n = 4 #n é o numero de subintervalos e n/2 e o numero de parábols e n+1 é o numero de pontos na partida

def g(x):
    return math.cos(x**2)

a, b=0, math.pi /2

