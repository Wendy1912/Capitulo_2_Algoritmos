import random
from HashTable import *

random.seed(42)

keys = random.sample(range(1000), 200)

max_load_factors = [0.5, 0.7, 0.9]
probe_schemes = [HashTable.linear_probe, HashTable.quadratic_probe, HashTable.double_hash]

for max_load_factor in max_load_factors:
    for probe_scheme in probe_schemes:
        print(f"Factor de carga máximo: {max_load_factor}, Esquema de sonda: {probe_scheme.__name__}")
        for i in range(5):
            ht = HashTable(103)
            for key in keys:
                ht.insert(key, key)
            displaced_keys = ht.find_displaced_keys()
            print(f"Iteración {i+1}: {len(displaced_keys)} claves desplazadas")
            ht.print_table()
        print()
