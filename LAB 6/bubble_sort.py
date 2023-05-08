def bubblesort(chars):
    count=0
   
    n=len(chars)
    for i in range(n):
        for j in range(0,n-i-1):
            if chars[j]>chars[j+1]:
                chars[j],chars[j+1]=chars[j+1],chars[j]
                count+=1
    print("No of swapping:",count)            
    return ''.join(chars)
chars=["p","y","t","h","o","n"]
   
print(bubblesort(chars))