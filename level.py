import pygame

colors = {
	'black': (0, 0, 0),
	'red': (255, 0, 0),
	'blue': (0, 0, 255),
	'dark-red': (148, 35, 35),
	'dark-blue': (63, 62, 85),
	'dark-green': (79, 94, 31),
	'dark-yellow': (93, 85, 31)
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

    def get_floor_tile(self, position):
    	""" Return floor step """
    	floor = LevelSprite(position, \
    		(self.unit_size[0], self.unit_size[1]), \
    		colors['dark-green'])
    	floor.set_sprite_sheet("resources/floor.bmp", (0, 0), (64, 64), (0, 0))
    	return floor

    def add_sprite(self, current_char):
    	""" Generate sprite for current representation """
    	if current_char == "-":
    		# Land piece
    		self.sprites.append(self.get_floor_tile((self.player_pos[0] + self.current_sprites * self.unit_size[0], self.player_pos[1] + self.unit_size[1])))
    		self.sprites.append(self.get_floor_tile((self.player_pos[0] + self.current_sprites * self.unit_size[0], self.player_pos[1] + 2 * self.unit_size[1])))
    	elif current_char == "_":
    		# Hole
    		self.sprites.append(self.get_floor_tile((self.player_pos[0] + self.current_sprites * self.unit_size[0], self.player_pos[1] + 2 * self.unit_size[1])))
    	elif current_char == "!":
    		# Finish flag
    		flag = LevelSprite((self.player_pos[0] + self.current_sprites * self.unit_size[0], self.player_pos[1]), \
    			self.unit_size, \
    			colors['blue'])
    		flag.set_sprite_sheet("resources/flag.bmp", (0, 0), (15, 55), (0, 0))
    		self.sprites.append(flag)

    		self.sprites.append(self.get_floor_tile((self.player_pos[0] + self.current_sprites * self.unit_size[0], self.player_pos[1] + self.unit_size[1])))
    		self.sprites.append(self.get_floor_tile((self.player_pos[0] + self.current_sprites * self.unit_size[0], self.player_pos[1] + 2 * self.unit_size[1])))
    	elif current_char == "&":
    		# Standing object
    		bug = LevelSprite((self.player_pos[0] + self.current_sprites * self.unit_size[0], self.player_pos[1]), \
    			self.unit_size, \
    			colors['dark-red'])
    		bug.set_sprite_sheet("resources/beatles.bmp", (82, 144), (64, 40), (0, 20), scale=(458, 202))
    		self.sprites.append(bug)
    		self.sprites.append(self.get_floor_tile((self.player_pos[0] + self.current_sprites * self.unit_size[0], self.player_pos[1] + self.unit_size[1])))
    		self.sprites.append(self.get_floor_tile((self.player_pos[0] + self.current_sprites * self.unit_size[0], self.player_pos[1] + 2 * self.unit_size[1])))
    	elif current_char == "^":
    		# Ceiling
    		self.sprites.append(self.get_floor_tile((self.player_pos[0] + self.current_sprites * self.unit_size[0], self.player_pos[1] - 3 * self.unit_size[1])))
    		self.sprites.append(self.get_floor_tile((self.player_pos[0] + self.current_sprites * self.unit_size[0], self.player_pos[1] - 2 * self.unit_size[1])))
    		self.sprites.append(self.get_floor_tile((self.player_pos[0] + self.current_sprites * self.unit_size[0], self.player_pos[1] - self.unit_size[1])))

    		# Ceiling spike
    		dangle = LevelSprite((self.player_pos[0] + self.current_sprites * self.unit_size[0], self.player_pos[1]), \
    			self.unit_size, \
    			colors['dark-blue'])
    		dangle.set_sprite_sheet("resources/dangle.bmp", (90, 0), (23, 88), (0, -30))
    		self.sprites.append(dangle)

    		# Floor
    		self.sprites.append(self.get_floor_tile((self.player_pos[0] + self.current_sprites * self.unit_size[0], self.player_pos[1] + self.unit_size[1])))
    		self.sprites.append(self.get_floor_tile((self.player_pos[0] + self.current_sprites * self.unit_size[0], self.player_pos[1] + 2 * self.unit_size[1])))


    def hole_beneath(self, character):
    	""" Return whether or not the character has a hole beneath it """
    	check_xpos = character.position[0] // self.unit_size[0]
    	return check_xpos < len(self._landscape) and self._landscape[check_xpos] == "_"

    def collided_with_standing_object(self, character):
    	""" Return whether or not the character has collided with an object """
    	check_xpos = character.position[0] // self.unit_size[0]
    	check_ypos = character.position[1] == self.player_pos[1]
    	return check_xpos < len(self._landscape) and self._landscape[check_xpos] == "&" and check_ypos

    def collided_with_ceiling_spikes(self, character):
    	""" Return whether or not the character has collided with a ceiling spike """
    	check_xpos = character.position[0] // self.unit_size[0]
    	return check_xpos < len(self._landscape) and self._landscape[check_xpos] == "^"

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

		self.sprite_sheet = None

		self.size = size

	def set_sprite_sheet(self, file, pos, size, offset, scale=None):
		""" Set the sprite sheet """
		self.sprite_sheet = pygame.image.load(file).convert()
		if scale:
			self.sprite_sheet = pygame.transform.scale(self.sprite_sheet, scale)
		self.sprite_sheet_pos = pos
		self.sprite_sheet_size = size
		self.sprite_offset = offset

	def get_sprite(self):
		""" Get the current sprite """
		rect = pygame.Rect((self.sprite_sheet_pos[0], self.sprite_sheet_pos[1], \
			self.sprite_sheet_size[0], self.sprite_sheet_size[1]))
		image = pygame.Surface(rect.size).convert()
		image.blit(self.sprite_sheet, (0, 0), rect)
		image.set_colorkey((255, 255, 255), pygame.RLEACCEL)
		return image

	def get_sprite_position(self):
		""" Get the current sprite's position """
		return (self.position[0] + (self.size[0] - self.sprite_sheet_size[0]) // 2 + self.sprite_offset[0], \
			self.position[1] + (self.size[1] - self.sprite_sheet_size[1]) // 2 + self.sprite_offset[1])