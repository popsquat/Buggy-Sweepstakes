
import pygame
import random
import buggies
import images
import stats



class Buggy(pygame.sprite.Sprite):

	def __init__(self, name, team):
		self.finished = False
		self.name = name
		self.r = random.randint(10,245)
		self.g = random.randint(10,245)
		self.b = random.randint(10,245)
		self.color = (self.r, self.g, self.b)
		self.weight = random.randint(1,10)
		self.control = random.randint(team.attributes["mechanics"]-2, 
			team.attributes["mechanics"]+2)
		self.currentHill = "hill1"
		self.hillTimer = 0
		self.team = team
		self.available = True
		self.abcNames = {0:"A", 1:"B", 2:"C"}

		#icons
		self.iconLocation = 0
		iconCx, iconCy = images.hills[self.currentHill][self.iconLocation]
		iconR = 10
		self.iconRect = pygame.Rect(iconCx-iconR, iconCy-iconR, iconR*2, iconR*2)
		self.speed = 1

		#buggies
		self.buggySpeed = 1

		#buggy images
		buggyIMG = images.buggy.copy()
		images.color_surface(buggyIMG, self.r, self.g, self.b)
		design = images.sidewaysBuggyDesign
		buggyIMG.blit(design, (0,0))

		self.leftBuggy = pygame.transform.scale(buggyIMG, (150,150))
		self.rightBuggy = pygame.transform.flip(self.leftBuggy, True, False)
		self.currentBuggy = pygame.transform.scale(buggyIMG, (200,100))
		self.rotatedBuggy = pygame.transform.scale(buggyIMG, (200,100))
		self.buggyWidth = self.leftBuggy.get_width()
		self.buggyHeight = self.leftBuggy.get_height()
		#to make buggy sit on ground
		self.buggyCx = 500
		self.buggyCy = 500
		self.yOffset = 20
		self.buggyRect = pygame.Rect(self.buggyCx-self.buggyWidth//2, 
			self.buggyCy-self.buggyHeight//2, self.buggyWidth, self.buggyHeight)

	def __repr__(self):
		return self.name

	def __eq__(self, other):
		return isinstance(other, Buggy) and self.name == other.name

	def drawIcon(self, screen):
		outlineRect = self.iconRect.inflate(2,2)
		pygame.draw.ellipse(screen, (255,255,255), outlineRect, 0)
		pygame.draw.ellipse(screen, self.color, self.iconRect, 0)

	def drawIconAt(self, screen, x, y):
		iconCx, iconCy = x, y
		iconR = 10
		iconRect = pygame.Rect(iconCx-iconR, iconCy-iconR, iconR*2, iconR*2)
		outlineRect = iconRect.inflate(2,2)
		pygame.draw.ellipse(screen, (255,255,255), outlineRect, 0)
		pygame.draw.ellipse(screen, self.color, iconRect, 0)


	def moveIcon(self):
		try:
			self.iconLocation+=1
			iconCx, iconCy = images.hills[self.currentHill][self.iconLocation]
			iconR = 10
			self.iconRect = pygame.Rect(iconCx-iconR, iconCy-iconR, iconR*2, iconR*2)
		except:
			if self.currentHill == "freeroll":
				self.currentHill = "hill3"
				self.buggyCy = self.game.height-40
				self.iconLocation = 1
			pass
		

	def drawBuggy(self, screen, width, height):
		if self.currentHill == "freeroll":
			return None
		#which way does it need to face
		if (self.currentHill == "hill1" or self.currentHill == "hill2"):
			self.currentBuggy = self.rightBuggy
		else:
			self.currentBuggy = self.leftBuggy
		#how much does it need to be rotated

		if self.currentHill == "hill2" or self.currentHill == "hill5":
			self.rotatedBuggy = self.currentBuggy
		elif self.currentHill == "hill1":
			self.rotatedBuggy = pygame.transform.rotate(self.currentBuggy, 11) 
		elif self.currentHill == "hill3":
			self.rotatedBuggy = pygame.transform.rotate(self.currentBuggy, -17)
		elif self. currentHill == "hill4": 
			self.rotatedBuggy = pygame.transform.rotate(self.currentBuggy, -8)

		screen.blit(self.rotatedBuggy, (self.buggyCx-self.buggyWidth//2, 
			self.buggyCy-self.buggyHeight//2+self.yOffset))

	def drawBuggyAt(self, screen, x, y):
		screen.blit(self.rightBuggy, (x-self.buggyWidth//2, 
			y-self.buggyHeight//2))

	def moveBuggy(self, width, height, game):
		#check if game is initialized, if not, initialize game
		try:
			if self.game != 1:
				pass
		except:
			self.game = game

			
		if self.currentHill == "freeroll":
			self.syncIcon(width, height, game)
			return None
		if self.finished == False:
			startingY = ({"hill1":height-20, "hill2":height-180, "hill3":height,
				"hill4":height-120, "hill5":height-200})
			startingX = ({"hill1":width//2, "hill2":width//2, "hill3":width, 
				"hill4":width, "hill5":width})

			slope = 0
			direct = 1

			if self.currentHill == "hill1":
				#slope = y/x
				slope = 1/5
			elif self.currentHill == "hill3":
				slope = 1.5/5
			elif self.currentHill == "hill4":
				slope = .75/5

			if (self.currentHill == "hill3" or self.currentHill == "hill4" 
				or self.currentHill == "hill5"):
				direct = -1

			self.buggyCx += self.buggySpeed*direct
			self.buggyCy -= self.buggySpeed*slope

			if (self.currentHill == "hill3" or self.currentHill == "hill4" 
				or self.currentHill == "hill5"):
				if self.buggyCx <= width//2:
					nextHill = "hill%d"%(int(self.currentHill[-1])+1)
					if nextHill == "hill6":
						self.finished = True
						stats.results[str(self.team)+" "+self.abcNames[stats.abcTeam]] = game.raceDayScreen.time
					else:
						self.currentHill = nextHill
						self.iconLocation = 0
						self.getSpeed(self.team)
						self.buggyCx = startingX[nextHill]
						self.buggyCy = startingY[nextHill]

			elif self.buggyCx >= width:
				nextHill = "hill%d"%(int(self.currentHill[-1])+1)
				if self.currentHill == "hill2":
						nextHill = "freeroll"
						self.syncIcon(width, height, game)
						self.currentHill = nextHill
						return None
				# if nextHill == "hill6":
				# 	self.finished = True
				# 	self.hillTimer += game.raceDayScreen.time
				else:
					self.currentHill = nextHill
					self.getSpeed(self.team)
					self.buggyCx = startingX[nextHill]
					self.buggyCy = startingY[nextHill]
					self.iconLocation = 0

			self.syncIcon(width, height, game)

	def syncIcon(self, width, height, game):
		checkpoints = 100
		if self.currentHill == "hill1":
			checkpoints = 19
		elif self.currentHill == "hill2":
			checkpoints = 9
		elif self.currentHill == "hill3":
			checkpoints = 19
		elif self.currentHill == "freeroll":
			checkpoints = 85
		elif self.currentHill == "hill4":
			checkpoints = 19
		elif self.currentHill == "hill5":
			checkpoints = 19

		callsBetweenMoves = (((width/2)/self.buggySpeed)/checkpoints)*50
		if (game.raceDayScreen.time*1000)%callsBetweenMoves < 50:
			self.moveIcon()


	def getSpeed(self, team):
		#speed should end up between 1 and 5
		
		#weights THIS NEEDS TO ADD TO 10 (or whatever my top speed should be)
		sth = .9
		spd = .1
		wt = -.6

		if self.currentHill == "hill2":
			sth = .8
			spd = .2
			wt = -.2

		elif self.currentHill == "freeroll":
			return

		elif self.currentHill == "hill3":
			sth = .6
			spd = .4
			wt = -.4

		elif self.currentHill == "hill4":
			sth = .3
			spd = .7
			wt = -.2

		elif self.currentHill == "hill5":
			sth = .1
			spd = .9
			wt = 0

		pusher = stats.getCurrentPusher(team, self.currentHill)

		speed = ((pusher.strength*sth) + 
			(pusher.speed*spd) + (self.weight*wt))
		if speed < 1:
			speed = 1

		self.speed = speed
		self.buggySpeed = speed

