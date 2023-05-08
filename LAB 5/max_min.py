#prgrm to find max and min of arr
arr=[11,6,4,3,8]
max=arr[0]
for i in arr:
    if(i>max):
        max=i
    else:
        max=max
print(max)       
min=arr[0]
for j in arr:
    if(j<min):
        min=j
    else:
        min=min
print(min)        
           