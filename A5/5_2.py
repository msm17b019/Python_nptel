array=input().split()
swap=0
for i in range(len(array)):
    for j in range(i+1,len(array)):

        if(int(array[i])>int(array[j])):

            temp=array[i]
            array[i]=array[j]
            array[j]=temp
            swap=swap+1
print(swap,end="")