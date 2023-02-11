from OrderedRecordArray import *

maxSize = 11                  # Max size of the array
arr = OrderedRecordArray(maxSize)   # Create the array object

arr.insert(77)                # Insert maxSize items
arr.insert(99)
arr.insert(44)                # Inserts not in order
arr.insert(55)
arr.insert(0)
arr.insert(12)
arr.insert(44)
arr.insert(99)
arr.insert(77)
arr.insert(0)
arr.insert(3)

print("Array containing", len(arr), "items:", arr)
   
arr.delete(0)                 # Delete a few items
arr.delete(99)
arr.delete(0)                 # Duplicate deletes
arr.delete(0)
arr.delete(3)

print("La matriz después de las eliminaciones ha", len(arr), "items:", arr)

print("find(44) returns", arr.find(44))
print("find(46) returns", arr.find(46))
print("find(77) returns", arr.find(77))

while len(arr) <= maxSize:    # Rellenar y luego desbordar la matriz
   try:
      arr.insert(len(arr))    # Inserta la longitud de la matriz
      print("Después de la inserción, la matriz tiene", len(arr), "items")
   except Exception as e:
      print("Intenta insertar", len(arr), "fallido")
      print("matriz contiene:", arr)
      print(e)
      break
