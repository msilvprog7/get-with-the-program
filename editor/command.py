import pygame

LVL_WIDTH  = 64
CMD_WIDTH  = 512
PRG_WIDTH  = CMD_WIDTH - LVL_WIDTH

TKN_WIDTH  = 156
TKN_HEIGHT = 48
TKN_PDDNG  = ( CMD_WIDTH - 3 * TKN_WIDTH ) / 4

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

        self.render_text(label, 24)

    def render_text(self, label, font_size):
        font = pygame.font.Font(None, font_size)
        text = font.render(label, True, (255,255,255))

        self.image.blit(text, ((TKN_WIDTH - text.get_width())/2, (TKN_HEIGHT - text.get_height())/2))

class CommandsBox(pygame.sprite.Sprite):
    def __init__(self, commands=['If', 'Then', 'Else', 'Or', 'And']):
        # Call the parent constructor
        super(CommandsBox, self).__init__()

        self.image = pygame.Surface([CMD_WIDTH, 384])
        self.image.fill((200, 200, 200))

        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = LVL_WIDTH

        x, y = LVL_WIDTH + TKN_PDDNG, TKN_PDDNG
        color = (144, 144, 190)
        self._commands = pygame.sprite.Group()
        for command in commands:
            self._commands.add(Command(x, y, TKN_WIDTH, TKN_HEIGHT, color, command))
            x, y = CommandsBox.compute_next_grid_location(x, y)

    @staticmethod
    def compute_next_grid_location(x, y):
        if (TKN_WIDTH + TKN_PDDNG + x) > CMD_WIDTH:
            x = LVL_WIDTH + TKN_PDDNG
            y += TKN_PDDNG + TKN_HEIGHT
        else:
            x += TKN_WIDTH + TKN_PDDNG
        return x, y
