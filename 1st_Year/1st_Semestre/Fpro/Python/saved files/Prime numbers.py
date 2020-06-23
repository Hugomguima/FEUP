n = int(input("Introduce a number: "))    

divisors = 0

for i in range(1, n + 1):
    if n % i == 0:
        divisors += 1

if divisors ==2:
    result = True
else :
    result = False
    
print(result)