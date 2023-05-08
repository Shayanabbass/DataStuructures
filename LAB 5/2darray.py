marks=[[70,78,90],
       [56,78,88],
       [90,77,66]]
avgmarks=[]
for i in marks:
    avgmarks.append(sum(i)/len(i))
print(avgmarks)  
subjmarks=[]

for j in range(len(marks[0])) :
    avg=[marks[k][j] for k in range(len(marks))]
    subjmarks.append(sum(avg)/len(avg))
print(subjmarks)    