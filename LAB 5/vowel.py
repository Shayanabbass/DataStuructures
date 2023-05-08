#program to print numbers of vowel in an array
alpha=[]
size=int(input("enter the size of array"))
for i in range(size):
    elements=input("enter the random alphabets")
    alpha.append(elements)
    
vowels=["a","e","i","o","u"]
count=0
for j in (alpha) :
    
    if j in vowels:
        count+=1
print(count)         