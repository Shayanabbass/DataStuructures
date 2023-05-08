def insertionsort(array):
    count=0
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while (j>=0 and key<array[j]):
            array[j+1]=array[j]
            j=j-1
            count+=1
        array[j+1]=key
    print(count)
array=["p","y","t","h","o","n"]
insertionsort(array)
print(array)           