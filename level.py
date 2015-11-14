import pygame

colors = {
	'red': (255, 0, 0),
	'blue': (0, 0, 255)
}

class Level:
    def __init__(self, number, landscape, tokens, player_pos, unit_size):
        self._number = number
        self._landscape = landscape
        self._tokens = tokens
        self.player_pos = player_pos
        self.sprites = []
        self.unit_size = unit_size
        self.generate_level()

    def generate_level(self):
    	""" Create sprites for components """
    	self.current_sprites = 0
    	for current_char in self._landscape:
    		self.add_sprite(current_char)
    		self.current_sprites += 1

    def add_sprite(self, current_char):
    	""" Generate sprite for current representation """
    	if current_char == "-":
    		self.sprites.append(LevelSprite((self.player_pos[0] + self.current_sprites * self.unit_size[0], self.player_pos[1] + self.unit_size[1]), \
    			(self.unit_size[0], 2 * self.unit_size[1]), \
    			colors['red']))
    	elif current_char == "_":
    		self.sprites.append(LevelSprite((self.player_pos[0] + self.current_sprites * self.unit_size[0], self.player_pos[1] + 2 * self.unit_size[1]), \
    			self.unit_size, \
    			colors['red']))
    	elif current_char == "!":
    		self.sprites.append(LevelSprite((self.player_pos[0] + self.current_sprites * self.unit_size[0], self.player_pos[1]), \
    			self.unit_size, \
    			colors['blue']))
    		self.sprites.append(LevelSprite((self.player_pos[0] + self.current_sprites * self.unit_size[0], self.player_pos[1] + self.unit_size[1]), \
    			(self.unit_size[0], 2 * self.unit_size[1]), \
    			colors['red']))

    def hole_beneath(self, character):
    	""" Return whether or not the character has a hole beneath it """
    	check_pos = character.position[0] // self.unit_size[0]
    	return check_pos < len(self._landscape) and self._landscape[check_pos] == "_"

    def flag_reached(self, character):
    	""" Return whether or not the character has reached the flag """
    	check_xpos = character.position[0] // self.unit_size[0]
    	check_ypos = character.position[1] == self.player_pos[1]
    	return check_xpos < len(self._landscape) and self._landscape[check_xpos] == "!" and check_ypos

    def past_end(self, character):
    	""" Return whether or not the character has past the end of the level """
    	return character.position[0] >= 1024

class LevelSprite(pygame.sprite.Sprite):
	""" Representation of a part of the level """

	def __init__(self, position, size, color):
		""" Constructor """
		super(LevelSprite, self).__init__()
		# Make a square
		self.image = pygame.Surface([size[0], size[1]])
		self.image.fill(color)

		self.position = position