def bubble_sort(array):
    
    a=len(array)
    for i in range(a):
        for j in range(a-1):
            if (array[j]>array[j+1]):
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
            
            else:
                continue


array=[7,1,4,9,3,6,2,8]
bubble_sort(array)
print(array)
