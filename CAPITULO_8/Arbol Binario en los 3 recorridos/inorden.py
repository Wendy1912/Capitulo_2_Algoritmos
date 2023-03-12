class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        
def recorrido_inorden(nodo):
    if nodo:
        recorrido_inorden(nodo.izquierda)
        print(nodo.valor)
        recorrido_inorden(nodo.derecha)
        
# Creamos el árbol binario con 15 elementos
raiz = Nodo(10)
raiz.izquierda = Nodo(6)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.izquierda.izquierda = Nodo(16)
raiz.izquierda.izquierda.derecha = Nodo(2)
raiz.izquierda.derecha = Nodo(12)
raiz.izquierda.derecha.izquierda = Nodo(19)
raiz.izquierda.derecha.derecha = Nodo(8)
raiz.derecha = Nodo(11)
raiz.derecha.izquierda = Nodo(14)
raiz.derecha.izquierda.izquierda = Nodo(5)
raiz.derecha.izquierda.derecha = Nodo(18)
raiz.derecha.derecha = Nodo(13)
raiz.derecha.derecha.izquierda = Nodo(15)
raiz.derecha.derecha.derecha = Nodo(7)

# Realizamos el recorrido inorden
recorrido_inorden(raiz)