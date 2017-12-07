# button class
import pygame
import images
import mainLoop
import stats


class Button(pygame.sprite.Sprite):


	def __init__(self, currScreen, text, function, rect, fontsize=25, buttonInput=None):
		super().__init__()
		self.currentScreen = currScreen
		self.text = text
		self.function = function
		self.rect = rect
		self.scrollY = 0
		self.fontsize = fontsize
		self.highlighted = False
		self.buttonInput = buttonInput
		


	def drawButton(self, screen):
		button = pygame.Surface((self.rect.width+6, self.rect.height+6))
		button.fill(images.white)
		buttonOverlay = pygame.Surface((self.rect.width, self.rect.height))
		buttonOverlay.fill(images.purple)
		font = pygame.font.SysFont('silom', self.fontsize)
		text = font.render(self.text, True, (images.blue))
		buttonOverlay.blit(text, (buttonOverlay.get_width()/2 - (text.get_width()//2), 
			buttonOverlay.get_height()/2 - (text.get_height() // 2)))
		button.blit(buttonOverlay, (3, 3))
		screen.blit(button, (self.rect.left, self.rect.top+self.scrollY, 
			self.rect.width, self.rect.height))

	def mouseMotion(self, mouseX, mouseY):
		currentRect = pygame.Rect(self.rect.left, self.rect.top+self.scrollY, 
			self.rect.width, self.rect.height)
		if currentRect.collidepoint(mouseX, mouseY) and self.highlighted == False:
			self.rect = self.rect.inflate(4, 4)
			self.highlighted = True
		elif not currentRect.collidepoint(mouseX, mouseY) and self.highlighted == True:
			self.rect = self.rect.inflate(-4, -4)
			self.highlighted = False
	

	def mousePressed(self, mouseX, mouseY):
		currentRect = pygame.Rect(self.rect.left, self.rect.top+self.scrollY, 
			self.rect.width, self.rect.height)
		if currentRect.collidepoint(mouseX, mouseY):
				self.function(self.buttonInput)


