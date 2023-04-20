import random

class HashTable:
    def __init__(self, capacity=11):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        
    def hash(self, key):
        hash_value = 0
        prime1 = 31
        prime2 = 37
        for byte in key.to_bytes((key.bit_length() + 7) // 8, 'little'):
            hash_value = hash_value * prime1 + byte + prime2
        return hash_value % self.capacity
    
    # MODIFICACION EJERCICIO 11.4
    def doubleHashProbe(self, start, key):
        yield start % self.capacity
        step = self.doubleHashStep(key)
        for i in range(1, self.capacity):
            yield (start + i * step) % self.capacity
        
    def doubleHashStep(self, key):
        prime = self.primeBelow(self.capacity)
        return prime - (self.hash2(key) % prime)
    
    def hash2(self, key):
        hash_value = 0
        prime1 = 53
        prime2 = 59
        for byte in key.to_bytes((key.bit_length() + 7) // 8, 'little'):
            hash_value = hash_value * prime1 + byte + prime2
        return hash_value
        
    def primeBelow(self, n):
        n -= 1 if n % 2 == 0 else 2
        while (3 < n and not self.is_prime(n)):
            n -= 2
        return n
    
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def insert(self, key, value):
        if self.size == self.capacity:
            print("Hash Table is full")
            return
        index = self.hash(key)
        if self.keys[index] is None:
            self.keys[index] = key
            self.values[index] = value
            self.size += 1
        elif self.keys[index] == key:
            self.values[index] = value
        else:
            for i in self.doubleHashProbe(index, key):
                if self.keys[i] is None:
                    self.keys[i] = key
                    self.values[i] = value
                    self.size += 1
                    break
                elif self.keys[i] == key:
                    self.values[i] = value
                    break
                    
    def get(self, key):
        index = self.hash(key)
        for i in self.doubleHashProbe(index, key):
            if self.keys[i] == key:
                return self.values[i]
            elif self.keys[i] is None:
                return None
        return None

# Prueba
table = HashTable()
print("Insertando 20 claves seleccionadas aleatoriamente del rango [0, 99999]:")
print("{:<10} {:<20} {:<20} {:<20}".format("Key", "Dirección cifrada", "Módulo con Prime", "Secuencia de sonda"))
print("{:<10} {:<20} {:<20} {:<20}".format("---", "--------------", "----------------", "-------------"))
for i in range(20):
    key = random.randint(0, 99999)
    hashed_address = table.hash(key)
    prime = table.primeBelow(table.capacity)
    step = table.doubleHashStep(key)
    modulo_prime = hashed_address % prime
    probe_sequence = [str(j) for j in table.doubleHashProbe(hashed_address, key)]
    probe_sequence_str = '->'.join(probe_sequence)
    table.insert(key, i)
    print("{:<10} {:<20} {:<20} {:<20}".format(key, hashed_address, modulo_prime, probe_sequence_str))
