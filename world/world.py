import pygame
from characters import Player

class World:
	""" World to generate player and level """

	def __init__(self, canvas, rect, color, player):
		""" Constructor """

		# Set rectangle and create canvas' subsurface
		self.world_rect  = rect
		self.world  = canvas.subsurface(self.world_rect)

		# Set world bg color
		self.color = color

		# Set player
		self.player = player
		self.player.position = (50, 50)

	def draw(self):
		self.world.fill(self.color)
		self.world.blit(self.player.image, self.player.position)