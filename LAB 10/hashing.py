class Hashtable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash(key)
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                return self.table[index][i][1]
        return None

    def delete(self, key):
        index = self.hash(key)
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                del self.table[index][i]
                return

    def display(self):
        for i in range(self.size):
            print(i, end='')
            for j in self.table[i]:
                print('-->', end='')
                print(j, end='')
            print()

class HashtableLinearProbing(Hashtable):
    def insert(self, key, value):
        index = self.hash(key)
        if len(self.table[index]) == 0:
            self.table[index] = [(key, value)]
            return
        for i in range(self.size):
            index = (index + 1) % self.size
            if len(self.table[index]) == 0:
                self.table[index] = [(key, value)]
                return
            elif self.table[index][0] == key:
                self.table[index][1] = value
                return

class HashtableQuadraticProbing(Hashtable):
    def insert(self, key, value):
        index = self.hash(key)
        if len(self.table[index]) == 0:
            self.table[index] = [(key, value)]
            return
        c1, c2 = 1, 1
        for i in range(self.size):
            index = (index + c1 * i + c2 * i * i) % self.size
            if len(self.table[index]) == 0:
                self.table[index] = [(key, value)]
                return
            elif self.table[index][0] == key:
                self.table[index][1] = value
                return

class HashtableSeparateChaining(Hashtable):
    def insert(self, key, value):
        index = self.hash(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash(key)
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                return self.table[index][i][1]
        return None

    def delete(self, key):
        index = self.hash(key)
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                del self.table[index][i]
                return


# create a hashtable object with size 10
ht = Hashtable(10)

# insert some key-value pairs
ht.insert('apple', 1)
ht.insert('banana', 2)
ht.insert('cherry', 3)
ht.insert('date', 4)
ht.insert('elderberry', 5)

# display the hashtable
ht.display()

# search for a key and print its value
print(ht.search('banana'))  # outputs: 2

# delete a key-value pair
ht.delete('date')

