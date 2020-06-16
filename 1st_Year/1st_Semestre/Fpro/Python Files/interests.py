p=float(input('Introduce the principal amount: '))
n=float(input('Introduce the frequency that the interest is paid out: '))
r=float(input('Introduce the interest rate: '))
t=2
r=(r/100)
A=float(p*((1+r/n)**(2*n)))
print('The final amount is',A)