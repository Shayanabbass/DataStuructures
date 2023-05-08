from timeit import default_timer as timer
start=timer()
def palindrome(s):
    

    stack=[]
    for i in s:
        stack.append(i)
    reversedstring=""  
    while len(stack)>0 :
        reversedstring+=stack.pop() 
    return s==reversedstring

    
 
print(palindrome("civic") )
end=timer()
print(end-start)


