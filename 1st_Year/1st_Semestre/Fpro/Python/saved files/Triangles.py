n1 = int(input('Introduce the first side of the triangle: '))
n2 = int(input('Introduce the second side of the triangle: '))
n3 = int(input('Introduce the third side of the triangle: '))
result = ""
if n1 <= 0 or n2 <= 0 or n3 <= 0:
    result = "The numbers must be positive!!"
    return result
if (n1 + n2 <= n3) or (n1 + n3 <= n2) or (n2 + n3 <= n1):
    result = ('Not a triangle')
    return result
elif n1 == n2 == n3 :
    result = ('The triangle is equilateral')
elif (n1 == n2 != n3) or (n1 == n3 != n2) or (n2 == n3 != n1):
    result = ('The triangle is Isosceles')
else:
    result = ('The triangle is Scalene' )
return result