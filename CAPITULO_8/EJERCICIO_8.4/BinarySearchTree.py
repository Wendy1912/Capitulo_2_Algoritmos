class BinarySearchTree:
    class _Node:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
    
    def __init__(self):
        self._root = None
    
    def insert(self, key, value=None):
        def _insert_recursive(node, key, value):
            if node is None:
                return BinarySearchTree._Node(key, value)
            
            if key < node.key:
                node.left = _insert_recursive(node.left, key, value)
            elif key > node.key:
                node.right = _insert_recursive(node.right, key, value)
            else:
                node.value = value
            
            return node
        
        self._root = _insert_recursive(self._root, key, value)
    
    def nodeBalance(self, node=None):
        if node is None:
            node = self._root
        
        def _node_balance_recursive(node):
            if node is None:
                return 0
            
            return _node_balance_recursive(node.right) - _node_balance_recursive(node.left)
        
        return _node_balance_recursive(node)
    
    def levelBalance(self, node=None):
        if node is None:
            node = self._root
        
        def _level_balance_recursive(node):
            if node is None:
                return 0
            
            return _level_balance_recursive(node.right) - _level_balance_recursive(node.left)
        
        return _level_balance_recursive(node)
    
    def _unbalanced_nodes_recursive(self, node, by, result):
        if node is None:
            return 0
        
        node_balance = self.nodeBalance(node)
        level_balance = self.levelBalance(node)
        
        if abs(node_balance) > by or abs(level_balance) > by:
            result.append(node.key)
        
        self._unbalanced_nodes_recursive(node.left, by, result)
        self._unbalanced_nodes_recursive(node.right, by, result)
    
    def unbalancedNodes(self, by=1):
        result = []
        self._unbalanced_nodes_recursive(self._root, by, result)
        return result
    
    def printTree(self, node=None, level=0):
            if node is None:
                node = self._root

            if node.right is not None:
                self.printTree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.key)
            if node.left is not None:
                self.printTree(node.left, level + 1)