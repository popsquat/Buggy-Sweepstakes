# instructions

import pygame
import images

class InstructionScreen(object):

	def __init__(self, game, width, height):
		self.game = game
		self.width = width
		self.height = height
		self.topBorder = 200
		self.border = 50
		self.instructions = pygame.transform.scale(images.startInstructions, (self.width, self.height))

	def redrawAll(self, screen):
		screen.blit(self.instructions, (0,0))

	def mousePressed(self, x, y):
		self.game.state = "chooseATeam"
