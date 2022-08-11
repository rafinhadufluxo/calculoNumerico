//====AJUSTE POR LINEARIZAÇÃO: Y=aexp(bx) ==========
  
clc  
n=5; //número de pontos
m=2; //grau do polinômio


X=[0;0.25;0.5;0.75;1];
Y=[00.62996;0.7937;0.90856;1];

for i=1:n
    YY(i)=log(Y(i));
end
//====matriz A====
for i=1:n
    for j=1:m+1
        A(i,j)=X(i)^(j-1);
    end
end

x=inv(A'*A)*A'*YY;

xx=linespaço(X(1),X(n),100);
for i=1:100
   YL(i)=x(1)+x(2)*xx(i);
end



//plot(X,YY,'.b',xx,YL,'b')//,X1,yy,'b')
//legend('dados','ajustar log')

a=exp(x(1));
b=x(2);
//====Cálculo de y instalado com n pontos

for i=1:n
    Ya(i)=a*exp(b*X(i));
end

//=====GRÁFICO======

// Y aproximado para 100 pontos
    for i=1:100
        Yaa(i)=a*exp(b*xx(i));
    end


plot(X,Y,'.r',xx,Yaa,'r',xx,YL,'b',X,YY,'.b')//,X1,yy,'b')
legenda('dados','ajustar','ajustar log','dadosL',2)

// ====determinação =======================================
S=0;
for i=1:n
   S=S+Y(i);
end
ym=S/n;
SM=0;
SN=0;
for i=1:n
    SM=SM+(Y(i)-ym)^2;
    SN=SN+(Y(i)-Ya(i))^2;
end

R2=1-SN/SM;
printf('Co=%f\n',a)
printf('k=%f\n',b)
printf('R2=%f\n',R2)







