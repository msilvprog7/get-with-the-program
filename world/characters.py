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
		self.size = (0, 0)
		self.face = Face.RIGHT
		self.speed = Speed.STOP
		self.is_jumping = False
		self.can_jump = True
		self.is_rolling = False
		self.is_falling = False
		self.health = 1
		self.has_health = True

	def step(self, level):
		""" Update the character's position """
		# Move forward
		if not Speed.is_stopped(self.speed):
			self.position = (self.position[0] + self.face * self.size[0] * self.speed, self.position[1])

		# Check fall after a jump
		if (self.is_falling and not self.can_jump):
			self.fall(should_die=False)

		# Check for jumping
		if self.is_jumping:
			self.position = (self.position[0], self.position[1] - self.size[1])
			self.is_jumping = False
			self.can_jump = False
		else:
			self.can_jump = True

		# Check for falling in hole
		if (not Speed.is_stopped(self.speed) and self.is_falling and level.hole_beneath(self)):
			self.fall(should_die=True)

	def fall(self, should_die):
		""" Make the character fall a space """
		self.position = (self.position[0], self.position[1] + self.size[1])

		if should_die:
			self.health = 0
			self.speed = Speed.STOP

class Player(Character):
	""" Main character with appropriate controls that the World can control """

	def __init__(self, position, size, color):
		""" Constructor """
		super(Player, self).__init__(position)
		# Properties
		self.speed = Speed.WALK
		self.is_falling = True
		self.winner = False

		# Image
		self.size = size
		self.image = pygame.Surface([size[0], size[1]])
		self.image.fill(color)

	def step(self, level):
		""" Update player's position """
		super(Player, self).step(level)

		# Check if flag reached
		if level.flag_reached(self):
			self.speed = Speed.STOP
			self.winner = True
		elif level.past_end(self):
			self.health = 0
			self.speed = Speed.STOP

	def jump(self):
		""" Set state to jumping """
		if self.can_jump:
			self.is_jumping = True