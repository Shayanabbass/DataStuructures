class HashTableLinearProbing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size
    
    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key, value):
        hash_value = self.hash_function(key)
        
        while self.table[hash_value] is not None and self.table[hash_value][0] != key:
            hash_value = (hash_value + 1) % self.size
        
        self.table[hash_value] = (key, value)
    
    def search(self, key):
        hash_value = self.hash_function(key)
        
        while self.table[hash_value] is not None:
            if self.table[hash_value][0] == key:
                return self.table[hash_value][1]
            hash_value = (hash_value + 1) % self.size
        
        return None
    
    def remove(self, key):
        hash_value = self.hash_function(key)
        
        while self.table[hash_value] is not None:
            if self.table[hash_value][0] == key:
                self.table[hash_value] = None
                return
            hash_value = (hash_value + 1) % self.size
        
        raise KeyError(key)
