import pygame
from settings  import* 

class Tile(pygame.sprite.Sprite):
	# Crea los mosaicos o bloques, segun la letra en level_map en settings.py
	def __init__(self,pos,size,color_mosaico):
		super().__init__()
		self.image = pygame.Surface((size,size))
		self.image.fill(color_mosaico)
		self.rect = self.image.get_rect(topleft = pos)
		

	def update(self,x_shift):
		self.rect.x += x_shift