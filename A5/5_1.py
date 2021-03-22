a=int(input("Enter an integer value: "))

for i in range(1,a+1):
    n=0
    for j in range(0,i):
        n=((10**j)*i)+n
    print(n)
        