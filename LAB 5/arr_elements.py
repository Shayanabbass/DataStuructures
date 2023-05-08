#program to input elements in an array and print them
arr=[]
elements=int(input("Enter the size of array"))
for i in range(elements):
    numbers=int(input("enter the element of array"))
    arr.append(numbers)
print(arr)
#sum the elements of array
count=0
for j in arr:
   
    count+=j    
print(count)
    
