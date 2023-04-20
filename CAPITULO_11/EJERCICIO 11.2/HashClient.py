import random
from HashTable import *

# Crear las dos tablas hash con sondeo lineal y recuento de claves desplazadas
table_3 = HashTable(1000)
table_2 = HashTable(1000)

# Generar mil enteros aleatorios de 10 dígitos
random_ints = random.sample(range(10000000000), 1000)

# Insertar los enteros en las tablas hash
for num in random_ints:
    table_3.insert(num, None)
    table_2.insert(num, None)

# Mostrar los recuentos de claves desplazadas para los factores de carga máximos
load_factors = [0.5, 0.7, 0.9]

for lf in load_factors:
    table_3.reset_displacements()
    table_3.set_max_load_factor(lf)
    for num in random_ints:
        table_3.insert(num, None)
    print(f"Función hash con grupos de 3 dígitos y factor de carga máximo de {lf}: {table_3.get_displacements()} desplazamientos")

    table_2.reset_displacements()
    table_2.set_max_load_factor(lf)
    for num in random_ints:
        table_2.insert(num, None)
    print(f"Función hash con grupos de 2 dígitos y factor de carga máximo de {lf}: {table_2.get_displacements()} desplazamientos")
