# Implemente una estructura de datos de matriz como un tipo simplificado de lista.

class Array(object):
    def __init__(self, initialSize): # Constructor
        self.__a = [None] * initialSize # La matriz almacenada como una lista
        self.__nItems = 0 # No hay elementos en la matriz inicialmente
        
    def __len__(self): # Definición especial para len() funcion
        return self.__nItems # Número de devolución de artículos
    
    def get(self, n): # Devuelve el valor en el índice n
        if 0 <= n and n < self.__nItems:  # Comprobar si n está dentro de los límites, y
            return self.__a[n] # solo devolver el artículo si está en límites
        
    def set(self, n, value): # Establecer el valor en el índice n
        if 0 <= n and n < self.__nItems: # Comprobar si n está dentro de los límites, y
            self.__a[n] = value # solo establece el elemento si está en límites
            
    def insert(self, item): # Insertar elemento al final
        self.__a[self.__nItems] = item # El artículo va al final actual
        self.__nItems += 1 # Incrementar el número de elementos
        
    def find(self, item): # Buscar índice para el artículo
        for j in range(self.__nItems): # Entre los artículos actuales
            if self.__a[j] == item: # Si se encuentra,
                return j # luego devuelve el índice al artículo
        return -1 # No encontrado -> devuelve -1
    
    def search(self, item): # Buscar artículo
        return self.get(self.find(item)) # y devolver el artículo si lo encuentra
    
    def delete(self, item): # Eliminar la primera ocurrencia
        for j in range(self.__nItems): # de un artículo
            if self.__a[j] == item: # Elemento encontrado
                self.__nItems -= 1 # Uno menos al final
                for k in range(j, self.__nItems): # Mover elementos de
                    self.__a[k] = self.__a[k+1] # justo sobre 1
                return True # Devuelve la bandera de éxito
            
        return False # Lo hice aquí, así que no pude encontrar el artículo
    
    def traverse(self, function=print): # Recorrer todos los elementos
        for j in range(self.__nItems): # y aplicar una función
            function(self.__a[j])
            
    #AGREGADO EJERCICIO 2.1     
    def  getMaxNum(self): #devuelve el valor del número más alto 
        max = self.__a[0];
        for x in self.__a:
            if x > max:
                max = x
        return max 

    #AGREGADO EJERCICIO 2.2
    def deleteMaxNum(self): #elimina el valor numérico más alto
        max = self.__a[0];
        for x in self.__a:
            if x > max:
                max = x
        #return max 
        for j in range(self.__nItems): # de un artículo
                if self.__a[j] == max: # Elemento encontrado
                    self.__nItems -= 1 # Uno menos al final
                    for k in range(j, self.__nItems): # Mover elementos de
                        self.__a[k] = self.__a[k+1] # justo sobre 1
                    return True # Devuelve la bandera de éxito
                
        return False 
    
    