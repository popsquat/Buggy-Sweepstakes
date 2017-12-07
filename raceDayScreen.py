# race day
import teamClass
import random
import copy
import images
import pygame
import buggyClass
import stats
import freeRollBuggyClass
import buttonClass


class RaceDayScreen(object):

	def __init__(self, game, width, height):
		# teamChoice = ["Fringe", "SDC", "PIKA", "Spirit", "Apex", "CIA", "SAE", "SigEp", "SigNu"]

		self.game = game
		self.raceOver = False
		stats.teamList = []
		stats.abcTeam = 2
		self.hill = "hill1"
		self.hillValues = {"hill1":1, "hill2":2, "hill3":3, "hill4":4, "hill5":5}
		self.time = 0.01
		self.width = width
		self.height = height
		self.abcNames = {0:"A", 1:"B", 2:"C"}
		buttonRect = pygame.Rect(self.width//2-85, self.height-75, 70, 50)
		self.button =  buttonClass.Button(self, "quick finish", self.quickFinish, buttonRect, 10)


	def draw(self, screen, width, height):
		if self.raceOver == False:
			self.drawLeftSide(screen, width, height)
			self.drawRightSide(screen, width, height)
			self.drawInfoBar(screen, width, height)

	def drawLeftSide(self, screen, width, height):
		# left side
		asphalt = pygame.transform.scale(images.asphalt, (width//2, height))
		screen.blit(asphalt, (0,0))

		# course map
		pygame.draw.lines(screen, images.one, False, images.hills["hill1"], 10)
		pygame.draw.lines(screen, images.two, False, images.hills["hill2"], 10)
		pygame.draw.lines(screen, images.roll, False, images.hills["freeroll"], 10)
		pygame.draw.lines(screen, images.three, False, images.hills["hill3"], 10)
		pygame.draw.lines(screen, images.four, False, images.hills["hill4"], 10)
		pygame.draw.lines(screen, images.five, False, images.hills["hill5"], 10)

		#draw buggies
		for team in stats.teamList:
			buggy = stats.getCurrentBuggy(team)
			buggy.drawIcon(screen)

	def drawRightSide(self, screen, width, height):
		#a team, will need to be able to change this as well
		myBug = stats.getCurrentBuggy(stats.myTeam)
		hillToDraw = myBug.currentHill
		if hillToDraw == "hill1":
			self.drawHill1(screen, width, height)
		elif hillToDraw == "hill2":
			self.drawHill2(screen, width, height)
		elif hillToDraw == "hill3":
			self.drawHill3(screen, width, height)
		elif hillToDraw == "hill4":
			self.drawHill4(screen, width, height)
		elif hillToDraw == "hill5":
			self.drawHill5(screen, width, height)


		self.drawRacingBuggies(screen, width, height)

	def drawHill1(self, screen, width, height):
		hill1 = pygame.transform.scale(images.hill1, (width//2, height))
		screen.blit(hill1, (width//2,0))
		loHeight = height-100
		hiHeight = height-200
		points = ([
			(width//2, loHeight), 
			(width, hiHeight),
			(width, height),
			(width//2, height)
		])
		pygame.draw.polygon(screen, images.grey, points, 0)


	def drawHill2(self, screen, width, height):
		hill2 = pygame.transform.scale(images.hill2, (width//2, height))
		screen.blit(hill2, (width//2,0))
		points = ([
			(width//2, height-200), 
			(width, height-200),
			(width, height),
			(width//2, height)
		])
		pygame.draw.polygon(screen, images.grey, points, 0)
		pass

	def drawHill3(self, screen, width, height):
		hill3 = pygame.transform.scale(images.hill3, (width//2, height))
		screen.blit(hill3, (width//2,0))
		loHeight = height-100
		hiHeight = height-250
		points = ([
			(width//2, hiHeight), 
			(width, loHeight),
			(width, height),
			(width//2, height)
		])
		pygame.draw.polygon(screen, images.grey, points, 0)
		pass

	def drawHill4(self, screen, width, height):
		hill4 = pygame.transform.scale(images.hill4, (width//2, height))
		screen.blit(hill4, (width//2,0))
		loHeight = height-150
		hiHeight = height-225
		points = ([
			(width//2, hiHeight), 
			(width, loHeight),
			(width, height),
			(width//2, height)
		])
		pygame.draw.polygon(screen, images.grey, points, 0)
		pass

	def drawHill5(self, screen, width, height):
		hill5 = pygame.transform.scale(images.hill5, (width//2, height))
		screen.blit(hill5, (width//2,0))
		points = ([
			(width//2, height-200), 
			(width, height-200),
			(width, height),
			(width//2, height)
		])
		pygame.draw.polygon(screen, images.grey, points, 0)
		pass

	def drawRacingBuggies(self, screen, width, height):
		for team in stats.teamList:
			buggy = stats.getCurrentBuggy(team)
			pusher = stats.getCurrentPusher(team, buggy.currentHill)
			if buggy.currentHill == stats.getCurrentBuggy(stats.myTeam).currentHill:
				buggy.drawBuggy(screen, width, height)


	def drawInfoBar(self, screen, width, height):
		pygame.draw.rect(screen, images.blue, (0,0,width, 55))
		pygame.draw.rect(screen, images.blue, (width//2-100,0,100, height))
		#draw timer
		font = pygame.font.SysFont('silom', 20)
		text = font.render("time: " + str(round(self.time, 2)), True, (images.white))
		screen.blit(text, (width//3, text.get_height()//2))

		#draw which hill it is
		myBug = stats.getCurrentBuggy(stats.myTeam)
		hillToDraw = myBug.currentHill
		hill = "Hill %s"%hillToDraw[-1]

		text = font.render(hill, True, (images.white))
		screen.blit(text, (width//2+text.get_width()//2,
		 text.get_height()//2))

		for i in range(len(stats.teamList)):
			team = stats.teamList[i]
			buggy = stats.getCurrentBuggy(team)
			buggy.drawIconAt(screen, width//2-50, 100+100*i)
			font = pygame.font.SysFont('silom', 10)
			text = font.render(team.name, True, (images.white))
			screen.blit(text, (width//2-50-text.get_width()//2, 100+100*i+15))

		self.button.drawButton(screen)


	def moveBuggies(self, width, height, game):
		for team in stats.teamList:
			buggy = stats.getCurrentBuggy(team)
			buggy.moveBuggy(width, height, game)

	def checkForFreeRoll(self):
		myBug = stats.getCurrentBuggy(stats.myTeam)
		if myBug.currentHill == "freeroll":

			self.game.freeRollScreen.speed = myBug.speed
			self.game.freeRollScreen.buggyGroup = pygame.sprite.Group()
			self.game.freeRollScreen.buggy = freeRollBuggyClass.FreeRollBuggy(self.width, self.height, stats.myTeam)
			self.game.freeRollScreen.buggyGroup.add(self.game.freeRollScreen.buggy)

			self.game.state = "freeroll"

		#check if everyone is done
		finished = True
		if len(stats.teamList) != 0:
			finished = True
			for team in stats.teamList:
				bug = stats.getCurrentBuggy(team)
				if not bug.finished:
					finished = False

			if finished == True:
				self.game.state = "results"
		
	

	def mouseMotion(self, x, y):
		self.button.mouseMotion(x, y)
		
	def mousePressed(self, x, y):
		self.button.mousePressed(x, y)


	def getBuggies(self):
		for team in stats.teamList:
			if team != stats.myTeam:
				choices = team.buggyList
				for abcTeam in range(3):
					bug = random.choice(choices)
					choices.remove(bug)
					team.raceDayBugs[abcTeam] = bug

	def getPeople(self):
		for team in stats.teamList:
			if team != stats.myTeam:
				choices = team.personList
				for abcTeam in range(3):
					for i in range(5):
						per = random.choice(choices)
						choices.remove(per)
						team.raceDayPushers[abcTeam].append(per)
					team.raceDayPushers[abcTeam].insert(2, 'You!')

	def timer(self):
		if self.timer == False:
			pygame.time.set_timer(pygame.USEREVENT, 1000)
			self.timer == True

	def getFinalTime(self, bug, team):
		#speed called every .02 seconds
		#total time in seconds
		totalTime = self.time
		nextHill = bug.currentHill
		if nextHill == "hill2" or nextHill == "hill1":
			totalTime += random.randint(20, 50)
		elif nextHill == "freeroll":
			totalTime += random.randint(20, 50)
			nextHill = "hill3"
			bug.iconLocation = 0
		while nextHill != "hill6":
			bug.currentHill = nextHill
			bug.getSpeed(team)
			currHill = bug.currentHill
			currSpeed = bug.buggySpeed
			percentDone = bug.iconLocation/len(images.hills[currHill])
			remaining = (self.width-(self.width*percentDone))
			totalTime += remaining*(.02/currSpeed)

			nextHill = "hill%d"%(int(bug.currentHill[-1])+1)
			bug.iconLocation = 0

		return totalTime
	


	def quickFinish(self, input):
		for team in stats.teamList:
			bug = stats.getCurrentBuggy(team)
			if bug.finished == False:
				finalTime = self.getFinalTime(bug, team)
				stats.results[str(team)+" "+self.abcNames[stats.abcTeam]] = finalTime
				bug = stats.getCurrentBuggy(team)
				bug.finished = True

