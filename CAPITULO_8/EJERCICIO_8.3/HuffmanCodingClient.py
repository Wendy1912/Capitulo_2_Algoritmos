from HuffmanCoding import *
import sys
# Example usage:
message = "ejemplo"
huffman_tree = HuffmanTree(message)
huffman_tree.build()
huffman_tree.display_tree()
encoded_message = huffman_tree.encode()
decoded_message = huffman_tree.decode(encoded_message)
print("Mensaje original:", message)
print("Mensaje codificado:", encoded_message)
print("Mensaje decodificado:", decoded_message)
print("Número de bits en el mensaje codificado:", len(encoded_message))
print("Número de caracteres en el mensaje original:", len(message))
