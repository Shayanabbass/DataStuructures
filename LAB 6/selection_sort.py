A=["p","y","t","h","o","n"]
count=0
for i in range(len(A)):
    min_indx=i
    for j in range(i+1,len(A)):
        if A[min_indx]>A[j]:
            min_indx=j
            count+=1
    A[i],A[min_indx]=A[min_indx],A[i]        
print(A)    
print("No of swapping:",count)    


