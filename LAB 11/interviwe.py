list1=[22,44,23,12,56,11,21,32]
small=list1[0]
for i in range(len(list1)):
    if (small>list1[i]):
        small=list1[i]
 
   
small2=list1[0]
for j in range(len(list1)):
    if (small2>list1[j] and list1[j]!=small):
        small2=list1[j]
print(small2)  