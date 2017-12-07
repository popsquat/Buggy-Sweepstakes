'''
pygamegame.py
barebones created by Lukas Peraza
for 15-112 F15 Pygame Optional Lecture, 11/11/15
use this code in your term project if you want
'''

import pygame
import startScreen
import raceDayScreen
import freeRollScreen
import stats
import chooseATeamScreen
import homeScreen
import setupScreen
import prepScreen
import resultsScreen
import trainingScreen
import instructionScreen

pygame.init()

class PygameGame(object):

    def init(self):
        self.state = "startScreen"
        self.timer = False
        self.startScreen = startScreen.StartScreen(self, self.width, self.height)
        self.raceDayScreen = raceDayScreen.RaceDayScreen(self, self.width, self.height)
        pygame.time.set_timer(pygame.USEREVENT, 10)
        self.freeRollScreen = freeRollScreen.FreeRollScreen(self, self.width, self.height)
        self.chooseATeamScreen = chooseATeamScreen.ChooseATeamScreen(self, self.width, self.height)
        self.homeScreen = homeScreen.HomeScreen(self, self.width, self.height)
        self.setupScreen = setupScreen.SetupScreen(self, self.width, self.height)
        self.prepScreen = prepScreen.PrepScreen(self, self.width, self.height)
        self.resultsScreen = resultsScreen.ResultsScreen(self, self.width, self.height)
        self.trainingScreen = trainingScreen.TrainingScreen(self, self.width, self.height)
        self.instructionScreen = instructionScreen.InstructionScreen(self, self.width, self.height)
        stats.results = {}

    def mousePressed(self, x, y):
        if self.state == "startScreen":
            self.startScreen.mousePressed(x, y)
        elif self.state == "raceday":
            self.raceDayScreen.mousePressed(x, y)
        elif self.state == "chooseATeam":
            self.chooseATeamScreen.mousePressed(x, y)
        elif self.state == "homeScreen":
            self.homeScreen.mousePressed(x, y)
        elif self.state == "setupScreen":
            self.setupScreen.mousePressed(x, y)
        elif self.state == "prep":
            self.prepScreen.mousePressed(x, y)
        elif self.state =="results":
            self.resultsScreen.mousePressed(x, y)
        elif self.state == "train":
            self.trainingScreen.mousePressed(x, y)
        elif self.state == "instructions":
            self.instructionScreen.mousePressed(x, y)
        elif self.state == "freeroll":
            self.freeRollScreen.mousePressed(x, y)
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        if self.state == "startScreen":
            self.startScreen.mouseMotion(x, y)
        elif self.state == "raceday":
            self.raceDayScreen.mouseMotion(x, y)
        elif self.state == "chooseATeam":
            self.chooseATeamScreen.mouseMotion(x, y)
        elif self.state == "homeScreen":
            self.homeScreen.mouseMotion(x, y)
        elif self.state == "setupScreen":
            self.setupScreen.mouseMotion(x, y)
        elif self.state == "prep":
            self.prepScreen.mouseMotion(x, y)
        elif self.state == "results":
            self.resultsScreen.mouseMotion(x, y)
        elif self.state == "train":
            self.trainingScreen.mouseMotion(x, y)
        pass

    def mouseDrag(self, x, y):
        if self.state == "homeScreen":
            self.homeScreen.mouseDrag(x, y)
        elif self.state == "setupScreen":
            self.setupScreen.mouseDrag(x, y)
        elif self.state == "train":
            self.trainingScreen.mouseDrag(x, y)
        pass

    def keyPressed(self, keyCode, modifier):
        if self.state == "train":
            self.trainingScreen.keyPressed(keyCode, modifier)
        pass

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        if self.state == "raceday":
            self.raceDayScreen.checkForFreeRoll()
            if self.raceDayScreen.raceOver == False:
                for team in stats.teamList:
                    buggy = stats.getCurrentBuggy(team)
                    buggy.getSpeed(team)
                self.raceDayScreen.moveBuggies(self.width, self.height, self)
        elif self.state == "freeroll":
            self.freeRollScreen.timerFired(dt)
        elif self.state == "setupScreen":
            self.setupScreen.raceday()

        pass

    def redrawAll(self, screen):
        if self.state == "startScreen":
            self.startScreen.draw(screen, self.width, self.height)

        elif self.state == "raceday":
            self.raceDayScreen.draw(screen, self.width, self.height)

        elif self.state == "freeroll":
            self.freeRollScreen.redrawAll(screen)

        elif self.state == "chooseATeam":
            self.chooseATeamScreen.redrawAll(screen)

        elif self.state == "homeScreen":
            self.homeScreen.redrawAll(screen)

        elif self.state == "setupScreen":
            self.setupScreen.redrawAll(screen)

        elif self.state =="prep":
            self.prepScreen.redrawAll(screen)

        elif self.state == "results":
            self.resultsScreen.redrawAll(screen)

        elif self.state == "train":
            self.trainingScreen.redrawAll(screen)

        elif self.state == "instructions":
            self.instructionScreen.redrawAll(screen)
        pass

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def userevent(self):
        if self.state == "raceday":
            if self.raceDayScreen.raceOver == False:
                self.raceDayScreen.time += .01
        elif self.state == "freeroll":
            self.freeRollScreen.userevent()
        elif self.state == "train":
            self.trainingScreen.userevent()
        #gets called once a second



    def __init__(self, width=1000, height=600, fps=50, title="Buggy Sweepstakes"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.USEREVENT:
                    self.userevent()
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()