import pygame

level_map = [
'                            ',
'                            ',
'                            ',
'      XX  X                 ',
' X        X          XXX    ',
'XX     X  X                 ',
'XXX    XXXX     XXXX      XX',
'XXX                         ',
'XXXXXXXXXXXXXX         XXX  ',
'XXXXX             XX    XX  ',
'XXX         XX    XX    XX  ',
'X      X  XXXX        XXXX  ',
'XP  XXXX  XXXXXX     XXXXX  ',
'XXXXXXXX  XXXXXXXX XXXXXXX  ',
'YYYYYYYYYYYYYYYYYYYYYYYYYY  ']

#Ultimo indice 14, para posible funcion, ignorar
list = []
indice = 0 
for daño in range(len(level_map)):
    list.append(daño)
    indice += 1
    ultimo_indice = indice - 1
        


imagen = "mosaicos/agua.png"
tile_size = 64
screen_width = 1200
screen_height = 950 #len(level_map) * tile_size

color_fondo = "#03001C"
color_mosaico = "#B31E6F"

otro_color = "#1A5F7A"

color_letra = "#BFDB38"



