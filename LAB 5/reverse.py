#program ro read n values in array and display it in reverse order
arr=[]
reverse=[]
size=int(input("enter the size of array"))
for i in range(size):
    elements=int(input("enter the elements"))
    arr.append(elements)
print(arr)    
for j in range(len(arr)):
    display=(arr[-j -1])
    reverse.append(display)
print(reverse)    
