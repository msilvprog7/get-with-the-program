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
		self.bg_image = None

		# Set player
		self.player = player

		# Set levels
		self.levels = levels
		self.current_level = 0
		self.player.position = self.levels[self.current_level].player_pos

		# State of the system running
		self.running = False
		self.running_action = 0
                self.game_over = False

		# Test squences
		self.test_run = [['Step' for i in range(15)], \
			['Step', 'Step', 'Jump', 'Jump', 'Step', 'Step', 'Step', 'Jump'] + ['Step' for i in range(4)], \
			['Run', 'Jump', 'Jump', 'Step', 'Step', 'Step', 'Step'], \
			['Run', 'Step', 'Jump', 'Roll', 'Step', 'Roll']]

		# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		# Test running sequence
		# self.run(self.test_run[0])

	def set_bg(self, bg):
		""" Set the background image """
		self.bg_image = bg

	def set_program(self, sequence):
		self.sequence = sequence

	def run(self, sequence, restart=True):
		""" Start the level with the sequence of actions """
		if restart:
			self.running_action = 0
			self.player.position = self.levels[self.current_level].player_pos

		self.player.health = 1
		self.player.winner = False
		self.player.speed = Speed.WALK
		self.running = True
		self.paused = False
		self.running_counter = 0
		self.running_max = 10
		self.run_single = False
		self.set_program(sequence)

	def restart(self):
		""" Restart the level """
		self.running_action = 0
		self.running = False
                self.game_over = False

		# Move to start
		self.player.position = self.levels[self.current_level].player_pos

		# Could re-run
		# self.run(self.sequence)

	def pause(self):
		""" Pause the current level """
		self.paused = True

	def step(self, sequence):
		""" Execute a single action """
		self.run(sequence, False)
		self.run_single = True

	def next_level(self):
		""" Start the next level """
		self.current_level += 1

		if self.current_level < len(self.levels):
			# Could do other things (mainly in testing scenarios)
			# self.run(self.test_run[self.current_level])
			# return
			pass
		else:
			print "Complete"
			# Set to last level
			self.current_level -= 1

		# Move to start
		self.player.position = self.levels[self.current_level].player_pos

		# Stop running
		self.running = False
		self.paused = True

	def draw(self):
		""" Draw the world (including level and player) """
		# Running counter
		if self.running and not self.paused:
			self.running_counter = (self.running_counter + 1) % self.running_max

		# Take next action
		if self.running and not self.paused and self.running_counter == 0:
			# Check for last move win
			if self.player.winner:
				print "Won level %d" % (self.current_level + 1, )
				self.next_level()
				return

			# If death
			if self.player.health == 0:
				print "Gameover on level %d" % (self.current_level + 1, )
                                self.game_over = True
                                self.running = False
				# self.restart()
				return


			# Parse Sequence of actions

			# Too few actions
			if self.running_action >= len(self.sequence):
				print "Too few actions, ending early"
				self.restart()
				return

			current_action = self.sequence[self.running_action]
			# print current_action

			if current_action == "Step":
				self.player.step(self.levels[self.current_level])
			elif current_action == "Jump":
				self.player.jump(self.levels[self.current_level])
			elif current_action == "Roll":
				self.player.roll(self.levels[self.current_level])
			elif current_action == "Walk":
				self.player.walk(self.levels[self.current_level])
			elif current_action == "Run":
				self.player.run(self.levels[self.current_level])

			self.running_action += 1

			if self.run_single:
				self.run_single = False
				self.running = False

		# 1/3 step (for running motion)
		if self.running and not self.paused and self.running_counter == self.running_max // 3:
			# Finish running motion
			if not self.player.is_falling and self.player.is_running:
				self.player.finish_run(self.levels[self.current_level])

				# Check for death
				self.player.check_for_death(self.levels[self.current_level])

		# 2/3 step (for jumping and falling)
		if self.running and not self.paused and self.running_counter == 2 * self.running_max // 3:
			# Finish a jump
			if not self.player.can_jump:
				self.player.step(self.levels[self.current_level])

			# Finish a fall or a roll (if doing that)
			if self.player.is_falling:
				self.player.fall(should_die=True)
			elif not self.player.can_roll:
				self.player.step(self.levels[self.current_level])

		# Display bg
		if self.bg_image:
			self.world.blit(self.bg_image, (0, 0))
		else:
			self.world.fill(self.color)

		# Display player
		if self.player.sprite_sheet:
			self.world.blit(self.player.get_sprite(), self.player.get_sprite_position())
		else:
			self.world.blit(self.player.image, self.player.position)

		# End early if no more levels
		if self.current_level >= len(self.levels):
			return

		for item in self.levels[self.current_level].sprites:
			if item.sprite_sheet:
				self.world.blit(item.get_sprite(), item.get_sprite_position())
			else:
				self.world.blit(item.image, item.position)
