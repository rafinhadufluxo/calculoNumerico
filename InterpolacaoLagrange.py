# para entender melhor a logica deste codigo, leia este aqui artigo(link)
# https://cn.ect.ufrn.br/index.php?r=conteudo%2Finterp-lagrange

#Metodo interpolacao lagrange em python 3

def main():
    pontos = int(input('Quantidade de pontos que serão utilizados: '))
    X,Y =[],[]
    for i in range(pontos):
        x= float(input("X" + str(i)+ "="))
        X.append(x)

        y = float(input("Y" + str(i)+ "="))
        Y.append(y)

    x=float(input("Valor que se deseja interpolar:"))
    coefientes = []

    for indice in range(pontos):
        L=1
        for j in range(len(X)):
            if indice !=j:
                L*=(x-X[j]) / (X[indice]-X[j])
        coefientes.append(L)
    
    pn=0
    for i in range(len(coefientes)):
        pn +=Y[i]* coefientes[i]
    
    print("p("+ str(x)+ ")=", pn)

if __name__ == '__main__':
	main()

