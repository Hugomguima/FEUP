import math

#Sistemas de duas equações

f = lambda x,y : 1-x**2-y
dfx = lambda x,y : -2*x
dfy = lambda x,y : -1

g = lambda x,y : 0.7+x-y
dgx = lambda x,y : 1
dgy = lambda x,y : -1

"""
f = lambda x,y : x+y-3
dfx = lambda x,y : 1
dfy = lambda x,y : 1

g = lambda x,y : x**2 + y**2-9
dgx = lambda x,y : 2*x
dgy = lambda x,y : 2*y
"""
x=1000
y=1000

xn = 0.001
yn = 1

n=0

while abs((x-xn)/x) > 0.005 or abs((x-xn)/xn) > 0.005:
    
    x = xn
    y = yn
    n+=1

    jacobian = dfx(x,y)*dgy(x,y) - dgx(x,y)*dfy(x,y)
    hn = f(x,y)*dgy(x,y) - g(x,y)*dfy(x,y)  
    kn = dfx(x,y)*g(x,y) - dgx(x,y)*f(x,y)
    
    xn = x - hn/jacobian
    yn = y - kn/jacobian

print("x =",xn )
print("y =",yn )
    
print(n)