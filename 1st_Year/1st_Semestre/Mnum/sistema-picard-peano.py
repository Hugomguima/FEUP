import math

#--------funcoes-----------------
def f(x,y):
    return math.sqrt((x*(y+5)-1)/2)

def g(x,y):
    return -math.sqrt(x+math.log10(x))

#--------Picard-Peano------------
def picard_peano(x,y):
    x_ant=x
    y_ant=y
    for i in range(20):
        x=f(x_ant,y_ant)
        y=g(x_ant,y_ant)
        x_ant=x
        y_ant=y
    print(x,y)
        
#------------Prints-------------
picard_peano(1.46,-1.41)