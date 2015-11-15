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
		self.is_running = False
		self.is_jumping = False
		self.can_jump = True
		self.is_rolling = False
		self.can_roll = True
		self.is_falling = False
		self.can_fall = False
		self.health = 1
		self.has_health = True

	def step(self, level):
		""" Update the character's position """
		# Move forward
		if not Speed.is_stopped(self.speed):
			self.position = (self.position[0] + self.face * self.size[0] * Speed.WALK, self.position[1])

		# If running (*** cut early if running through the flag ***)
		self.is_running = Speed.is_running(self.speed) and not level.flag_reached(self) \
			and not level.collided_with_standing_object(self) \
			and not(not self.is_rolling and level.collided_with_ceiling_spikes(self))

		# Check fall after a jump
		if (self.can_fall and not self.can_jump):
			self.fall(should_die=False)

		# Check for jumping (handle double turn)
		if self.is_jumping:
			self.position = (self.position[0], self.position[1] - self.size[1])
			self.is_jumping = False
			self.can_jump = False
		else:
			self.can_jump = True

		# Check for rolling (handle double turn)
		if self.is_rolling:
			self.is_rolling = False
			self.can_roll = False
		else:
			self.can_roll = True

		# Check for falling in hole
		if (self.can_jump and not Speed.is_stopped(self.speed) and self.can_fall and level.hole_beneath(self)):
			self.is_falling = True

	def fall(self, should_die):
		""" Make the character fall a space """
		self.position = (self.position[0], self.position[1] + self.size[1])

		if should_die:
			self.health = 0
			self.speed = Speed.STOP

		self.is_falling = False

	def finish_run(self, level):
		""" Finish a running motion """
		# Move forward
		if not Speed.is_stopped(self.speed):
			self.position = (self.position[0] + self.face * self.size[0] * Speed.WALK, self.position[1])

		# Check for falling in hole
		if (self.can_jump and not Speed.is_stopped(self.speed) and self.can_fall and level.hole_beneath(self)):
			self.is_falling = True


class Player(Character):
	""" Main character with appropriate controls that the World can control """

	def __init__(self, position, size, color):
		""" Constructor """
		super(Player, self).__init__(position)
		# Properties
		self.speed = Speed.WALK
		self.can_fall = True
		self.winner = False

		# Image
		self.size = size
		self.image = pygame.Surface([size[0], size[1]])
		self.image.fill(color)

	def check_for_death(self, level):
		""" Check if player has gone off screen, collided with an object, or collided with ceiling spikes """
		if level.past_end(self) or level.collided_with_standing_object(self) or \
			(self.can_roll and not self.is_rolling and level.collided_with_ceiling_spikes(self)):
			self.health = 0
			self.speed = Speed.STOP

	def step(self, level):
		""" Update player's position """
		super(Player, self).step(level)

		# Check if flag reached or death
		if level.flag_reached(self):
			self.speed = Speed.STOP
			self.winner = True
		elif level.past_end(self) or level.collided_with_standing_object(self) or \
			(self.can_roll and not self.is_rolling and level.collided_with_ceiling_spikes(self)):
			self.health = 0
			self.speed = Speed.STOP

	def jump(self, level):
		""" Set state to jumping """
		if self.can_jump:
			self.is_jumping = True
			self.step(level)

	def run(self, level):
		""" Change speed to fast """
		self.speed = Speed.RUN
		self.step(level)

	def walk(self, level):
		""" Change speed to slow """
		self.speed = Speed.WALK
		self.step(level)

	def roll(self, level):
		""" Change to crouching roll """
		if self.can_roll:
			self.is_rolling = True
			self.step(level)