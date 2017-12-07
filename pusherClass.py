#pusher class
import random
import pygame


class Pusher(object):

	def __init__(self, name, teamAttributes):
		self.name = name
		self.strength = random.randint(max(teamAttributes["pushers"]-2, 0), 
			min(teamAttributes["pushers"]+2,10))
		self.speed = random.randint(max(teamAttributes["pushers"]-2, 0), 
			min(teamAttributes["pushers"]+2, 10))
		self.available = True

	def __repr__(self):
		return self.name

	def __eq__(self, other):
		return isinstance(other, Pusher) and self.name == other.name
