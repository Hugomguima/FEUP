import math

#--------funcoes----------------
def f(x,y):
    return 2*x**2-x*y-5*x+1

def g(x,y):
    return x+3*math.log10(x)-y**2

#--------derivadas--------------
def fx(x,y):
    return 4*x-y-5

def fy(x,y):
    return -x

def gx(x,y):
    return 1+3/x

def gy(x,y):
    return -2*y

#--------jacobiano-------------
def jacobiano(x,y):
    return fx(x,y)*gy(x,y)-fy(x,y)*gx(x,y)

#-------- hn e kn--------------
def hn(x,y):
    return (f(x,y)*gy(x,y)-fy(x,y)*g(x,y))/jacobiano(x,y)

def kn(x,y):
    return (fx(x,y)*g(x,y)-f(x,y)*gx(x,y))/jacobiano(x,y)

#--------newton---------------
def sistema(x,y):
    x_ant=x
    y_ant=y
    for i in range(20):
        x=x-hn(x_ant,y_ant)
        y=y-kn(x_ant,y_ant)
        x_ant=x
        y_ant=y
    print (x,y)
        
#-----------Prints-----------
sistema(3.5,2.3)
sistema(1.46,-1.41)