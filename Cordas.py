import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x + 3*math.cos(x) - np.exp(x) # mudamos aqui a expressão dada da questão para obtermos o resultado do calculo

a = -2#intervalo, a < b
b = -1
eps = 10**(-2)#0.000001
i = 0
y = []
eixoX = []
n = 100

x = np.linspace(a,b, 100)
for i in range(n):
    y.append(f(x[i]))
    eixoX.append(0)




#existencia da raíz no intervalo
def verificaRaiz(a, x0):
    if(f(a)*f(x0) <= 0):
        return True
    else:
        return False

#codigo principal
def cordas(a, b):
    
    if verificaRaiz(a, b):
        print ('Precisão: {:.10f}'.format(eps))
        print ('Intervalo: [{},{}]'.format(a, b))
        print ('\nProcesso de Convergencia:\n')
        cont_it = 0
        fx0 = 100
        x0 = (a*f(b)-b*f(a))/(f(b)-f(a))
        fa = f(a)
        
        while abs(fx0) > eps:
            cont_it += 1 #contador de iterações
            fx0 = f(x0)

            #verifica se o próprio ponto é a raíz
            if(f(a) == 0):
                print ('\nQuantidade de iterações processadas: {}'.format(cont_it))
                print ('Raiz no ponto X = {}'.format(a))
                return
            if(f(b) == 0):
                print ('\nQuantidade de iterações processadas: {}'.format(cont_it))
                print ('Raiz no ponto X = {}'.format(b))
                return

            #verifica raíz em um intervalo menor
            if verificaRaiz(a, x0):
                b = x0
            else:
                a = x0
                

            x0 = (a*f(b)-b*f(a))/(f(b)-f(a))
            print ('I{} = {:.10f}'.format(cont_it, x0))
          

    else:
        print ('Função não possui raíz no intervalo selecionado.')
        print ('Intervalo: [{},{}]'.format(a, b))
        return

    #resultado final
    print ('\nQuantidade de iterações processadas: {}'.format(cont_it))
    print ('Valor final: {:.10f}'.format(x0))
    plt.plot(x,y,'b',x,eixoX,'black')
    plt.show() 


if(a >= b):
    print ('Intervalo inválido.')

else:
    cordas(a, b)