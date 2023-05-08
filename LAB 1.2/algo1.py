def add():
    array=[] 
    num=int(input("What is the size fo your array?"))
    for i in range(num):
        number=int(input("Enter the number"))
        array.append(number)
    
    a=0
    for i in array:
       a=a+i
    print(a)
add()

    