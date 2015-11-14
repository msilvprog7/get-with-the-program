import pygame

LVL_WIDTH = 64
CMD_WIDTH = 512
PRG_WIDTH = CMD_WIDTH - LVL_WIDTH

class Command(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, label):
        # Call the parent constructor
        super(Command, self).__init__()

        # Create a new command sprite
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def draw():
        pass

class CommandsBox(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent constructor
        super(CommandsBox, self).__init__()

        self.image = pygame.Surface([CMD_WIDTH, 384])
        self.image.fill((200, 200, 200))

        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = LVL_WIDTH
