from HashTable import *
import random

# Función para generar 200 números aleatorios del 0 al 999 sin repetición
def generate_random_numbers():
    return random.sample(range(1000), 200)

# Función para probar la tabla hash con diferentes cargas y sondas
def test_hashtable(load_factor, probe):
    table = HashTable(size=128)
    table.max_load_factor = load_factor
    keys = generate_random_numbers()
    for key in keys:
        table[key] = key
    displaced = table.get_displaced_keys(probe)
    print(f"Factor de carga: {load_factor}, Sondas: {probe}")
    if displaced is not None:
        print(f"Número de llaves desplazadas: {len(displaced)}")
    else:
        print("No se pueden insertar todas las claves")

# Pruebas de la tabla hash con diferentes cargas y sondas
load_factors = [0.5, 0.7, 0.9]
probes = [1, 2, 3]
for load_factor in load_factors:
    for probe in probes:
        test_hashtable(load_factor, probe)
