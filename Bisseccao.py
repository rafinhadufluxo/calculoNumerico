import math

def f(x):
    #return( 2.0*math.sin(2.0*x) - x**3 + 3.0)
    return x**3 - 4 # mudamos aqui a expressão dada da questão para obtermos o resultado do calculo

l = 0.0000001
tol = 0.0000001
Ni = 100
cont = 0


a = float(input("Entre com o valor de 'a' do intervalo [a;b]: "))
b = float(input("Entre com o valor de 'b' do intervalo [a;b]: "))

c = b - a
x0 = (a*f(b) - b*f(a))/(f(b) - f(a))

while(c > l or math.fabs(f(x0)) > tol):
    if(f(a)*f(x0) < 0.0):
        b = x0
    if(f(a)*f(x0) > 0.0):
        a = x0
    c = b - a
    x0 = (a*f(b) - b*f(a))/(f(b) - f(a))
    cont = cont + 1
    if(cont >= Ni):
        break

print("\n\nRaíz: %f\nIterações: %i\nf(%f) = %g" %(x0,cont,x0,f(x0))) 