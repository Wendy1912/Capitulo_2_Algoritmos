class OrderedRecordArray(object):
    
    def find(self, key): # Encuentra el índice en o justo debajo de ke
        lo = 0 # en lista ordenada
        hi = self.__nItems-1 # Buscar entre lo y hi
        while lo <= hi:
            mid = (lo + hi) // 2 # Selecciona el punto medio
            if self.__key(self.__a[mid]) == key: # ¿Lo encontramos?
                return mid # Ubicación de devolución del artículo
            elif self.__key(self.__a[mid]) < key: # ¿Está key en la mitad superior?
                lo = mid + 1 # Sí, eleva el límite lo
            else:
                hi = mid - 1 # No, pero podría estar en la mitad inferior
                return lo # Elemento no encontrado, devuelve el punto de inserción en su lugar
        
    def search(self, key):
        idx = self.find(key) # Busca un registro por su clave
        if idx < self.__nItems and self.__key(self.__a[idx]) == key:
            return self.__a[idx] # y devolver el artículo si lo encuentra
    
    def insert(self, item): # Insertar elemento en la posición correcta
        if self.__nItems >= len(self.__a): # Si la matriz está llena,
            raise Exception("Array overflow") # generar excepción
        j = self.find(self.__key(item)) # Encuentra dónde debe ir el elemento
        for k in range(self.__nItems, j, -1): # Mover elementos más grandes a la derecha
            self.__a[k] = self.__a[k-1]
            self.__a[j] = item # Insertar el artículo
            self.__nItems += 1 # Incrementa el número de elementos
    
    def delete(self, item): # Eliminar cualquier ocurrencia
        j = self.find(self.__key(item))  # Intenta encontrar el item
        if j < self.__nItems and self.__a[j] == item: # Si se encuentra,
            self.__nItems -= 1 # Uno menos al final
            for k in range(j, self.__nItems): # Mover elementos más grandes a la izquierda
                self.__a[k] = self.__a[k+1]
                return True # Devuelve el indicador de éxito
            return False # Hecho aquí; objeto no encontrado
        
    #AGREGADO EJERCICIO 2.5
    def merge(self, item): # Eliminar cualquier ocurrencia
        j = self.find(self.__key(item))  # Intenta encontrar el item
        if j < self.__nItems and self.__a[j] == item: # Si se encuentra,
            self.__nItems -= 1 # Uno menos al final
            for k in range(j, self.__nItems): # Mover elementos más grandes a la izquierda
                self.__a[k] = self.__a[k+1]
                return True # Devuelve el indicador de éxito
            return False # Hecho aquí; objeto no encontrado