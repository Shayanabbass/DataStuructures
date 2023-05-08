import random
from timeit import default_timer as timer
from collections import deque
start=timer()
def enque(m,n):

   for i in range(m):
        queue=[]
        for j in range(n):
                    queue.append(random.randint(1,n))
        for k in range(n):
                    queue.pop(0)  
        print(queue)          

enque(3,100)
end=timer()
print(end-start)


def que_dequeue(m,n):
    
 for i in range(m):

   q=deque()
   for j in range(n):
        q.append(random.randint(1,n))
   for k in range(n):
          q.popleft()   
que_dequeue(3,100)          
