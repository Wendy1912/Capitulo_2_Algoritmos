import Array
maxSize = 10 # Tamaño máximo de la matriz
arr = Array.Array(maxSize) # Crear un objeto de matriz
arr.insert(77) #  Insertar 10 elementos
arr.insert(99)
arr.insert(20)
arr.insert(20)
arr.insert(44)
arr.insert(20)
arr.insert(20.34)
arr.insert(0)
arr.insert(20)
arr.insert(-17)
print("Matriz que contiene", len(arr), "elementos")
arr.traverse()
print("Buscar 12 devoluciones", arr.search(12))
print("Buscar devoluciones 12.34", arr.search(12.34))
print("Eliminando 0 devoluciones", arr.delete(0))
print("Eliminando 17 devoluciones", arr.delete(17))
print("Configuración del elemento en el índice 3 a 33")
arr.set(3, 33)
print("La matriz después de las eliminaciones tiene", len(arr), "elementos")
arr.traverse()

#AGREGADO EJERCICIO 2.4 
print("El arreglo sin duplicados es:", arr.removeDupes())

