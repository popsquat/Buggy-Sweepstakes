# raceDay setup screen
import images
import pygame
import stats
import buttonClass
import teamClass
import random


class SetupScreen(object):

	def __init__(self, game, width, height):
		self.game = game
		self.width = width
		self.height = height
		self.topBorder = 200
		self.border = 50
		self.currentTeam = 0
		self.teamLetter = {0:"A", 1:"B", 2:"C"}
		self.currentHill = 0
		self.hillName = {0:"hill 1", 1:"hill 2", 2:"freeroll", 3:"hill 3", 4:"hill 4", 5:"hill 5"}
		self.need = "buggy"

		self.scrollY = 0
		self.clickY = 0

		self.raceReady = False

		self.dist = (self.width-(self.border*2))//3

		self.buggySquareWidth = (self.dist*2)//3.5
		self.buggySquareHeight = (self.height-self.topBorder-self.border)//2.5
		self.buggySquareDistX = (self.dist*2)//3
		self.buggySquareDistY = (self.height-self.topBorder-self.border)//2
		self.buttons = []
		self.personButtons = []
		self.buggyButtons = []


		self.transRect = pygame.Surface((self.buggySquareWidth, self.buggySquareHeight))
		self.transRect.set_alpha(50)
		self.transRect.fill((images.red))

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
				self.addBuggy, rect, 25, buggy))


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
				self.addPusher, rect, 25, person))

	def redrawAll(self, screen):
		screen.fill(images.red)

		if self.need == "buggy":
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
				if not buggy.available:
					screen.blit(self.transRect, (cx-self.buggySquareWidth//2, cy-self.buggySquareHeight//2))

		else:
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
				if not person.available:
					screen.blit(self.transRect, (cx-self.buggySquareWidth//2, cy-height//2,
					self.buggySquareWidth, height))

		pygame.draw.rect(screen, images.yellow, (0,0,self.width,self.topBorder))
		pygame.draw.rect(screen, images.yellow, (0,0,self.border,self.height))
		pygame.draw.rect(screen, images.yellow, (self.border+2*self.dist,
			0,self.width-(self.border+2*self.dist),self.height))
		pygame.draw.rect(screen, images.yellow, (0,self.height-self.border,
			self.width,self.border))

		font = pygame.font.SysFont('signpainter', 100)
		text = font.render("Build Your Teams", True, (images.red))
		screen.blit(text, (self.width//3 - text.get_width()//2, 
			self.topBorder//2 - (text.get_height()//2)))

		font = pygame.font.SysFont('silom', 15)
		text = font.render("click and drag to scroll", True, (images.white))
		screen.blit(text, (self.border, 
			self.topBorder-text.get_height()))

		#A team
		font = pygame.font.SysFont('silom', 20)
		text = font.render("%s team buggy: %s"%(self.teamLetter[self.currentTeam], 
			stats.myTeam.raceDayBugs[self.currentTeam]),
			True, (images.blue))
		screen.blit(text, (self.width-self.border-text.get_width(), self.border+
			text.get_height()//2))
		text = font.render("%s team pushers:"%self.teamLetter[self.currentTeam], True, (images.blue))
		screen.blit(text, (self.width-self.border-text.get_width(), self.border+
			text.get_height()//2+20))
		for i in range(len(stats.myTeam.raceDayPushers[self.currentTeam])):
			text = font.render("%s: %s"%(self.hillName[i], 
				stats.myTeam.raceDayPushers[self.currentTeam][i]), 
				True, (images.blue))
			screen.blit(text, (self.width-self.border-text.get_width(), self.border+
				text.get_height()//2+40+20*i))
	

		#what do do next
		font = pygame.font.SysFont('silom', 20)
		if self.need == "buggy":
			text = font.render("Choose your %s Team %s"%(self.teamLetter[self.currentTeam], self.need), 
				True, (images.white))
		elif self.need == "pusher":
			text = font.render("Choose your %s Team %s %s"%(self.teamLetter[self.currentTeam], 
				self.hillName[self.currentHill], self.need), 
				True, (images.white))
		screen.blit(text, (self.width-self.border-text.get_width(),
			text.get_height()//2))



	def mousePressed(self, x, y):
		for button in self.buttons:
			button.mousePressed(x, y)
		self.clickY = y-self.scrollY
		if self.need == "buggy":
			for button in self.buggyButtons:
				button.mousePressed(x, y)
		elif self.need == "pusher":
			for button in self.personButtons:
				button.mousePressed(x, y)

	def mouseMotion(self, x, y):
		for button in self.buttons:
			button.mouseMotion(x, y)

	def mouseDrag(self, x, y):
		self.scrollY = y-self.clickY
		if self.scrollY > 0:
			self.scrollY = 0
		elif self.need == "buggies":
			height = (-(len(stats.myTeam.buggyList)//3+1)*self.buggySquareDistY + 
				(self.height-self.topBorder-self.border))
			if self.scrollY < height:
				self.scrollY = height
		elif self.need == "roster":
			height = (-(len(stats.myTeam.personList)//3+1)*(self.buggySquareDistY//3) + 
				(self.height-self.topBorder-self.border))
			if self.scrollY < height:
				self.scrollY = height

		for button in self.buggyButtons:
			button.scrollY = self.scrollY
		for button in self.personButtons:
			button.scrollY = self.scrollY

	def addBuggy(self, buggy):
		if buggy.available:
			stats.myTeam.raceDayBugs[self.currentTeam] = buggy
			self.scrollY = 0
			for button in self.personButtons:
				button.scrollY = 0
			buggy.available = False
			self.need = "pusher"
			self.currentHill = 0
			
			

	def addPusher(self, pusher):
		if pusher.available:
			stats.myTeam.raceDayPushers[self.currentTeam].append(pusher)
			pusher.available = False
			self.currentHill += 1
			if self.currentHill == 2:
				stats.myTeam.raceDayPushers[self.currentTeam].append('You!')
				self.currentHill += 1
			elif self.currentHill == 6:
				self.need = "buggy"
				self.scrollY = 0
				for button in self.buggyButtons:
					button.scrollY = 0
				self.currentTeam += 1
				if self.currentTeam == 3:
					self.raceReady = True
					self.currentTeam -= 1

	def raceday(self):
		if self.raceReady:

			teamChoice = ["Fringe", "SDC", "PIKA", "Spirit", "Apex", "CIA", "SAE", "SigEp", "SigNu"]

			teamChoice.remove(stats.myTeam.name)

			stats.team2 = teamClass.Team(random.choice(teamChoice))
			stats.teamList.append(stats.team2)
			teamChoice.remove(stats.team2.name)

			stats.team3 = teamClass.Team(random.choice(teamChoice))
			stats.teamList.append(stats.team3)
			teamChoice.remove(stats.team3.name)

			stats.team4 = teamClass.Team(random.choice(teamChoice))
			stats.teamList.append(stats.team4)
			teamChoice.remove(stats.team4.name)

			self.game.raceDayScreen.getBuggies()
			self.game.raceDayScreen.getPeople()

			for team in stats.teamList:
				stats.getCurrentBuggy(team).getSpeed
			self.game.state = "prep"








