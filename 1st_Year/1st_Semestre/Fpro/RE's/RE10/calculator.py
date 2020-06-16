def calculator(expr):
    if type(expr) == int:
        return expr
    total = 0
    if type(expr[0]) == tuple:
        a = calculator(expr[0])    
    else:
        a = expr[0]    
    if type(expr[2]) == tuple:
        b = calculator(expr[2])    
    else:
        b = expr[2]
    if expr[1] == "+":           
        total = a + b        
    elif expr[1] == "-":           
        total = a - b
    elif expr[1] == "*":           
        total = a * b              
    return total
#print(calculator((1, '+', 2)))
#print(calculator(((1, '+', 2), '*', 3)))           