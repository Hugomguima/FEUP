#import math

#Método da Bisseção

#f = lambda x : -2.75*(x**3) + 18*(x**2) - 21*x - 12
#f = lambda x : x-2*math.log(x) - 5
f = lambda x: 2**(x**(1/2)) -10*x +1

a = 98    #Coloque em "a" o valor á esquerda do zero da função
b = 100   #Coloque em "b" o valor á direita do zero da função
n= 0      #Numero de iterações inicializado a 0

while(abs(a-b) > (10**-5)):  #Condição de paragem por convenção é 10**-5
    n += 1                   #Incrementação do contador do numero de iterações
    result = (a+b)/2         #Alteração do resultado para um novo valor entre "a" e "b"
    if( f(a)*f(result) < 0): #Verificar qual dos intervalos é que se deve eliminar
        b = result           #substiuir "b" pelo resultado caso a função esteja incluida no intervalo [a,result] 
    else:                     
        a = result           #substiuir "a" pelo resultado caso a função esteja incluida no intervalo [b,result]

print(n)
print(result)
