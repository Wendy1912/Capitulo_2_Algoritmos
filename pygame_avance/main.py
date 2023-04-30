import pygame, sys
from settings import * 
from level import Level

"""Ejecutar este archivo para ejecutar el juego"""

"""Nota si se quiere cambiar el color de algo dentro del juego verificar el archivo
settings.py, ahi se especifican algunas configuraciones en general."""

"""Teclas de movimiento: [a, s, w, d]"""

#Configuracion de la ventana de juego
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)

# Agrega la musica principal 
pygame.mixer.init()
pygame.mixer.music.load("musica/Goetia.mp3")
pygame.mixer.music.play(-1)

# Creacion de pantalla de inicio 
def pantalla_inicio (start, screen):
	menu_imagen = pygame.image.load("menu_final.png")
	screen.blit(menu_imagen, (-350,0))
	pygame.display.update()
	#if activo == True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			
		elif event.type == pygame.KEYDOWN:
			if event.key:
				return False
			
	return True	

# Inicializa el parametro start de pantalla_inicio para ejecutar la pantalla
start = True 

# Inicio del bucle del juego 
while True:

	#Ejecucion de la pantalla_inicio 
	while start:
		start = pantalla_inicio(start, screen)

	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# Ejecucion del juego 			
	screen.fill(color_fondo)
	manejo = True
	level.run(manejo)
	pygame.display.update()
	clock.tick(60)

