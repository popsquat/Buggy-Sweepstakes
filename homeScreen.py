#home screen
import stats
import pygame
import images
import buttonClass

class HomeScreen(object):

	def __init__(self, game, width, height):
		self.homeState = "buggies"
		self.game = game
		self.width = width
		self.height = height
		self.topBorder = 200
		self.border = 50
		self.scrollY = 0
		self.clickY = 0

		self.dist = (self.width-(self.border*2))//3

		self.buggySquareWidth = (self.dist*2)//3.5
		self.buggySquareHeight = (self.height-self.topBorder-self.border)//2.5
		self.buggySquareDistX = (self.dist*2)//3
		self.buggySquareDistY = (self.height-self.topBorder-self.border)//2
		self.buttons = []
		self.personButtons = []
		self.buggyButtons = []
		self.showInfo = False

		buttonDist = (self.height-2*self.border)/4

		buttCx = int(self.border+self.dist*(5/2))
		buttCy = int(self.height-buttonDist*4)
		buttWidth = width//4
		buttHeight = height//8
		buttonRect = pygame.Rect(buttCx-buttWidth//2, buttCy-buttHeight//2, 
			buttWidth, buttHeight)
		
		self.buttons.append(buttonClass.Button(self, "View Roster", self.displayRoster, buttonRect))
		
		buttCy = int(self.height-buttonDist*3)
		buttonRect = pygame.Rect(buttCx-buttWidth//2, buttCy-buttHeight//2, 
			buttWidth, buttHeight)

		self.buttons.append(buttonClass.Button(self, "View Buggies", self.displayBuggies, buttonRect))

		buttCy = int(self.height-buttonDist*2)
		buttonRect = pygame.Rect(buttCx-buttWidth//2, buttCy-buttHeight//2, 
			buttWidth, buttHeight)

		self.buttons.append(buttonClass.Button(self, "Train", self.train, buttonRect))

		buttCy = int(self.height-buttonDist)
		buttonRect = pygame.Rect(buttCx-buttWidth//2, buttCy-buttHeight//2, 
			buttWidth, buttHeight)

		self.buttons.append(buttonClass.Button(self, "Race", self.race, buttonRect))

		buttCy = self.height-self.border-buttHeight//2-20
		buttCx = self.width//3
		buttonRect = pygame.Rect(buttCx-buttWidth//2, buttCy-buttHeight//2, 
			buttWidth, buttHeight)

		self.backButton = buttonClass.Button(self, "Back", self.goBack, buttonRect)

	def makeInfoButtons(self):
		for i in range(len(stats.myTeam.buggyList)):
			loc = i%3
			buggy = stats.myTeam.buggyList[i]
			cx = (self.border+self.buggySquareDistX*loc+
				self.buggySquareDistX//2)
			cy = (self.topBorder+self.buggySquareDistY*(i//3)+self.scrollY+
				self.buggySquareDistY//2)
			rect = pygame.Rect(cx-self.buggySquareWidth//2, cy-self.buggySquareHeight//2,
				self.buggySquareWidth, self.buggySquareHeight)
			self.buggyButtons.append(buttonClass.Button(self, "Buggy", 
				self.showBuggyInfo, rect, 25, buggy))
			


		for i in range(len(stats.myTeam.personList)):
			loc = i%3
			height = self.buggySquareHeight//3
			distY = self.buggySquareDistY//3
			person = stats.myTeam.personList[i]
			cx = (self.border+self.buggySquareDistX*loc+
				self.buggySquareDistX//2)
			cy = (self.topBorder+distY*(i//3)+self.scrollY+
				distY//2)
			rect = pygame.Rect(cx-self.buggySquareWidth//2, cy-height//2,
				self.buggySquareWidth, height)
			self.personButtons.append(buttonClass.Button(self, "Person", 
				self.showPersonInfo, rect, 25, person))
	

	def redrawAll(self, screen):
		screen.fill(images.red)
		
		if self.homeState == "buggies" and self.showInfo == False:
			for i in range(len(stats.myTeam.buggyList)):
				loc = i%3
				buggy = stats.myTeam.buggyList[i]
				cx = (self.border+self.buggySquareDistX*loc+
					self.buggySquareDistX//2)
				cy = (self.topBorder+self.buggySquareDistY*(i//3)+self.scrollY+
					self.buggySquareDistY//2)
				pygame.draw.rect(screen, images.white, (cx-self.buggySquareWidth//2, cy-self.buggySquareHeight//2,
					self.buggySquareWidth, self.buggySquareHeight))
				buggy.drawBuggyAt(screen, cx, cy-10)
				font = pygame.font.SysFont('silom', 20)
				text = font.render(buggy.name, True, (images.blue))
				screen.blit(text, (cx-text.get_width()//2, cy+40))

		elif self.homeState == "roster" and self.showInfo == False:
			for i in range(len(stats.myTeam.personList)):
				loc = i%3
				height = self.buggySquareHeight//3
				distY = self.buggySquareDistY//3
				person = stats.myTeam.personList[i]
				cx = (self.border+self.buggySquareDistX*loc+
					self.buggySquareDistX//2)
				cy = (self.topBorder+distY*(i//3)+self.scrollY+
					distY//2)
				pygame.draw.rect(screen, images.white, (cx-self.buggySquareWidth//2, cy-height//2,
					self.buggySquareWidth, height))
				font = pygame.font.SysFont('silom', 20)
				text = font.render(person.name, True, (images.blue))
				screen.blit(text, (cx-text.get_width()//2, cy-text.get_height()//2))

		elif self.homeState == "buggies" and self.showInfo == True:
			font = pygame.font.SysFont('silom', 40)
			text = font.render(stats.currentBuggyInfo.name, True, (images.white))
			screen.blit(text, (self.border+50, 
				self.topBorder+text.get_height()//2))

			font = pygame.font.SysFont('silom', 20)
			text = font.render("weight: %d"%stats.currentBuggyInfo.weight, True, (images.white))
			screen.blit(text, (self.border+50, 
				self.topBorder+text.get_height()//2+100))

			self.backButton.drawButton(screen)

		elif self.homeState == "roster" and self.showInfo == True:
			font = pygame.font.SysFont('silom', 40)
			text = font.render(stats.currentPersonInfo.name, True, (images.white))
			screen.blit(text, (self.border+50, 
				self.topBorder+text.get_height()//2))

			font = pygame.font.SysFont('silom', 20)
			text = font.render("strength: %d"%stats.currentPersonInfo.strength, True, (images.white))
			screen.blit(text, (self.border+50, 
				self.topBorder+text.get_height()//2+100))

			text = font.render("speed: %d"%stats.currentPersonInfo.speed, True, (images.white))
			screen.blit(text, (self.border+50, 
				self.topBorder+text.get_height()//2+150))

			self.backButton.drawButton(screen)


		pygame.draw.rect(screen, images.yellow, (0,0,self.width,self.topBorder))
		pygame.draw.rect(screen, images.yellow, (0,0,self.border,self.height))
		pygame.draw.rect(screen, images.yellow, (self.border+2*self.dist,
			0,self.width-(self.border+2*self.dist),self.height))
		pygame.draw.rect(screen, images.yellow, (0,self.height-self.border,
			self.width,self.border))

		for button in self.buttons:
		 	button.drawButton(screen)

		font = pygame.font.SysFont('signpainter', 100)
		text = font.render("Hello %s"%stats.myTeam, True, (images.red))
		screen.blit(text, (self.width//3 - text.get_width()//2, 
			self.topBorder//2 - (text.get_height()//2)))

		font = pygame.font.SysFont('silom', 15)
		text = font.render("click and drag to scroll", True, (images.white))
		screen.blit(text, (self.border, 
			self.topBorder-text.get_height()))



	def mouseMotion(self, x, y):
		for button in self.buttons:
			button.mouseMotion(x, y)
		if self.showInfo == True:
			self.backButton.mouseMotion(x, y)
		pass
		

	def mousePressed(self, x, y):
		if self.showInfo == True:
			self.backButton.mousePressed(x, y)

		else:
			if self.homeState == "buggies":
				for button in self.buggyButtons:
					button.mousePressed(x, y)
			elif self.homeState == "roster":
				for button in self.personButtons:
					button.mousePressed(x, y)

		for button in self.buttons:
			button.mousePressed(x, y)
		self.clickY = y-self.scrollY


	def mouseDrag(self, x, y):
		self.scrollY = y-self.clickY
		if self.scrollY > 0:
			self.scrollY = 0
		elif self.homeState == "buggies":
			height = (-(len(stats.myTeam.buggyList)//3+1)*self.buggySquareDistY + 
				(self.height-self.topBorder-self.border))
			if self.scrollY < height:
				self.scrollY = height
		elif self.homeState == "roster":
			height = (-(len(stats.myTeam.personList)//3+1)*(self.buggySquareDistY//3) + 
				(self.height-self.topBorder-self.border))
			if self.scrollY < height:
				self.scrollY = height

		for button in self.buggyButtons:
			button.scrollY = self.scrollY
		for button in self.personButtons:
			button.scrollY = self.scrollY


	def displayRoster(self, input):
		self.homeState = "roster"
		self.scrollY = 0
		self.showInfo = False
		for button in self.buttons:
			button.scrollY = 0
		pass

	def displayBuggies(self, input):
		self.homeState = "buggies"
		self.scrollY = 0
		self.showInfo = False
		for button in self.buttons:
			button.scrollY = 0

	def train(self, input):
		self.game.state = "train"
		self.game.trainingScreen.__init__(self.game, self.width, self.height)
		self.game.trainingScreen.makeInfoButtons()

	def race(self, input):
		self.game.state = "setupScreen"
		self.game.setupScreen.makeInfoButtons()

	def showPersonInfo(self, person):
		stats.currentPersonInfo = person
		self.showInfo = True

	def showBuggyInfo(self, buggy):
		stats.currentBuggyInfo = buggy
		self.showInfo = True

	def goBack(self, input):
		self.showInfo = False


	def chooseRaceDayTeams(self):
		pass







