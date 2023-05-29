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
        print(L,M,"According to merge sort")
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
    def bucket_sort(self):
        n = self.length
        slot_num = 10  # 10 means 10 slots, each slot's size is 0.1
        buckets = [[] for _ in range(slot_num)]

        # Put array elements in different buckets
        for num in self.age:
            index_b = int((num - min(self.age)) / (max(self.age) - min(self.age)) * (slot_num - 1))
            buckets[index_b].append(num)

        # Sort individual buckets using insertion sort
        for i in range(slot_num):
            # Perform insertion sort on the current bucket
            for j in range(1, len(buckets[i])):
                key = buckets[i][j]
                k = j - 1
                while k >= 0 and buckets[i][k] > key:
                    buckets[i][k + 1] = buckets[i][k]
                    k -= 1
                buckets[i][k + 1] = key

        # Concatenate the sorted buckets
        sorted_list = []
        for bucket in buckets:
            sorted_list.extend(bucket)

        self.age = sorted_list
        print(self.age,"bucket sort")


    
    def radix_sort(self):
        max_num = max(self.age)
        exp = 1

        while max_num // exp > 0:
            n = len(self.age)
            output = [0] * n
            count = [0] * 10

            for i in range(n):
                index = (self.age[i] // exp) % 10
                count[index] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            i = n - 1
            while i >= 0:
                index = (self.age[i] // exp) % 10
                output[count[index] - 1] = self.age[i]
                count[index] -= 1
                i -= 1

            for i in range(n):
                self.age[i] = output[i]

            exp *= 10

        print(self.age,"radix sort")









while True:
    print("1 - Bubble Sort")
    print("2 - selection Sort")
    print("3 - insertion Sort")
    print("4 - Merge Sort")
    print("5 - Quick Sort")
    print("6 - Count Sort")
    print("7 - Shell Sort")
    print("8 - BucketSort")
    print("9 - Radix Sort")




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
    elif select==8:
    # sorting_algorithm.take_input()
        sorting_algorithm = SortingAlgorithm()

        sorting_algorithm.bucket_sort() 


        break 
    elif select==9:
    # sorting_algorithm.take_input()
        sorting_algorithm = SortingAlgorithm()

        sorting_algorithm.radix_sort() 


        break 
          
        

    else:
        print("Invalid input. Please try again.")
