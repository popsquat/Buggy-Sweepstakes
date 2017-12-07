# startScreen

import images
import pygame
import buttonClass

#initialize sprites
allButtonsList = pygame.sprite.Group()


class StartScreen(object):



	def __init__(self, game, width, height):
		self.game = game
		# Here's how a button is made
		buttCx = width*(2/3)
		buttCy = height*(2/3)
		buttWidth = width//4
		buttHeight = height//8
		buttonRect = pygame.Rect(buttCx-buttWidth//2, buttCy-buttHeight//2, 
			buttWidth, buttHeight)
		self.b1 = buttonClass.Button(self, "click to continue", self.changeState, 
			buttonRect, 25)
		allButtonsList.add(self.b1)

	def draw(self, screen, width, height):
		#change size of image to fit screen
		background = pygame.transform.scale(images.startBackground, (width, height))
		screen.blit(background, (0,0))
		haze = pygame.Surface(screen.get_size())
		haze.set_alpha(100)
		haze.fill(images.white)
		screen.blit(haze, (0,0))
		# create text
		font = pygame.font.SysFont('silom', 200)
		text = font.render("Buggy", True, (images.blue))
		screen.blit(text, (width/2 - text.get_width() // 2, 
			height/2 - text.get_height()*(3/4)))
		font = pygame.font.SysFont('signpainter', 100)
		text = font.render("Sweepstakes", True, (images.white))
		screen.blit(text, (width/2 - text.get_width() // 4, 
			height/2 - (text.get_height() // 2)*(4/5)))
		self.b1.drawButton(screen)
		

	def mouseMotion(self, x, y):
		for button in allButtonsList:
			return button.mouseMotion(x, y)
		

	def mousePressed(self, x, y):
		for button in allButtonsList:
			return button.mousePressed(x, y)
		pass


# button functions

	def changeState(self, input):
		#### goes to raceday for now until I get that working
			self.game.state = "instructions"
