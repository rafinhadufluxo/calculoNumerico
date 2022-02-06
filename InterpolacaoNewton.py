# Implementação em Python do método de Newton para interpolação polinomial.
# references -> https://pythonnumericalmethods.berkeley.edu/notebooks/chapter17.05-Newtons-Polynomial-Interpolation.html

def comecando():
    quant_pontos= int(input("informe quantidade de pontos:"))
    
    pontos, f_pontos=[],[] #arrays
    tabela =[]
    for i in range(quant_pontos):
        ponto = float(input("x%d =" %i)) #quantidade de x linha
        f_ponto = float(input("f(X%d) =" %i))
        pontos.append(ponto)
        f_pontos.append(f_ponto)
    tabela.append(f_pontos)
    
    print()
    x=float(input("Informe o ponto x a ser estimado:"))
    print()

    passo = 1
    for n in range(quant_pontos -1):
        ordem = []
        for m in range(len(tabela[n])-1):
            dif_divida = (tabela[n][m+1] - tabela[n][m]) / (pontos[m+passo] - pontos[m])
            ordem.append(dif_divida)
        tabela.append(ordem)
        passo +=1
    
    for k in range(len(tabela)):
        print("Ordem %d:" %k, tabela[k])
    print()

    aprox = 0
    grau = 0

    for i in range(len(tabela)):
        fator = tabela[i][0]
        for j in range(grau):
            fator *=(x - pontos[j])
        grau += 1
        aprox += fator
    print("A aproximação encontrada para f(%f) = %f" %(x,aprox))

if __name__ == '__main__':
	comecando()
