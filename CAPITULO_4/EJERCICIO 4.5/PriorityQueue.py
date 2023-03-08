# Implement a Priority Queue data structure using a Python list

def identity(x):  return x            # Identity function

class PriorityQueue(object):
   def __init__(self, size, pri=identity):
      self.__maxSize = size
      self.__que = []              # Cola de prioridad almacenada como una lista
      self.__indices = {}          # Diccionario para almacenar índices de elementos
      self.__pri = pri
      self.__nItems = 0

   def insert(self, item):
      if self.isFull():
         raise Exception("Desbordamiento de cola")
      self.__que.append(item)      # Agregar elemento al final de la lista
      self.__indices[item] = len(self.__que) - 1 #Almacenar el índice del artículo
      self.__nItems += 1
      return True

   def remove(self):
      if self.isEmpty():
         raise Exception("Subdesbordamiento de la cola")
      maxItem = max(self.__que, key=self.__pri)  # Buscar elemento con mayor prioridad
      maxIndex = self.__indices[maxItem]         # Obtener el índice del artículo máximo
      del self.__indices[maxItem]                # Eliminar elemento del dictado de índice
      del self.__que[maxIndex]                   # Remove item from queue list
      self.__nItems -= 1
      return maxItem

   def peek(self):
      return None if self.isEmpty() else max(self.__que, key=self.__pri)

   def isEmpty(self):
      return self.__nItems == 0

   def isFull(self):
      return self.__nItems == self.__maxSize

   def __len__(self):
      return self.__nItems

   def __str__(self):
      return str(self.__que)