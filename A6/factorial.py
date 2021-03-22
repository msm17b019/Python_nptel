def factorial(n):
    product=1
    for i in range(1,n+1):
        product=product*i
    return product

n=int(input('Enter the number (integer): '))
if n<0:
    print('factorial is not defined for negative integer')

else:
    f=factorial(n)
    print('factorial of',n,'is',f)
