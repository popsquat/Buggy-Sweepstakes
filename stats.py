#stats

teamList = []

myTeam = None
team1 = None
team2 = None
team3 = None

abcTeam = 2

currentPersonInfo = None
currentBuggyInfo = None

def getCurrentBuggy(team):
	return team.raceDayBugs[abcTeam]

def getCurrentPusher(team, hill):
	h = 0
	if hill == "hill1":
		h = 0
	elif hill == "hill2":
		h = 1
	elif hill == "hill3":
		h = 3
	elif hill == "hill4":
		h = 4
	elif hill == "hill5":
		h = 5
	else: return None

	return team.raceDayPushers[abcTeam][h]


results = {}

