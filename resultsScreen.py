#results screen
import images
import stats
import pygame
import buttonClass

class ResultsScreen(object):

	def __init__(self, game, width, height):
		self.game = game
		self.width = width
		self.height = height
		self.topBorder = 200
		self.border = 50
		self.resultDistY = (self.height-self.topBorder-self.border)//6
		self.resultDistX = (self.width-2*self.border)//2
		self.resultHeight = (self.height-self.topBorder-self.border)//6.5
		self.resultWidth = (self.width-2*self.border)//2.5
		buttCx = self.width//2
		buttCy = self.height//3 + 350
		buttWidth = width//5
		buttHeight = height//9
		buttonRect = pygame.Rect(buttCx-buttWidth//2, buttCy-buttHeight//2, 
			buttWidth, buttHeight)
		
		self.button = (buttonClass.Button(self, "next race", self.nextRace, buttonRect))
		
		self.againButton = (buttonClass.Button(self, "play again?", self.restart, buttonRect))

	def redrawAll(self, screen):
		screen.fill(images.yellow)

		font = pygame.font.SysFont('signpainter', 100)
		text = font.render("Results", True, (images.red))
		screen.blit(text, (self.width//2 - text.get_width()//2, 
			text.get_height()//2))

		results = sorted(stats.results.values())
		for i in range(len(results)):
			result = results[i]
			cx = self.border+self.resultDistX//2
			if i >= 6:
				cx = self.border+self.resultDistX+self.resultDistX//2
			cy = self.border+100+self.resultDistY*(i%6)+self.resultDistY//2
			pygame.draw.rect(screen, images.white, (cx-self.resultWidth//2, cy-self.resultHeight//2, self.resultWidth, 
				self.resultHeight))
			font = pygame.font.SysFont('silom', 25)
			text = font.render(str(i+1), True, (images.blue))
			screen.blit(text, (cx-self.resultWidth//2+5, cy-text.get_height()//2))

			for key in stats.results:
				if stats.results[key] == result:
					font = pygame.font.SysFont('silom', 25)
					text = font.render(key, True, (images.blue))
					screen.blit(text, (cx-self.resultWidth//2+50, cy-text.get_height()//2))
					text = font.render(str(round(stats.results[key], 2)), True, (images.blue))
					screen.blit(text, (cx+self.resultWidth//2-text.get_width()-5, cy-text.get_height()//2))
		if stats.abcTeam != 0:
			self.button.drawButton(screen)
		else:
			self.againButton.drawButton(screen)

	def nextRace(self, input):
		stats.abcTeam -= 1
		self.game.raceDayScreen.time = 0
		self.game.state = "prep"

	def restart(self, input):
		self.game.init()

	def mouseMotion(self, x, y):
		if stats.abcTeam != 0:
			self.button.mouseMotion(x, y)
		else:
			self.againButton.mouseMotion(x, y)

	def mousePressed(self, x, y):
		if stats.abcTeam != 0:
			self.button.mousePressed(x, y)
		else:
			self.againButton.mousePressed(x, y)





