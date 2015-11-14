import pygame
from characters import Player, Speed

class World:
	""" World to generate player and level """

	def __init__(self, canvas, rect, color, player, levels):
		""" Constructor """

		# Set rectangle and create canvas' subsurface
		self.world_rect  = rect
		self.world  = canvas.subsurface(self.world_rect)

		# Set world bg color
		self.color = color

		# Set player
		self.player = player

		# Set levels
		self.levels = levels
		self.current_level = 0

		# State of the system running
		self.running = False

		# Test squences
		self.test_run = [['Step' for i in range(15)], \
			['Step', 'Step', 'Jump', 'Jump', 'Step', 'Step', 'Step', 'Jump'] + ['Step' for i in range(4)]]
		print self.test_run

	def run(self):
		""" Start the level (testing) """
		self.player.health = 1
		self.player.winner = False
		self.player.speed = Speed.WALK
		self.player.position = self.levels[self.current_level].player_pos
		self.running = True
		self.running_action = 0
		self.running_counter = 0
		self.running_max = 60

	def restart(self):
		""" Restart the level """
		self.running = False
		self.run()

	def next_level(self):
		""" Start the next level """
		self.current_level += 1

		if self.current_level < len(self.levels):
			self.run()
		else:
			print "Complete"
			self.running = False

	def draw(self):
		""" Draw the world (including level and player) """
		if self.running:
			self.running_counter = (self.running_counter + 1) % self.running_max

		if self.running and self.running_counter == 0:
			# Check for last move win
			if self.player.winner:
				print "Won level %d" % (self.current_level + 1, )
				self.next_level()
				return

			# If death
			if self.player.health == 0:
				print "Gameover on level %d" % (self.current_level + 1, )
				self.restart()
				return

			# Test, parse test command
			current_action = self.test_run[self.current_level][self.running_action]
			if current_action == "Step":
				self.player.step(self.levels[self.current_level])
			elif current_action == "Jump":
				self.player.jump()

		self.world.fill(self.color)
		self.world.blit(self.player.image, self.player.position)

		for item in self.levels[self.current_level].sprites:
			self.world.blit(item.image, item.position)

