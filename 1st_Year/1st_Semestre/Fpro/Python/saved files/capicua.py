def capicua():
    num_1 = int(input('Write an integer number '))
    if num_1 <0:
        result = "Number must be positive!!'
        return result
    num = num_1
    inverse = 1
    while num / 10 > 0:
        digit = num % 10
        inverse = inverse * 10 + digit
        num = num // 10
    if inverse == num_1:
        result = str(num_1) + " is a palindrome."
    else:
        result = str(num_1) + " is not a palindrome."
    return result        
