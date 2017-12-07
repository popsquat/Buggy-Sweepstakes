# choose a team screen
import buttonClass
import images
import stats
import teamClass
import copy
import pygame

class ChooseATeamScreen(object):

	def __init__(self, game, width, height):
		self.game = game
		self.width = width
		self.height = height
		self.topBorder = 200
		self.border = 50
		self.buttWidth = (self.width-self.border*2)//3.5
		self.buttHeight = (self.height-self.border-self.topBorder)//3.5
		self.distWidth = (self.width-self.border*2)//3
		self.distHeight = (self.height-self.border-self.topBorder)//3
		self.buttons = []
		teams = copy.copy(images.teamChoice)

		for x in range(3):
			for y in range(3):
				rect = pygame.Rect(self.border+self.distWidth*x, self.topBorder+self.distHeight*y, 
					self.buttWidth, self.buttHeight)
				team = teams.pop(0)

				self.buttons.append(buttonClass.Button(self, team, 
					self.buttonFunction, rect, 50, team))

	def buttonFunction(self, team):
		stats.myTeam = teamClass.Team(team)
		stats.teamList.append(stats.myTeam)
		self.game.homeScreen.makeInfoButtons()

		#change this as soon as the next step is available
		self.game.state = "homeScreen"


	def redrawAll(self, screen):
		screen.fill(images.yellow)
		for button in self.buttons:
			button.drawButton(screen)

		font = pygame.font.SysFont('signpainter', 100)
		text = font.render("Choose a Team", True, (images.red))
		screen.blit(text, (self.width//2 - text.get_width()//2, 
			self.topBorder//2 - (text.get_height()//2)))

	def mouseMotion(self, x, y):
		for button in self.buttons:
			button.mouseMotion(x, y)
		

	def mousePressed(self, x, y):
		for button in self.buttons:
			button.mousePressed(x, y)
