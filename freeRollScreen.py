#free roll screen

import freeRollBuggyClass
import haybaleClass
import random
import pygame
import images
import math
import stats

class FreeRollScreen(object):

	def __init__(self, game, width, height):
		self.game = game
		self.width = width
		self.height = height
		self.x = self.width//2
		self.scrollY = 0
		self.haybaleGroup = pygame.sprite.Group()
		self.rollHeight = 7500
		self.viewInstructions = True
		self.instructions = pygame.transform.scale(images.freerollInstructions, (self.width, self.height))
		self.makeCourse()
		for i in range(self.rollHeight//80):
			self.addRandomHaybale()

		# pygame.time.set_timer(pygame.USEREVENT, 10)

		self.seconds = 0


	def timerFired(self, dt):
		if not self.viewInstructions:

			if self.game.isKeyPressed(pygame.K_LEFT):
				self.buggy.changeDirection(-1)

			elif self.game.isKeyPressed(pygame.K_RIGHT):
				self.buggy.changeDirection(1)


			self.buggyGroup.update()

			#move the screen
			self.scrollY += self.speed
			if self.scrollY >= self.rollHeight:
				self.scrollY = self.rollHeight
				self.buggy.y -= self.speed
				if self.buggy.y < 0:
					myBug = stats.getCurrentBuggy(stats.myTeam)
					#put my buggy's hill at 3	
					myBug.currentHill = "hill3"
					myBug.buggyCy = self.height-40
					myBug.iconLocation = 0
					self.game.state = "raceday"
					pass


			self.haybaleGroup.update(self.scrollY)

			collided = pygame.sprite.spritecollide(self.buggy, self.haybaleGroup, True)
			if len(collided) > 0:
				self.speed = max(self.speed-3, 1)


	def redrawAll(self, screen):
		if not self.viewInstructions:
			asphalt = pygame.transform.scale(images.asphalt, (self.width, self.height*2))
			picHeight = self.height*2
			screen.blit(asphalt, (0,self.scrollY-self.height))
			screen.blit(asphalt, (0,self.scrollY-(self.height+picHeight)))
			screen.blit(asphalt, (0,self.scrollY-(self.height+picHeight*2)))
			screen.blit(asphalt, (0,self.scrollY-(self.height+picHeight*3)))
			screen.blit(asphalt, (0,self.scrollY-(self.height+picHeight*4)))
			screen.blit(asphalt, (0,self.scrollY-(self.height+picHeight*5)))
			screen.blit(asphalt, (0,self.scrollY-(self.height+picHeight*6)))
			screen.blit(asphalt, (0,self.scrollY-(self.height+picHeight*7)))

			self.haybaleGroup.draw(screen)
			self.buggyGroup.draw(screen)

			font = pygame.font.SysFont('silom', 20)
			text = font.render("time: " + str(round(self.game.raceDayScreen.time, 2)), True, (images.white))
			screen.blit(text, (self.width-200, text.get_height()//2))

		else:
			screen.blit(self.instructions, (0,0))

	def isKeyPressed(self, key):
		''' return whether a specific key is being held '''
		return self._keys.get(key, False)

	def addRandomHaybale(self):
		baleX = random.randint(0,self.width)
		baleY = random.randint(-self.rollHeight,self.height-250)
		baleRot = random.randint(0,355)
		bale = haybaleClass.Haybale(baleX, baleY, baleRot, self.scrollY)
		collided = pygame.sprite.spritecollide(bale, self.haybaleGroup, False)
		if len(collided) == 0:
			self.haybaleGroup.add(bale)

	def addHaybale(self, x, y, rotation):
		bale = haybaleClass.Haybale(x, y, rotation, self.scrollY)
		self.haybaleGroup.add(bale)

	def makeCourse(self):
		for y in range(-(self.rollHeight-50), self.height, 100):
			sides = [50, self.width-100]
			rot = random.choice([70, 80, 90, 100, 110, 270, 260, 250, 280, 290, 300])
			for x in sides:
				self.addHaybale(x, y, rot)

	def userevent(self):
		self.game.raceDayScreen.time += .01
		if self.game.raceDayScreen.time%1 < .01:
			self.seconds += 1
			if self.seconds%4 == 0:
				self.speed += 1
		pass

	def mousePressed(self, x, y):
		self.viewInstructions = False
		pygame.time.set_timer(pygame.USEREVENT, 10)


