from constants import *
import pygame
from events.click import ClickHandler

class Command(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, label, parent):
        # Call the parent constructor
        super(Command, self).__init__()

        # Create a new command sprite
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.text = label
        self.render_text(label, 24)
        self.parent = parent

    def click(self, event):
        # no clicky while running
        if self.parent.world.running:
            return
        
        print "Clicked", self.text
        self.parent.program.step_list.append(self.text)
        self.parent.program.render_steps()

    def render_text(self, label, font_size):
        font = get_font(TOKEN_SIZE)
        text = font.render(label, True, hex_to_rgb("#FFFFFF"))

        self.image.blit(text, ((TKN_WIDTH - text.get_width())/2, (TKN_HEIGHT - text.get_height())/2))

class CommandsBox(pygame.sprite.Sprite):
    def __init__(self, levels, program, world, parent):
        # Call the parent constructor
        super(CommandsBox, self).__init__()

        self.program = program
        self.image = pygame.Surface([CMD_WIDTH, 384])
        self.image.fill(hex_to_rgb("#555555"))

        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = LVL_WIDTH

        self.world = world
        self.parent = parent

        self.levels = levels
        commands = self.levels[0]._tokens
        self.draw(commands, True)

    def draw(self, commands, init):
        x, y = LVL_WIDTH + TKN_PDDNG, TITLE_SIZE + TKN_PDDNG + 5
        color = hex_to_rgb("#0085BF")
        self._commands = pygame.sprite.Group()
        for command in commands:
            sprite = Command(x, y, TKN_WIDTH, TKN_HEIGHT, color, command, self)
            self._commands.add(sprite)
            x, y = CommandsBox.compute_next_grid_location(x, y)

        self.render_title()

        if not init:
            self.parent.update_children()

    def update(self):
        lvl = self.world.current_level
        self.draw(self.levels[lvl]._tokens, False)

    def render_title(self):
        font = get_font(TITLE_SIZE)
        text = font.render("Available Actions", True, hex_to_rgb("#FFFFFF"))

        self.image.blit(text, (TKN_PDDNG, 10))

    @staticmethod
    def compute_next_grid_location(x, y):
        if (TKN_WIDTH + TKN_PDDNG + x) > CMD_WIDTH:
            x = LVL_WIDTH + TKN_PDDNG
            y += TKN_PDDNG + TKN_HEIGHT
        else:
            x += TKN_WIDTH + TKN_PDDNG
        return x, y
