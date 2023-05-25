class SortingAlgorithm():
    def __init__(self):
        self.age = []
        

    
        self.length = int(input("Enter the length: "))
        for i in range(self.length):
            number = int(input("Enter a number: "))
            self.age.append(number)

    def bubble_sort(self):
        n = self.length
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.age[j] > self.age[j + 1]:
                    self.age[j], self.age[j + 1] = self.age[j + 1], self.age[j]
        print(self.age, "according to bubble sort")

    def selection_sort(self):
        n= len(self.age)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if(self.age[j]>min_index):
                    min_index=j
            self.age[min_index],self.age[i]= self.age[i],self.age[min_index]
        print(self.age,"according to selection sort")  
    def insertion_sort(self):
        n=len(self.age)
        for i in range(1,n):
            key=self.age[i]
            j=i-1
            while(j>=0 and key<self.age[j]):
                self.age[j+1]=self.age[j]
                j=j-1
            self.age[j + 1] = key
        print(self.age,"according to insertion sort")
    def merge_sort(self):
        n=len(self.age)
        if(n>1):
            r=n//2
            L=self.age[:r]
            print(L)
            M=self.age[r:]
            
            i=k=j=0
            while i<len(L) and j<len(M):
                if(L[i]<M[j]):
                    self.age[k]=L[i]
                    i+=1
                else:
                    self.age[k]=M[j]   
                    j+=1
                k+=1
            while i<len(L):
                self.age[k]=L[i]
                i+=1
                k+=1
            while j<len(M):
                self.age[k]=M[j]
                j+=1
                k+=1  
        print(self.age,"According to merge sort")
    def quick_sort(self):
        n= len(self.age)    
        pivot=self.age[-1]
        low=[]
        high=[]
        for i in range(n):
            if self.age[i]>pivot:
                high.append(self.age[i])
            else:
                low.append(self.age[i])
        for j in range(len(low)):
            min_index=j
            for k in range(j+1,len(low)):
                if(low[k])<low[min_index]:
                    min_index=k
            low[min_index],low[j]=low[j],low[min_index]
        for j in range(len(high)):
            min_index=j
            for k in range(j+1,len(high)):
                if(high[k])<high[min_index]:
                    min_index=k
            high[min_index],high[j]=high[j],high[min_index]    
        print(low+high,"quick sort")  
    def count_sort(self):
        n = self.length
        max1 = max(self.age)
        max2 = max1 + 1
        output = [0] * n
        count = [0] * max2
        
        for i in range(n):
            # Count how many times a number appears in self.age
            count[self.age[i]] += 1
        
        for k in range(1, max2):
            count[k] += count[k - 1]
            
        for i in range(n - 1, -1, -1):
            output[count[self.age[i]] - 1] = self.age[i]
            count[self.age[i]] -= 1

        # Copy the sorted elements from the output array to the original array
        for i in range(n):
            self.age[i] = output[i]

        # Print the sorted array
        print(self.age, "according to count sort")
    def shell_sort(self):
        n=self.length
        gap=n//2
        while gap > 0:
            for i in range(gap, n):
                temp = self.age[i]
                j = i
                while j>=gap and self.age[j-gap]>temp:
                    self.age[j]=self.age[j-gap]
                    j-=gap
                self.age[j]=temp
            gap//=2
        print(self.age,"shell sort")            








while True:
    print("1 - Bubble Sort")
    print("2 - selection Sort")
    print("3 - insertion Sort")
    print("4 - Merge Sort")
    print("5 - Quick Sort")



    select = int(input("Enter the number of sorting you want to perform: "))


    if select == 1:
        # sorting_algorithm.take_input()
        sorting_algorithm = SortingAlgorithm()

        sorting_algorithm.bubble_sort()
        break
    elif select==2:
        # sorting_algorithm.take_input()
        sorting_algorithm = SortingAlgorithm()

        sorting_algorithm.selection_sort() 
        break 
    elif select==3:
        # sorting_algorithm.take_input()
        sorting_algorithm = SortingAlgorithm()

        sorting_algorithm.insertion_sort() 
        break  
    elif select==4:
        # sorting_algorithm.take_input()
        sorting_algorithm = SortingAlgorithm()

        sorting_algorithm.merge_sort() 
        break 
    elif select==5:
        # sorting_algorithm.take_input()
        sorting_algorithm = SortingAlgorithm()

        sorting_algorithm.quick_sort() 
        break 
    elif select==6:
        # sorting_algorithm.take_input()
        sorting_algorithm = SortingAlgorithm()

        sorting_algorithm.count_sort() 
        break 
    elif select==7:
    # sorting_algorithm.take_input()
        sorting_algorithm = SortingAlgorithm()

        sorting_algorithm.shell_sort() 
        break 
          
        

    else:
        print("Invalid input. Please try again.")
