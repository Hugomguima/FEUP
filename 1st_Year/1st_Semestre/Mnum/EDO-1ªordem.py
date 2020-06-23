# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:58:10 2019

@author: Hugo
"""

#Resolução de EDO de 1ªa ordem
#Utilizando o Método de rk4
#Metodo de 4ªa ordem


def rk4(f,g,x,y,z,h,maximo):
    
    while(x < maximo):
        
        xn = x
        yn = y
        zn = z
        
        dy1 = h*f(x,y,z)
        dz1 = h*g(x,y,z)
        
        dy2 = h*f(x + h/2, y + dy1/2,z + dz1/2)
        dz2 = h*g(x + h/2, y + dy1/2,z + dz1/2)
        
        dy3 = h*f(x + h/2, y + dy2/2,z + dz2/2)
        dz3 = h*g(x + h/2, y + dy2/2,z + dz2/2)
        
        dy4 = h*f(x + h, y + dy3,z + dz3)
        dz4 = h*g(x + h, y + dy3,z + dz3)
        
        x = xn + h
        y = yn + dy1/6 + dy2/3 + dy3/3 + dy4/6
        z = zn + dz1/6 + dz2/3 + dz3/3 + dz4/6
#        print("x =",x,"y =",y)
    
    return (y,z,x)

#Dados
#Funcao
f = lambda x,y,z : z*y + x
g = lambda x,y,z : z*x + y

f = lambda x,y,z : 0*x + 0*y +z
g = lambda x,y,z : x - 3*z - 2*y

#Altura
h = 0.0125
h = 0.025
#Ponto inicial
x = 0
y = 1
z = 1
x = 0
y = 0
z = 0
#Intervalo superior do integral
maximum = 0.4999

sy = rk4(f,g,x,y,z,h,maximum)[0]
s1y= rk4(f,g,x,y,z,h/2,maximum)[0]
s2y= rk4(f,g,x,y,z,h/4,maximum)[0]

xy = rk4(f,g,x,y,z,h,maximum)[2]
x1y= rk4(f,g,x,y,z,h/2,maximum)[2]
x2y= rk4(f,g,x,y,z,h/4,maximum)[2] 

qcy = (s1y-sy)/(s2y-s1y)#Formula do quociente de convergencia
erroy = (s2y-s1y)/15#Formula do ero de convergencia de 4ª ordem

sz = rk4(f,g,x,y,z,h,maximum)[1]
s1z= rk4(f,g,x,y,z,h/2,maximum)[1]
s2z= rk4(f,g,x,y,z,h/4,maximum)[1]

xz = rk4(f,g,x,y,z,h,maximum)[2]
x1z= rk4(f,g,x,y,z,h/2,maximum)[2]
x2z= rk4(f,g,x,y,z,h/4,maximum)[2]

qcz = (s1z-sz)/(s2z-s1z)#Formula do quociente de convergencia
erroz = (s2z-s1z)/15#Formula do ero de convergencia de 4ª ordem

print()
print("Método de Runga-Kutta-4:")#Utilizar RK4 para resolver EDOs 1ª ordem

print()
print("xy =",xy,"Sy =",sy)#Resultado de x
print("xz =",xz,"Sz =",sz)#Resultado de y

print()
print("x1y =",x1y,"S1y =",s1y)#Resultado de x com h/2
print("x1z =",x1z,"S1z =",s1z)#Resultado de y com h/2

print()
print("x2y =",x2y,"S2y =",s2y)#Resultado de x com h/2
print("x2z =",x2z,"S2z =",s2z)#Resultado de y com h/2

print()
print("Qcy =",qcy,"Qcz =",qcz)#Quocientes de Convergencia
print()
print("Erroy =",erroy,"Erroz =",erroz)#Erros de convegencia


#Caso queira resolver EDO's de ordem superior,
#É neessário transformar a EDOO numa EDO de 1ªa ordem,
#Fazendo a substituição z = dy/dx






