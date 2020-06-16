import math

#Método de Newton

#Este método exije que se se adivinhe um valor inicial (x) e que se calcule a derivada
#O valor inicial de x deve ser um valor proximo aos zeros da função encontrados no máxima

f = lambda x : 2*(x**2) - 5*x - 2   #Escreva aqui a função
df = lambda x : 4*x - 5             #Escreva aqui a derivada da função

f = lambda x : (0.69*x - 1)/(x-1)
df = lambda x: 0.69/(x-1)-(0.69*x-1)/ ((x-1)**2)

f = lambda x : (math.cos(x+1.2))**3 +x-3.6
df = lambda x: 1-3*(math.cos(x+1.2))**2*math.sin(x+1.2)

f = lambda x : (math.e)**(-x);
df = lambda x : (math.cos(x+1.2))**3 +x-3.6

f = lambda x : math.sin(10*x) + math.cos(3*x)
df = lambda x: 10*math.cos(10*x) - 3*math.sin(3*x)

n = 0
x = 3.2
xn = 1000                               #Escreva aqui o valor inicial de x

while abs((x-xn)/x) > 0.005 or abs((x-xn)/xn) > 0.005:                 #O numero de iterações será o suficiente que se ache necessário para obter o resultado
    n+=1
    xn = x
    x -= (f(x)/ df(x))              #Quanto mais itrações, maior a chance de obter o resultado correto, porém, será um pior algoritmo

print(x)                            #Print ao resultado do método, se tiver vários zeros alterar o valor de x corretamente
print(n)
                                    #Dica: Ver os zeros da função no maxima para chegar ao resultado através deste método

#Guia para Métodos Numéricos não iterativos:

#1-Calcular os zeros da função no maxima
#2-Adivinhar valores conforme os zeros da função no maxima
#3-Aplicar Método Numérico (Método de Newton, neste caso)
#4-Comparar soluções em termos de erros absolutos



