class Students:
    def __init__(self,name,course,rl,cgpa):
        self.name=name
        self.course=course
        self.rl=rl
        self.cgpa=cgpa
    def display(self):
        print("NAME=",self.name)    
        print("COURSE=",self.course)
        print("ROLL NO=",self.rl) 
        print("CGPA=",self.cgpa)  
nl=["ali","shoaib","shayan","hadi","bilal","ahsan"]
rl=[44,12,76,46,89,90]
cl=["SE","CS","MBBS","BBA","BCOM","MCOM"]
cgpal=[2.4,3.3,3.4,3.9,4.0,3.7]
objl=[]
for i in range(0,6):
    objl.append(Students(nl[i],cl[i],rl[i],cgpal[i]))        
#linear sarch
search=int(input("enter roll no\n"))
n=len(rl)
for j in range(0,n):
    if(rl[j]==search):
        print(objl[j].display())
#bubble sort        
for k in range(n):
    for s in range(0,n-k-1):
        if rl[s]>rl[s+1]:
            temp=rl[s]
            rl[s]=rl[s+1]
            rl[s+1]=temp     
print(rl)           
#BINARY SEARCH
def binarysearch(array,x,low,high):
    while(low<=high):
        mid=low+(high-low)//2
        if array[mid]==x:
            return mid
        elif(array[mid]<x):
            low=mid+1
        else:
            high=mid-1
    return -1
nl1=["shoaib","ali","hadi","shayan","bilal","ahsan"]

cl1=["CS","SE","BBA","MBBS","BCOM","MCOM"]
cgpal1=[3.3,2.4,3.9,3.4,4.0,3.7]

obj2=[]
array=rl
x=int(input("enter roll no\n"))            
result=binarysearch(array,x,0,len(array)-1)
if result!=-1:
    rs=(result)
    for l in range(0,6):
        obj2.append(Students(nl1[l],cl1[l],array[l],cgpal1[l]))  
    print(obj2[rs].display())

