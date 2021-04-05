n=int(input(''))


def number_of_ways(n):
    if n%2!=0 or n<0:
        print('invalid')
    else:
        a=[]
        for i in range(2,n+1):
            if i%2==0:
                a.append(i)
        

        count=1
        for j in range(0,len(a)):
            for k in range(0,len(a)):
                if a[j]+a[k]==n:
                    count+=1
        print(count)



        
number_of_ways(n)
