#Sistemas de duas equações

f = lambda x,y : -((1-y)**0.5)
g = lambda x,y : 0.7 + x
#f = lambda x,y : y-0.7
#g = lambda x,y : 1-x**2



x=1000
y=1000

xn = 0
yn = 0.5

n=0

while abs(xn-x)>10**-3 or abs(yn-y) > 10**-3:
    
    x = xn
    y = yn

    n+=1
    
    xn = f(x,y)
    yn = g(x,y)

    print("x =",xn )
    print("y =",yn )
    
print(n)