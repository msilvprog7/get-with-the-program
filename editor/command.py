from constants import *
import pygame
from events.click import ClickHandler

class Command(pygame.sprite.Sprite, ClickHandler):
    def __init__(self, x, y, width, height, color, label):
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

    def click(self, event):
        print "Clicked", self.text

    def render_text(self, label, font_size):
        font = get_font(TOKEN_SIZE)
        text = font.render(label, True, hex_to_rgb("#FFFFFF"))

        self.image.blit(text, ((TKN_WIDTH - text.get_width())/2, (TKN_HEIGHT - text.get_height())/2))

class CommandsBox(pygame.sprite.Sprite):
    def __init__(self, commands=[]):
        # Call the parent constructor
        super(CommandsBox, self).__init__()

        self.image = pygame.Surface([CMD_WIDTH, 384])
        self.image.fill(hex_to_rgb("#555555"))

        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = LVL_WIDTH

        x, y = LVL_WIDTH + TKN_PDDNG, TITLE_SIZE + TKN_PDDNG + 5
        color = hex_to_rgb("#0085BF")
        self._commands = pygame.sprite.Group()
        for command in commands:
            sprite = Command(x, y, TKN_WIDTH, TKN_HEIGHT, color, command)
            self._commands.add(sprite)
            self.children.append(sprite)
            x, y = CommandsBox.compute_next_grid_location(x, y)
            
        self.render_title()

    def click(self, event):
        print "Clicked commands"

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
