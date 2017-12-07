# team attributes
import buggies
import buggyClass
import random
import pusherClass
import images
import names


Fringe = {"money":800, "size":50, "buggies":9, "pushers":6, "mechanics":10}
SDC = {"money":1000, "size":40, "buggies":7, "pushers":10, "mechanics":7}
PIKA = {"money":900, "size":20, "buggies":9, "pushers":9, "mechanics":6}
Spirit = {"money":600, "size":25, "buggies":6, "pushers":9, "mechanics":6}
Apex = {"money":600, "size":16, "buggies":4, "pushers":4, "mechanics":8}
CIA = {"money":600, "size":20, "buggies":7, "pushers":4, "mechanics":8}
SAE = {"money":900, "size":20, "buggies":4, "pushers":8, "mechanics":6}
SigEp = {"money":900, "size":20, "buggies":5, "pushers":8, "mechanics":5}
SigNu = {"money":900, "size":20, "buggies":7, "pushers":8, "mechanics":6}

teams = ({"Fringe":buggies.Fringe, "SDC":buggies.SDC, "PIKA":buggies.PIKA, 
	"Spirit":buggies.Spirit, "Apex":buggies.Apex, "CIA":buggies.CIA, 
	"SAE":buggies.SAE, "SigEp":buggies.SigEp, "SigNu":buggies.SigNu})

attributes = ({"Fringe":Fringe, "SDC":SDC, "PIKA":PIKA, 
	"Spirit":Spirit, "Apex":Apex, "CIA":CIA, 
	"SAE":SAE, "SigEp":SigEp, "SigNu":SigNu})


class Team(object):

	def __init__(self, name):
		self.raceDayPushers = {0:[], 1:[], 2:[]}
		self.name = name
		self.attributes = attributes[self.name]
		self.buggyList = []
		self.getBuggies(self.attributes)
		self.personList = []
		self.getPeople(self.attributes)
		self.raceDayBugs = {0:None, 1:None, 2:None}
		
		self.totalTime = {0:0, 1:0, 2:0}

	def getBuggies(self, attributes):
		nameBank = teams[self.name]
		for i in range(self.attributes["buggies"]):
			bug = random.choice(nameBank)
			nameBank.remove(bug)
			bug = buggyClass.Buggy(bug, self)
			self.buggyList.append(bug)
			

	def getPeople(self, attributes):
		peopleAdded = 0
		while peopleAdded <= self.attributes["size"]:
			person = names.get_first_name()
			person = pusherClass.Pusher(person, self.attributes)
			if person not in self.personList:
				self.personList.append(person)
				peopleAdded += 1

	def __repr__(self):
		return self.name


