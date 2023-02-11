import Array
import builtins
maxSize = 10 # Tamaño máximo de la matriz
arr = Array.Array(maxSize) # Crear un objeto de matriz
arr.insert(77) #  Insertar 10 elementos
arr.insert(99)
arr.insert(13)
arr.insert(20)
arr.insert(44)
arr.insert(20)
arr.insert(12.34)
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


#AGREGADO EJERCICIO 2.3
print("El arreglo ordenado de mayor a menor:")
maxSize2 = 10 # Tamaño máximo de la matriz nueva
arr2 = Array.Array(maxSize2) # Crear un objeto de matriz nuevo

n = len(arr)-1 # n = posicion final del segmento a tratar, comienza en len(lista)-1*
while n > 0: # ciclo mientras haya elementos para ordenar (2 o más elementos)
    p = arr.getMaxNum() # p es la posicion del mayor valor del segmento
    arr2.insert(p)
    arr.delete(p)
    n = n - 1 # reduce el segmento en 1

arr2.traverse()

#print("El arreglo ordenado de menor a mayor:")

