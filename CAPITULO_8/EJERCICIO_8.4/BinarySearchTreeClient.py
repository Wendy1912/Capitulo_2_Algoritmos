from BinarySearchTree import BinarySearchTree

bst = BinarySearchTree()

keys_list = [    
    [7, 6, 5, 4, 3, 2, 1, 8, 12, 10, 9, 11, 14, 13, 15],
    [8, 4, 5, 6, 7, 3, 2, 1, 12, 10, 9, 11, 14, 13, 15],
    [8, 4, 2, 3, 1, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15],
    [8, 4, 2, 3, 1, 6, 5, 7, 12, 10, 9, 11, 14, 13, 8.5]
]

for keys in keys_list:
    for key in keys:
        bst.insert(key)

print("Tree:")
bst.printTree()

root_node = bst._root

print("Equilibrio de nodos del nodo raíz:", bst.nodeBalance(root_node))
print("Equilibrio de nivel del nodo raíz:", bst.levelBalance(root_node))
print("Nodos desequilibrados (by=1):", bst.unbalancedNodes(1))
print("Nodos desequilibrados (by=2):", bst.unbalancedNodes(2))


