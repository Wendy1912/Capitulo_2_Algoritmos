class Deque(object):
    def __init__(self, size):
        self.items = [None] * size
        self.primer = 0
        self.ultimo = 0
        self.size = size
        
    def insertLeft(self, item):
        if self.isFull():
            raise Exception('Deque is full')
        self.primer = (self.primer - 1) % self.size
        self.items[self.primer] = item
    
    """def insertRight1(self, item):
        if self.isFull():
            raise Exception('Deque is full')
        self.items[self.ultimo] = item
        self.ultimo = (self.ultimo + 1) % self.size
    """
    def insertRight2(self, item): #Para admitir el ajuste al final de la matriz
        if self.isFull():
            self.resize1(2 * self.size)  # Duplica el tamaño de la deque
        self.items[self.ultimo] = item
        self.ultimo = (self.ultimo + 1) % self.size
    
    def resize1(self, new_size):
        old_items = self.items
        self.items = [None] * new_size
        for i in range(self.size):
            self.items[i] = old_items[(self.primer + i) % self.size]
        self.primer = 0
        self.ultimo = self.size
        self.size = new_size


    def removeLeft1(self):
        if self.isEmpty():
            raise Exception('Deque is empty')
        item = self.items[self.primer]
        self.items[self.primer] = None
        self.primer = (self.primer + 1) % self.size
        return item
    
    """def removeLeft2(self): #Para admitir el ajuste al final de la matriz
        if self.isEmpty():
            raise Exception('Deque is empty')
        item = self.items[self.primer]
        self.items[self.primer] = None
        self.primer = (self.primer + 1) % self.size
        # verificar si deque está a menos de 1/4 de su capacidad y cambiar
        #  el tamaño si es necesario
        if self.size > 4 and (self.ultimo - self.primer) < self.size // 4:
            self.resize2(self.size // 2)
        return item

    def resize2(self, new_size): 
        #reducir el tamaño de la matriz a la mitad y copiar los
        #elementos existentes en la nueva matriz
        old_items = self.items
        self.items = [None] * new_size
        for i in range(self.size):
            self.items[i] = old_items[(self.primer + i) % self.size]
        self.primer = 0
        self.ultimo = self.size
        self.size = new_size """
    def removeRight(self):
        if self.isEmpty():
            raise Exception('Deque is empty')
        self.ultimo = (self.ultimo - 1) % self.size
        item = self.items[self.ultimo]
        self.items[self.ultimo] = None
        return item

    def peekLeft(self):     #Devuelve el elemento más a la izquierda
        if self.isEmpty():
            raise Exception('Deque is empty')
        return self.items[self.primer]

    def peekRight(self):    ##Devuelve el elemento más a la derecha
        if self.isEmpty():
            raise Exception('Deque is empty')
        return self.items[self.ultimo - 1]

    def isEmpty(self):
        return self.primer == self.ultimo and self.items[self.primer] is None

    def isFull(self):
        return self.primer == self.ultimo and self.items[self.primer] is not None