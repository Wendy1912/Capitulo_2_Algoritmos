# A program to reverse the letters of a word
from SimpleStack import *

stack = Stack(100) # Create a stack to hold letters
pa = input("Palabra a invertir: ")

for let in pa: # Loop over letters in word
    if not stack.isFull(): # Push letters on stack if not full
        stack.push(let)

reverb = '' # Build the reversed version

while not stack.isEmpty(): # by popping the stack until empty
    reverb += stack.pop()

print('El inverso de ', pa, 'es', reverb)


clean_word = ''.join(e.lower() for e in pa if e.isalpha())

for let in clean_word: # Loop over letters in word
    if not stack.isFull(): # Push letters on stack if not full
        stack.push(let)

reverb = '' # Build the reversed version

while not stack.isEmpty(): # by popping the stack until empty
    reverb += stack.pop()

# Check if the reversed word is equal to the original word
if clean_word == reverb:
    print(pa, 'es un palíndromo.')
else:
    print(pa, 'no es un palíndromo.')
