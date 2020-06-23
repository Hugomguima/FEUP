from math import factorial

def pascal(n):
    
    result = ""
            
    
    for j in range(n):
        for l in range(j + 1):
            value = int(factorial(j) / (factorial(l) * factorial(j - l)))
            result += " " + str(value)
        
        result += "\n"
        
    return result

                