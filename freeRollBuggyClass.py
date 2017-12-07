# free roll buggy class

import pygame
import images
import buggyClass
import stats

class FreeRollBuggy(pygame.sprite.Sprite):

	def __init__(self, width, height, team):
		super().__init__()
		self.team = team
		self.image = images.genericBuggy
		buggy = stats.getCurrentBuggy(self.team)
		images.color_surface(self.image, buggy.r, buggy.g, buggy.b)
		design = images.buggyDesign
		self.image.blit(design, (0,0))
		self.image = pygame.transform.scale(self.image, (150, 150))
		self.preserved = self.image.copy()
		self.y = height-120
		self.x = width//2
		self.dx = 0
		self.rotation = 0
		self.getRect()
		self.screenWidth = width
		self.screenHeight = height

	def getRect(self):
		(w, h) = self.image.get_size()
		w = w//2
		h = h//2
		self.rect = pygame.Rect(self.x - w / 2, (self.y)- h / 2, w, h)

	def changeDirection(self, dx):
		self.dx += dx
		self.rotation -= 3*dx

	def update(self):
		self.x += self.dx
		self.x = min(self.screenWidth-50, self.x)
		self.x = max(0, self.x)
		self.image = pygame.transform.rotate(self.preserved, self.rotation)
		self.getRect()


	def restore(self):
		self.image = self.preserved

	def __repr__(self):
		return "buggy at (%d, %d)"%(self.x, self.y)
