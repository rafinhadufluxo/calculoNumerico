#pego do git (https://github.com/douglasgusson/regra-simpson)
# como compilar $ python3 main_regra_simpson.py 0 1 90 '3*x**(1/3)/e**(x**2)'

# a função foi extraida do repositorio do igor, observe a função dada (*derive*)

import sys
from math import *


def simpson(a, b, n, f):
    count = 0
    h = (b - a) / n
    soma = (execf(f, a) + execf(f, b))
    
    for i in range(1, n):
        x = a + i * h
        
        if i % 2 == 0:
            soma += 2 * execf(f, x)
            
        else:
            soma += 4 * execf(f, x)
           
            
    print(count)
    return (soma * (h / 3))


def execf(f, x=None):
    return eval(f)


if __name__ == '__main__':
    re = simpson(float(sys.argv[1]),
                 float(execf(sys.argv[2])),
                 int(sys.argv[3]),
                 sys.argv[4])
    print(re)