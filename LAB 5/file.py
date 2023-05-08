file=open("dumm.txt","rt")
data=file.read()

list=[]
for i in data:
    if(i!=" "):
     list.append(i)
print(len(list))  


      