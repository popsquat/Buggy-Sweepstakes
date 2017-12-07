#haybale class

import pygame
import images

class Haybale(pygame.sprite.Sprite):

	def __init__(self, x, y, rotation, scrollY):
		super().__init__()
		self.x = x
		self.y = y
		self.rotation = rotation
		self.scrollY = scrollY
		self.image = pygame.transform.scale(images.haybale, (100, 90))
		self.image = pygame.transform.rotate(self.image, self.rotation)
		self.getRect()

	def getRect(self):
		(w, h) = self.image.get_size()
		w = w//2
		h = h//3
		self.rect = pygame.Rect(self.x - w / 2, (self.y+self.scrollY)- h / 2, w, h)

	def update(self, scrollY):
		self.scrollY = scrollY
		self.getRect()

	def __repr__(self):
		return "bale at (%d, %d)"%(self.x, self.y)





