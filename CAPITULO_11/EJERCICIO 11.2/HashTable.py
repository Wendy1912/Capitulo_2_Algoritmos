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
    
    def reset_displacements(self):
            self.displacements = 0

    def set_max_load_factor(self, factor):
        #Establece el factor de carga máximo para la tabla hash.
        self.max_load_factor = factor

    def get_displacements(self):
        return self.displacements

    def print_table(self):
        # Método para imprimir ls tablas
        print("Tabla hash:")
        for i in range(self.size):
            print(f"{i}: {self.keys[i]}, {self.values[i]}")
        
    #Agregado para el ejercicio 11.2
    def hash_function_3(self, num, size):
        # Plegar el número en grupos de 3 dígitos
        num_str = str(num)
        num_len = len(num_str)
        num_groups = [int(num_str[i:i+3]) for i in range(0, num_len, 3)]
        
        # Sumar los grupos y devolver el valor hash
        hash_value = sum(num_groups)
        return hash_value % size

    def hash_function_2(self, num, size):
        # Plegar el número en grupos de 2 dígitos
        num_str = str(num)
        num_len = len(num_str)
        num_groups = [int(num_str[i:i+2]) for i in range(0, num_len, 2)]
        
        # Sumar los grupos y devolver el valor hash
        hash_value = sum(num_groups)
        return hash_value % size

    