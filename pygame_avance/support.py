from os import walk
import pygame

def import_folder(path):
	# Importa las imagenes en una lista para las animaciones en player.py
	surface_list = []

	for _,__,img_files in walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

	return surface_list
