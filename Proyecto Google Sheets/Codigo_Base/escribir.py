from sortclass import *
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import random
import timeit

#Para sincronizar con Google sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'C:/Users/user/Documents/googlesheets/clave.json'
SPREADSHEET_ID = '1en596aFjos16WjIcgT6u7kBXbNxEAHIrhMtK6MxGCJ8'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

def initArray(size=6, maxValue=30, seed=3.14159):
    lista = Array(size)                   
    random.seed(seed)                   
    for i in range(size):              
        lista.insert(random.randrange(maxValue)) 
    return lista                          

lista = initArray()
for test in ['initArray().bubbleSort()',
             'initArray().selectionSort()',
             'initArray().insertionSort()']:
    elapsed = timeit.timeit(test, number=4, globals=globals())
    print(test, "took", elapsed, "seconds", flush=True)


#Random list
lista.traverse()
print('La matriz desordenada contiene:\n', lista)
NuevaLista = [[lista.get(i)] for i in range(len(lista))]
range_ ='A1:A7' 
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range_,
							valueInputOption='USER_ENTERED',
							body={'values':NuevaLista}).execute()
print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")



#Bubblesort
lista.bubbleSort()
print('Agregado Bubble Sort')
NuevaLista = [[lista.get(i)] for i in range(len(lista))]
range2_ ='B1:B7' 
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range2_,
							valueInputOption='USER_ENTERED',
							body={'values':NuevaLista}).execute()
print(f"Datos insertados de Bubble.\n{(result.get('updates').get('updatedCells'))}")

#insertion sort
lista.insertionSort()
print('Agregado Insertion sort')
NuevaLista = [[lista.get(i)] for i in range(len(lista))]
range4_ ='D1:D7' 
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range4_,
							valueInputOption='USER_ENTERED',
							body={'values':NuevaLista}).execute()
print(f"Datos insertados de insertion.\n{(result.get('updates').get('updatedCells'))}")

#selection sort
lista.selectionSort()
print('Agregado Insertion sort')
NuevaLista = [[lista.get(i)] for i in range(len(lista))]
range3_ ='C1:C7' 
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range3_,
							valueInputOption='USER_ENTERED',
							body={'values':NuevaLista}).execute()
print(f"Datos insertados de Selection.\n{(result.get('updates').get('updatedCells'))}")






