# Automated tests of the BinarySearchTree class

from BinarySearchTree import *
import sys

# crear el árbol
tree = BinarySearchTree()

# insertar claves duplicadas con diferentes valores
tree.insert(10, "valor1")
tree.insert(5, "valor2")
tree.insert(15, "valor3")
tree.insert(10, "valor4")
tree.insert(10, "valor5")
tree.insert(15, "valor6")

tree.print()

# eliminar claves duplicadas
tree.delete(10)
tree.delete(15)
tree.delete(10)

# imprimir los valores de las claves restantes
print(tree.search(5))   # debe imprimir "valor2"
print(tree.search(10))  # debe imprimir "valor5"
print(tree.search(15))  # debe imprimir "valor6"