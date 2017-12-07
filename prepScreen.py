# prep screen
import images
import pygame
import buttonClass
import stats

class PrepScreen(object):
	def __init__(self, game, width, height):
		self.game = game
		self.width = width
		self.height = height
		self.topBorder = 200
		self.border = 50
		self.teamLetter = {0:"A", 1:"B", 2:"C"}
		self.buttons = []

		buttCx = self.width//2
		buttCy = self.height//3 + 300
		buttWidth = width//4
		buttHeight = height//8
		buttonRect = pygame.Rect(buttCx-buttWidth//2, buttCy-buttHeight//2, 
			buttWidth, buttHeight)
		
		self.buttons.append(buttonClass.Button(self, "GO!", self.race, buttonRect))

	def redrawAll(self, screen):
		screen.fill(images.yellow)

		font = pygame.font.SysFont('signpainter', 100)
		text = font.render("Race %d, %s Team"%(3-stats.abcTeam, 
			self.teamLetter[stats.abcTeam]), True, (images.red))
		screen.blit(text, (self.width//2 - text.get_width()//2, 
			text.get_height()))

		bug = stats.getCurrentBuggy(stats.myTeam)
		bug.drawBuggyAt(screen, self.width//2, self.height//3+50)

		font = pygame.font.SysFont('silom', 25)
		text = font.render(bug.name, True, (images.white))
		screen.blit(text, (self.width//2 - text.get_width()//3, self.height//3+100))

		font = pygame.font.SysFont('signpainter', 50)
		text = font.render("3, 2, 1, ready, set...", True, (images.red))
		screen.blit(text, (self.width//2 - text.get_width()//2, self.height//3+200))

		for button in self.buttons:
			button.drawButton(screen)

	def mouseMotion(self, x, y):
		for button in self.buttons:
			button.mouseMotion(x, y)

	def mousePressed(self, x, y):
		for button in self.buttons:
			button.mousePressed(x, y)

	def race(self, input):
		self.game.state = "raceday"
		self.game.freeRollScreen.scrollY = 0


