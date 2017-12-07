# training screen
import images
import stats
import pygame
import buttonClass
import random
import string

class TrainingScreen(object):

	def __init__(self, game, width, height):
		self.game = game
		self.width = width
		self.height = height
		self.displayInstructions = True
		self.pusher = None
		self.train = None
		self.instructions = images.trainingInstructions
		self.instructions = pygame.transform.scale(self.instructions, (self.width, self.height))
		self.map = images.courseMap
		self.map = pygame.transform.scale(self.map, (self.width, self.height))
		self.personButtons = []
		self.done = False
		self.count = 0
		self.plus = 0
		self.keyEdge = 50
		self.keyCx = random.randint(50, self.width-50)
		self.keyCy = random.randint(50, self.height-50)
		self.currentKey = random.choice(string.ascii_lowercase)
		self.buttons = []

		self.scrollY = 0
		self.clickY = 0

		self.time = 0
		self.seconds = 30
		pygame.time.set_timer(pygame.USEREVENT, 10)


		self.topBorder = 200
		self.border = 50
		self.dist = (self.width-(self.border*2))//3

		self.buggySquareWidth = (self.dist*2)//3.5
		self.buggySquareHeight = (self.height-self.topBorder-self.border)//2.5
		self.buggySquareDistX = (self.dist*2)//3
		self.buggySquareDistY = (self.height-self.topBorder-self.border)//2

		buttonDist = (self.height-2*self.border)/4

		buttCx = int(self.border+self.dist*(5/2))
		buttCy = int(self.height-buttonDist*2)
		buttWidth = width//4
		buttHeight = height//8
		buttonRect = pygame.Rect(buttCx-buttWidth//2, buttCy-buttHeight//2, 
			buttWidth, buttHeight)
		
		self.buttons.append(buttonClass.Button(self, "strength", self.strength, buttonRect))

		buttCy = int(self.height-buttonDist*3)
		buttonRect = pygame.Rect(buttCx-buttWidth//2, buttCy-buttHeight//2, 
			buttWidth, buttHeight)
		self.buttons.append(buttonClass.Button(self, "speed", self.speed, buttonRect))


	def redrawAll(self, screen):
		if self.pusher == None or self.train == None:
			screen.fill(images.red)
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

			font = pygame.font.SysFont('signpainter', 80)
			text = font.render("Choose a Pusher to Train", True, (images.red))
			screen.blit(text, (self.width//3 - text.get_width()//2, 
				self.topBorder//2 - (text.get_height()//2)))

			font = pygame.font.SysFont('silom', 15)
			text = font.render("click and drag to scroll", True, (images.white))
			screen.blit(text, (self.border, self.topBorder-text.get_height()))

			font = pygame.font.SysFont('silom', 25)
			text = font.render("pusher: %s"%str(self.pusher), True, (images.white))
			screen.blit(text, (self.width-self.border*2-text.get_width(), self.height-self.border-100))

			font = pygame.font.SysFont('silom', 25)
			text = font.render("training: %s"%self.train, True, (images.white))
			screen.blit(text, (self.width-self.border*2-text.get_width(), self.height-self.border-50))


			for button in self.buttons:
							button.drawButton(screen)

		elif self.displayInstructions == True:
			screen.blit(self.instructions, (0, 0))

		elif not self.done:
			screen.blit(self.map, (0,0))
			self.drawKey(screen)
			font = pygame.font.SysFont('silom', 30)
			text = font.render("time left: %d"%self.seconds, True, (images.white))
			screen.blit(text, (self.width-text.get_width(), 10))

		else:
			screen.fill(images.yellow)
			font = pygame.font.SysFont('silom', 30)
			
			text = font.render("your score: %d"%self.count, True, (images.white))
			screen.blit(text, (self.width//2-text.get_width()//2, self.height//4-text.get_height()))

			text = font.render("%s gained %d %s"%(self.pusher, self.plus, self.train), True, (images.white))
			screen.blit(text, (self.width//2-text.get_width()//2, (self.height//4)*2-text.get_height()))

			text = font.render("click anywhere to return to home", True, (images.white))
			screen.blit(text, (self.width//2-text.get_width()//2, (self.height//4)*3-text.get_height()))

			
	def makeInfoButtons(self):
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
				self.addPerson, rect, 25, person))

	def mouseMotion(self, x, y):
		if self.pusher == None or self.train == None:
			for button in self.buttons:
				button.mouseMotion(x, y)
		

	def mousePressed(self, x, y):
		self.clickY = y-self.scrollY
		
		if self.pusher == None or self.train == None:
			for button in self.personButtons:
				button.mousePressed(x, y)
			for button in self.buttons:
				button.mousePressed(x, y)

		elif self.displayInstructions == True:
			self.displayInstructions = False

		elif self.done:
			self.game.state = "homeScreen"


	def mouseDrag(self, x, y):
		if self.pusher == None or self.train == None:

			self.scrollY = y-self.clickY

			if self.scrollY > 0:
				self.scrollY = 0
		
			height = (-(len(stats.myTeam.personList)//3+1)*(self.buggySquareDistY//3) + 
				(self.height-self.topBorder-self.border))
			if self.scrollY < height:
				self.scrollY = height

			for button in self.personButtons:
				button.scrollY = self.scrollY

	def drawKey(self, screen):
		key = pygame.Surface((self.keyEdge, self.keyEdge))
		key.fill(images.purple)
		inner = pygame.Surface((self.keyEdge-4, self.keyEdge-4))
		inner.fill(images.blue)
		font = pygame.font.SysFont('silom', 30)
		text = font.render(self.currentKey.upper(), True, (images.white))
		inner.blit(text, ((self.keyEdge)//2-text.get_width()//2, 
			(self.keyEdge)//2-text.get_height()//2))
		key.blit(inner, (2, 2))
		screen.blit(key, (self.keyCx-self.keyEdge//2, self.keyCy-self.keyEdge//2, 
			self.keyEdge, self.keyEdge))


	def addPerson(self, person):
		self.pusher = person

	def keyPressed(self, keyCode, modifier):
		if keyCode == ord(self.currentKey):
			self.count += 1
			self.currentKey = random.choice(string.ascii_lowercase)
			self.keyCx = random.randint(50, self.width-50)
			self.keyCy = random.randint(50, self.height-50)
			

	def userevent(self):
		if ((self.done == False) and (self.pusher != None) and 
			(self.train != None) and (self.displayInstructions != True)):
			self.time += .01
			if self.time%1 < .01:
				self.seconds -= 1
				if self.seconds == 0:
					self.plus = self.count//6
					if self.train == "speed":
						newSpeed = self.pusher.speed + self.plus
						if newSpeed >= 10:
							self.plus = 10-self.pusher.speed
						self.pusher.speed = min(newSpeed, 10)
					elif self.train == "strength":
						newStrength = self.pusher.strength + self.plus
						if newStrength >= 10:
							self.plus = 10-self.pusher.strength
						self.pusher.strength = min(newStrength, 10)
					self.done = True




	def strength(self, input):
		self.train = "strength"

	def speed(self, input):
		self.train = "speed"




