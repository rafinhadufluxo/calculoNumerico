# https://github.com/IgorAlmeeida/Calculo-Numerico dê uma olha neste repositorio

def integralSimpson(listaPontos):
    a = listaPontos[0][0]
    b = listaPontos[len(listaPontos)-1][0]
    h = (b - a)/(len(listaPontos)-1)
    soma1 = 0
    soma2 = 0
    soma3 = 0
    for i in range(len(listaPontos)):
        if(i == 0 or i == len(listaPontos)-1):
            soma1+= listaPontos[i][1]
        elif (i % 2 == 0):
            soma3 += listaPontos[i][1]
        else:
            soma2 += listaPontos[i][1]
    #h = h/3
    h = (3 * (1/3))/8
    return h*(soma1 + 4*soma2 + 2*soma3)

def integralTrapezio(listaPontos):
    a = listaPontos[0][0]
    b = listaPontos[len(listaPontos)-1][0]
    h = (b - a)/(len(listaPontos)-1)
    soma = 0

    for i in range(len(listaPontos)):
        if(i == 0 or i == len(listaPontos)-1):
            soma += listaPontos[i][1]/2
        else:
            soma += listaPontos[i][1]

    return h*soma

#listaPontos=[[0,0],[2,1.8],[4,2],[6,4],[8,4],[10,6],[12,4],[14,3.6],[16,3.4],[18,2.8],[20,0]]
listaPontos= [[0,1],[1/3,1.3956],[2/3,1.9477],[1,2.7182]] # dados da aula do pedro borges

print("Trapézios:")
print (integralTrapezio(listaPontos))
print("")
print("Simpson:")
print(integralSimpson(listaPontos))