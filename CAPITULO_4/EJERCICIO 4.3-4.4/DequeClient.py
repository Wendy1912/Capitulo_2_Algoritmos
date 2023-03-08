# importar la clase Deque
from Deque import Deque

# crear un objeto Deque con tamaño 5
d = Deque(5)

# insertar elementos por la derecha
d.insertRight2(1)
d.insertRight2(2)
d.insertRight2(3)

# insertar elementos por la izquierda
d.insertLeft(4)
d.insertLeft(5)

#Insertar mas elementos de los que permite
d.insertRight2(6)

# mostrar el contenido del Deque
print("Contenido del Deque:")
while not d.isEmpty():
    print(d.removeLeft1())

# insertar elementos por la derecha
d.insertRight2(6)
d.insertRight2(7)
d.insertRight2(8)

# mostrar el contenido del Deque
print("Contenido del Deque:")
while not d.isEmpty():
    print(d.removeLeft1())