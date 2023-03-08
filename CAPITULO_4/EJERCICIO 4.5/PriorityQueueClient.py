from PriorityQueue import *

def first(x): return x[0]  # Use first element of item as priority

priority = PriorityQueue(5)
priority.insert(8)
priority.insert(6)
priority.insert(3)
priority.insert(9)
priority.insert(1)
print("Contenido de la PriorityQueue: ", priority)

print("Removing:", priority.remove())
print("Contenido de la PriorityQueue: ", priority)


print("Ultimo elemento de la lista: ", priority.peek())


print("¿La lista esta vacía? ", priority.isEmpty())


print("¿La lista esta llena? ", priority.isFull())
