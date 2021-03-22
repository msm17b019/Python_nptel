def factorial(n):
    if (n==0):
        return 1
    else:
        return n*factorial(n-1)
    
    

n=int(input('enter an integer value: '))


if n>=0:
    f=factorial(n)
    print(f)

else:
    print('please enter valid integer')

