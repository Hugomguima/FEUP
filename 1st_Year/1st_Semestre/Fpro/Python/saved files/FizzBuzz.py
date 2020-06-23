n = int(input('write an integer number: '))
if n <= 0:
    result = 'Number must be positive!!'
    return result
result = ''
for i in range(1,n+1):
    if (i % 3 == 0 and i % 5 == 0):
        result = result + "" 
    elif (i % 3 == 0 and i % 5 != 0):
        result += 'Fizz '    
    elif (i % 5 == 0 and i % 3 != 0):
        result += 'Buzz '
    elif (i % 3 != 0 and i % 5 != 0): 
        result += str(i) + ' '
return result

    