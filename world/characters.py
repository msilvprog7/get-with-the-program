import pygame

class Face:
	""" Represent the direction a character is facing """
	LEFT = -1
	RIGHT = 1

	@staticmethod
	def is_facing_left(face):
		""" See if character is facing left """
		return face == Face.LEFT

	@staticmethod
	def is_facing_right(face):
		""" See if character is facing right """
		return face == Face.RIGHT


class Speed:
	""" Represents the speed at which a character is moving """
	STOP = 0
	WALK = 1
	RUN = 2

	@staticmethod
	def is_stopped(speed):
		""" See if character is stopped """
		return speed == Speed.STOP

	@staticmethod
	def is_walking(speed):
		""" See if character is walking """
		return speed == Speed.WALK

	@staticmethod
	def is_running(speed):
		""" See if character is running """
		return speed == Speed.RUN


class Character(pygame.sprite.Sprite):
	""" State and basic functionality of a movable character """

	def __init__(self, position):
		""" Constructor """
		super(Character, self).__init__()
		self.position = position
		self.face = Face.RIGHT
		self.speed = Speed.STOP
		self.is_jumping = False
		self.is_rolling = False
		self.health = 1
		self.has_health = True

	def draw(self):
		""" Draw the character """
		pass


class Player(Character):
	""" Main character with appropriate controls that the World can control """

	def __init__(self, position, size, color):
		""" Constructor """
		super(Player, self).__init__(position)
		self.image = pygame.Surface([size[0], size[1]])
		self.image.fill(color)