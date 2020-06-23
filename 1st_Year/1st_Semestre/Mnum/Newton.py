import math

#Método de Newton

#Este método exije que se se adivinhe um valor inicial (x) e que se calcule a derivada
#O valor inicial de x deve ser um valor proximo aos zeros da função encontrados no máxima

f = lambda x : 2*(x**2) - 5*x - 2   #Escreva aqui a função
df = lambda x : 4*x - 5             #Escreva aqui a derivada da função
x = 2                               #Escreva aqui o valor inicial de x

for i in range(20):                 #O numero de iterações será o suficiente que se ache necessário para obter o resultado
    x -= (f(x)/ df(x))              #Quanto mais itrações, maior a chance de obter o resultado correto, porém, será um pior algoritmo

print(x)                            #Print ao resultado do método, se tiver vários zeros alterar o valor de x corretamente
                                    #Dica: Ver os zeros da função no maxima para chegar ao resultado através deste método

#Guia para Métodos Numéricos não iterativos:

#1-Calcular os zeros da função no maxima
#2-Adivinhar valores conforme os zeros da função no maxima
#3-Aplicar Método Numérico (Método de Newton, neste caso)
#4-Comparar soluções em termos de erros absolutos


