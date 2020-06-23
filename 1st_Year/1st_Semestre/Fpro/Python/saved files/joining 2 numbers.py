n1 = int(input('Introduce the first number: '))
n2 = int(input('Introduce the second number: '))
if n1 < 0 or n2 < 0:
    result = "Error. Numbers must be positive!!"
    return result
if n1 == 0 and n2 == 0:
    result = 0
    return result
elif n1 == 0:
    result == n2
    return result
elif n2 == 0:
    result == n1 * 10
    return result
    
n3 = n2
digits = 0

while n3 / 10 > 0:
    digits += 1 
    n3 = n3 // 10
    
result = n1 * (10 ** n3) + n2
return result

    
