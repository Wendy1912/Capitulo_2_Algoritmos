import string

class HashTable:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        
    def hash(self, key):
        hash_value = 0
        prime1 = 31
        prime2 = 37
        for byte in key.encode():
            hash_value = hash_value * prime1 + byte + prime2
        return hash_value % self.capacity
    
    def insert(self, key):
        index = self.hash(key)
        if self.keys[index] is None:
            self.keys[index] = key
            self.values[index] = 1
            self.size += 1
        else:
            self.values[index] += 1
            
    def get(self, key):
        index = self.hash(key)
        if self.keys[index] == key:
            return self.values[index]
        return None

def strip_punctuation(word):
    return word.strip(string.punctuation)

def count_words(file_name):
    table = HashTable()
    with open(file_name, 'r') as f:
        for line in f:
            for word in line.split():
                word = strip_punctuation(word).lower()
                if word:
                    count = table.get(word)
                    if count is None:
                        table.insert(word)
                    else:
                        table.values[table.hash(word)] += 1
    return table

def print_word_counts(table):
    print("{:<20} {}".format("Palabra", "Contar"))
    print("{:<20} {}".format("----", "-----"))
    for i in range(table.capacity):
        if table.keys[i] is not None:
            print("{:<20} {}".format(table.keys[i], table.values[i]))
    
table = count_words('C:\\Users\\Alicia Ulloa\\OneDrive\\Documentos\\IS-310_ALGORITMOS Y ESTRUCTURAS DE DATOS\\Unidad 3\\Cap 11\\11.5\\sample_text.txt')
print_word_counts(table)
