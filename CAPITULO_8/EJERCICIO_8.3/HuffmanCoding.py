import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, value=None, freq=0):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq

class HuffmanTree:
    def __init__(self, message):
        self.message = message
        self.tree = None
        self.codes = {}
    
    def _create_frequency_table(self):
        frequency_table = defaultdict(int)
        for char in self.message:
            frequency_table[char] += 1
        return frequency_table
    
    def _create_tree(self, frequency_table):
        priority_queue = []
        for key, value in frequency_table.items():
            node = HuffmanNode(key, value)
            heapq.heappush(priority_queue, node)
        
        while len(priority_queue) > 1:
            left_child = heapq.heappop(priority_queue)
            right_child = heapq.heappop(priority_queue)
            
            new_node = HuffmanNode(None, left_child.freq + right_child.freq)
            new_node.left = left_child
            new_node.right = right_child
            
            heapq.heappush(priority_queue, new_node)
        
        return priority_queue[0]
    
    def _create_codes(self, node, current_code=""):
        if node.value is not None:
            self.codes[node.value] = current_code
        else:
            self._create_codes(node.left, current_code + "0")
            self._create_codes(node.right, current_code + "1")
    
    def _encode_message(self):
        encoded_message = ""
        for char in self.message:
            encoded_message += self.codes[char]
        return encoded_message
    
    def _decode_message(self, encoded_message):
        decoded_message = ""
        current_code = ""
        reverse_codes = {v: k for k, v in self.codes.items()}
        for bit in encoded_message:
            current_code += bit
            if current_code in reverse_codes:
                decoded_message += reverse_codes[current_code]
                current_code = ""
        return decoded_message
    
    def build(self):
        frequency_table = self._create_frequency_table()
        self.tree = self._create_tree(frequency_table)
        self._create_codes(self.tree)
    
    def encode(self):
        encoded_message = self._encode_message()
        return encoded_message
    
    def decode(self, encoded_message):
        decoded_message = self._decode_message(encoded_message)
        return decoded_message
    
    def display_tree(self):
        if len(self.message) > 10:
            print("El mensaje es demasiado largo para mostrar el árbol.")
            return
        def traverse(node, level=0):
            if node is None:
                return
            traverse(node.right, level+1)
            print(" "*4*level + "->", node.freq, node.value)
            traverse(node.left, level+1)
        traverse(self.tree)

