print('The goal of this programm is to write all prime number up to the number input by the user')
n = int(input('Introduce that number: '))

for i in range(1,n+1):
    counter = 0
    for a in range(1,i+1):
        if i % a == 0 :
            counter += 1
    if counter == 2:
        print(a,'is a prime number')