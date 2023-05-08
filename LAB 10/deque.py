from collections import deque
from timeit import default_timer as timer
start=timer()
def deque_1(s):
    
    

    q= deque(s)
    while len(q)>1:
        if q.pop()!=q.popleft():
            return False
     
   
    return True
    


    


print(deque_1("civic")) 
end=timer()  
print(end-start)      
        
    
