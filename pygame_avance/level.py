import pygame, sys
from tiles import * 
from settings import *
from player import *


class Level:
	def __init__(self,level_data,surface):

		# Creacion de la pantalla
		self.screen = pygame.display.set_mode((screen_width,screen_height))

		# Configuracion de nivel 
		self.display_surface = surface 
		self.configuracion_nivel(level_data)
		self.world_shift = 0
		self.current_x = 0

		self.player_on_ground = False

	def get_player_on_ground(self):

		#Verifica si el jugador esta encima del mosaico(bloque)
		if self.player.sprite.on_ground:
			self.player_on_ground = True
		else:
			self.player_on_ground = False


	def configuracion_nivel(self,layout):
		self.tiles = pygame.sprite.Group()
		self.player = pygame.sprite.GroupSingle()
		
		for row_index,row in enumerate(layout):
			for col_index,cell in enumerate(row):
				x = col_index * tile_size
				y = row_index * tile_size
				
				"""Segun las letras que esten en level_map, ahi se van poniendo los bloques"""

				if cell == 'X':
					tile = Tile((x,y),tile_size, color_mosaico)
					self.tiles.add(tile)
				if cell == 'P':
					player_sprite = Player((x,y),self.display_surface)
					self.player.add(player_sprite)
				if cell == "Y":
					tile = Tile((x,y),tile_size, otro_color)
					self.tiles.add(tile)
					
			 
	def camara(self):
		player = self.player.sprite
		player_x = player.rect.centerx
		direction_x = player.direccion.x

		if player_x < screen_width / 4 and direction_x < 0:
			self.world_shift = 8
			player.velocidad = 0
		elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
			self.world_shift = -8
			player.velocidad = 0
		else:
			self.world_shift = 0
			player.velocidad = 8

	def colision_horizontal(self):
		player = self.player.sprite
		player.rect.x += player.direccion.x * player.velocidad

		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.direccion.x < 0: 
					player.rect.left = sprite.rect.right
					player.on_left = True
					self.current_x = player.rect.left
				elif player.direccion.x > 0:
					player.rect.right = sprite.rect.left
					player.on_right = True
					self.current_x = player.rect.right

		if player.on_left and (player.rect.left < self.current_x or player.direccion.x >= 0):
			player.on_left = False
		if player.on_right and (player.rect.right > self.current_x or player.direccion.x <= 0):
			player.on_right = False

	def colision_vertical(self):
		player = self.player.sprite
		player.apply_gravity()

		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.direccion.y > 0: 
					player.rect.bottom = sprite.rect.top
					player.direccion.y = 0
					player.on_ground = True
				elif player.direccion.y < 0:
					player.rect.top = sprite.rect.bottom
					player.direccion.y = 0
					player.on_ceiling = True

		if player.on_ground and player.direccion.y < 0 or player.direccion.y > 1:
			player.on_ground = False
		if player.on_ceiling and player.direccion.y > 0.1:
			player.on_ceiling = False

	def mensaje_pantalla(self, mensaje, color, tamaño, posicion):
		
		# Muestra un mensaje en pantalla en la posicion que se le indique

		self.fuente = pygame.font.SysFont(None, tamaño)
		self.texto = self.fuente.render(mensaje, True, color)
		self.screen.blit(self.texto, posicion)


	def run(self, activo=False):

		if activo == True:
			# Mosaicos del nivel
			self.tiles.update(self.world_shift)
			self.tiles.draw(self.display_surface)
			self.camara()
			# Jugador
			self.player.update()
			self.colision_horizontal()
			self.get_player_on_ground()
			self.colision_vertical()
			self.player.draw(self.display_surface)
			self.mensaje_pantalla("[ En linea ]", color_letra, 25, (5, 5) )
		