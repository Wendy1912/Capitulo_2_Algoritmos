import pygame 
from support import import_folder

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,surface):
		super().__init__()

		# Animaciones del jugador 
		self.import_anim_jugador()
		self.frame_index = 0
		self.velocidad_animacion = 0.20
		self.image = self.animaciones['inactivo'][self.frame_index]
		self.rect = self.image.get_rect(topleft = pos)
		
		# Movimiento del jugador
		self.direccion = pygame.math.Vector2(0,0)
		self.velocidad = 6
		self.gravedad = 0.8
		self.vel_salto = -16

		# Estado del jugador
		self.estado = 'inactivo'
		self.mirando_derecha = True
		self.on_ground = False
		self.on_ceiling = False
		self.on_left = False
		self.on_right = False

	def import_anim_jugador(self):
		character_path = '../pygame_avance/sprites/punk/'
		self.animaciones = {'inactivo':[],'correr':[],'saltar':[],'cayendo':[]}
		#Crea un diccionario para las animaciones del jugador con ayuda de => support.py

		for animation in self.animaciones.keys():
			full_path = character_path + animation
			self.animaciones[animation] = import_folder(full_path)

	def animar(self):
		animacion = self.animaciones[self.estado]

		# Bucle para controlar el indice de las animaciones 
		self.frame_index += self.velocidad_animacion
		if self.frame_index >= len(animacion):
			self.frame_index = 0

		image = animacion[int(self.frame_index)]
		if self.mirando_derecha:
			self.image = image
		else:
			flipped_image = pygame.transform.flip(image,True,False)
			self.image = flipped_image

		# Quita rectangulo que sobra 
		if self.on_ground and self.on_right:
			self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
		elif self.on_ground and self.on_left:
			self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
		elif self.on_ground:
			self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
		elif self.on_ceiling and self.on_right:
			self.rect = self.image.get_rect(topright = self.rect.topright)
		elif self.on_ceiling and self.on_left:
			self.rect = self.image.get_rect(topleft = self.rect.topleft)
		elif self.on_ceiling:
			self.rect = self.image.get_rect(midtop = self.rect.midtop)

	def get_input(self):

		# Teclas para el movimiento del jugador 
		# si se quiere cambiar una tecla seria: K_[la letra que se desee implementar]
		
		keys = pygame.key.get_pressed()

		if keys[pygame.K_d]:
			self.direccion.x = 1
			self.mirando_derecha = True
		elif keys[pygame.K_a]:
			self.direccion.x = -1
			self.mirando_derecha = False
		else:
			self.direccion.x = 0

		if keys[pygame.K_w] and self.on_ground:
			self.jump()

			# Agregar sonido de salto, al presionar la w, tecla de salto.
			sonido = pygame.mixer.Sound("musica/salto_final.wav")
			sonido.play()

		

	def get_status(self):

		#Se obtienen los estados del jugador para ir cambiando de animaciones 
		
		if self.direccion.y < 0:
			self.estado = 'saltar'
		elif self.direccion.y > 1:
			self.estado = 'cayendo'
		else:
			if self.direccion.x != 0:
				self.estado = 'correr'
			else:
				self.estado = 'inactivo'

	def apply_gravity(self):
		self.direccion.y += self.gravedad
		self.rect.y += self.direccion.y

	def jump(self):
		self.direccion.y = self.vel_salto

	def update(self):
		self.get_input()
		self.get_status()
		self.animar()
