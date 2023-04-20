class HashTable:
    def __init__(self, size=128):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.max_load_factor = 0.5
        self.num_keys = 0
        self.num_displacements = 0
    
    def __setitem__(self, key, value):
        self.insert(key, value)
    
    def __getitem__(self, key):
        index = self.__find_index(key)
        if index is None:
            raise KeyError(str(key))
        return self.values[index]
    
    def __contains__(self, key):
        index = self.__find_index(key)
        return index is not None

    def __find_index(self, key, probe=1):
        hash_value = self.hash_function(key)
        index = hash_value % self.size
        for i in range(probe):
            if self.keys[index] is None or self.keys[index] == key:
                return index
            index = (hash_value + i**2) % self.size
        return None

    def hash_function(self, key):
        return hash(key) % self.size

    
    def insert(self, key, value):
        if (self.num_keys + 1) / self.size > self.max_load_factor:
            self.__grow_table()
        index = self.__find_index(key)
        if index is None:
            index = self.__find_empty(key)
        if index is not None:
            self.keys[index] = key
            self.values[index] = value
            self.num_keys += 1
        else:
            raise Exception("Probe sequence is full")
    
    def __find_empty(self, key):
        hash_value = self.__hash(key)
        i = 0
        while i < self.size and self.keys[hash_value] is not None and self.keys[hash_value] != key:
            i += 1
            hash_value = (hash_value + i) % self.size
            self.num_displacements += 1
        if self.keys[hash_value] is None:
            return hash_value
        return None
    
    def __hash(self, key):
        return hash(key) % self.size
    
    def get_displaced_keys(self, probe):
        displaced_keys = []
        for i in range(self.size):
            if self.keys[i] is not None:
                index = self.__find_index(self.keys[i], probe)
                if index != i:
                    displaced_keys.append(self.keys[i])
        return displaced_keys

    
    # Mejora Ejercicio 11.3
    def __grow_table(self):
        oldKeys = self.keys
        oldValues = self.values
        oldSize = self.size
        self.size = oldSize * 2
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.num_keys = 0
        self.num_displacements = 0
        for i in range(oldSize):
            if oldKeys[i] is not None:
                self.insert(oldKeys[i], oldValues[i])
