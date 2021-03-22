a=[]
for i in range(1,1001):
    a.append(i)

def linear_search(a,x):
    n=len(a)
    for j in range(n):
        if(x==j):
            print(j)
            break
        else:
            continue

x=int(input("Enter the number you have to search: "))
linear_search(a,x)