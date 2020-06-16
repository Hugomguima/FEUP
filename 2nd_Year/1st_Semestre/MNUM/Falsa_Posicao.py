import math

#Método da Falsa POsição ou da Corda

f = lambda x : -2.75*(x**3) + 18*(x**2) - 21*x - 12 #Defina aqui a sua função
#f = lambda x : x-2*math.log(x) - 5
#f = lambda x: 2**(x**(1/2)) -10*x +1
f = lambda x : math.sin(10*x) + math.cos(3*x)

                                    
a = 3.2     #Coloque em "a" o primeiro valor que deseje manter constante
b = 3.3      #Coloque em "b" a priemira aproximação entre "a" e o zerto da função 
n = 1      #Numero de iterações. Inicializsdo a 1 pq a primeira iteração está fora od while

result =  (a * f(b) - b * f(a) ) / (f(b) - f(a))    #primeira iteração que deve ocorrer obrigatoriamente

while (abs(result-b) > (10**-5)):                   #Condição de paragem por convenção é 10**-5
    n += 1                                          #Incrementação do contador do numero de iterações
    b = result                                      #Alteração do valor de b para um valor mais próximo da raiz
    result = (a * f(b) - b * f(a) ) / (f(b) - f(a)) #Calcular uma nova aproximação

print(n)                                            #Print ao numero de iterações
print(result)                                       #Print ao resultado final
