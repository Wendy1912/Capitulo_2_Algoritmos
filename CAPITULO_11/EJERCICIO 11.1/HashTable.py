class HashTable:
    def __init__(self, size):
        # Inicialización del objeto HashTable con una lista de claves y otra de valores vacías
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        # Función hash que utiliza el módulo del tamaño de la tabla para obtener el índice de la clave
        return key % self.size

    def linear_probe(self, index):
        # Esquema de sonda lineal que simplemente avanza al siguiente índice en la tabla
        return (index + 1) % self.size

    def quadratic_probe(self, index, i):
        # Esquema de sonda cuadrático que utiliza un cálculo matemático para avanzar al siguiente índice
        return (index + i*i) % self.size

    def double_hash(self, index, key):
        # Esquema de sonda de doble hash que utiliza dos funciones hash para obtener el siguiente índice
        return (index + 2*self.hash_function(key) + 1) % self.size

    def insert(self, key, value):
        # Método para insertar una clave y su valor en la tabla
        index = self.hash_function(key)
        i = 0
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            i += 1
            if i == self.size:
                print("Error: tabla llena")
                return
            index = self.linear_probe(index)
            #index = self.quadratic_probe(index, i)
            #index = self.double_hash(index, key)
        self.keys[index] = key
        self.values[index] = value
        
    def find_displaced_keys(self):
        # Método para encontrar todas las claves que no están en su posición hash inicial debido a colisiones
        displaced_keys = []
        for i in range(self.size):
            if self.keys[i] is not None and self.hash_function(self.keys[i]) != i:
                displaced_keys.append(self.keys[i])
        return displaced_keys # Devuelve una lista de claves desplazadas

    def print_table(self):
        # Método para imprimir ls tablas
        print("Tabla hash:")
        for i in range(self.size):
            print(f"{i}: {self.keys[i]}, {self.values[i]}")
