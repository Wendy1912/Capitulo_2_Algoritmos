from SortArray import *
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import random
import timeit

#Para sincronizar con Google sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
SPREADSHEET_ID = '1en596aFjos16WjIcgT6u7kBXbNxEAHIrhMtK6MxGCJ8'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

def initArray(size=4, maxValue=10, seed=3.14159):
    """Create an Array of the specified size with a fixed sequence of
       'random' elements"""
    arr = Array(size)                   # Create the Array object
    random.seed(seed)                   # Set random number generator
    for i in range(size):               # to known state, then loop
        arr.insert(random.randrange(maxValue)) # Insert random numbers
    return arr                          # Return the filled Array

arr = initArray()
print("Array containing", len(arr), "items:\n", arr)

for test in ['initArray().bubbleSort()',
             'initArray().selectionSort()',
             'initArray().insertionSort()']:
    elapsed = timeit.timeit(test, number=4, globals=globals())
    print(test, "took", elapsed, "seconds", flush=True)


#LISTA NORMAL
arr.traverse()
print('La matriz desordenada contiene:\n', arr)

# Convertir el arreglo a una lista de listas con un elemento por sublista
values = [[arr.get(i)] for i in range(len(arr))]

# Especificar la dirección de la celda para cada valor
range_ ='A' + str(len(arr)-2)

# Llamamos a la api para insertar los valores
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range_,
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")


"""
#BUBBLE
arr.bubbleSort()
print('La matriz ordenada por bubbleSort contiene:\n', arr)

# Convertir el arreglo a una lista de listas con un elemento por sublista
values = [[arr.get(i)] for i in range(len(arr))]

# Especificar la dirección de la celda para cada valor
range2_ ='B' + str(len(arr)-2)

# Llamamos a la api para insertar los valores
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range2_,
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")
"""

"""
#SELECTION
arr.selectionSort()
print('La matriz ordenada por selectionSort contiene:\n', arr)

# Convertir el arreglo a una lista de listas con un elemento por sublista
values = [[arr.get(i)] for i in range(len(arr))]

# Especificar la dirección de la celda para cada valor
range3_ ='C' + str(len(arr)-2)

# Llamamos a la api para insertar los valores
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range3_,
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")
"""

"""
#INSERTION
arr.insertionSort()
print('La matriz ordenada por nsertionSort contiene:\n', arr)

# Convertir el arreglo a una lista de listas con un elemento por sublista
values = [[arr.get(i)] for i in range(len(arr))]

# Especificar la dirección de la celda para cada valor
range4_ ='D' + str(len(arr)-2)

# Llamamos a la api para insertar los valores
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range4_,
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")
"""

