import pygame

class World: 

	def __init__(self, rect, color, canvas):
		""" Constructor """
		self.world_rect  = rect
		self.world  = canvas.subsurface(self.world_rect)
		self.color = color

	def draw(self):
		self.world.fill(self.color)