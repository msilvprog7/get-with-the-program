import pygame
from command import PRG_WIDTH, LVL_WIDTH, CMD_WIDTH

std_padding = (10,10)
white = (255, 255, 255)
font_size = 30

class Program(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent constructor
        super(Program, self).__init__()

        self.image = pygame.Surface([PRG_WIDTH, 384])
        self.image.fill((50, 50, 50))

        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = LVL_WIDTH + CMD_WIDTH

        self.render_text()
        self.render_actions()

    def render_actions(self):
        self.actions = ProgramActions()
        right = self.image.get_width() - self.actions.image.get_width()
        self.image.blit(self.actions.image, (right, 0))

    def render_text(self):
        font = pygame.font.Font(None, font_size)
        text = font.render("Actions to Run", True, white)

        self.image.blit(text, std_padding)

class ProgramList(pygame.sprite.Sprite):
    pass

class ProgramActions(pygame.sprite.Sprite):
    def __init__(self):
        super(ProgramActions, self).__init__()

        self.image = pygame.Surface([200, 50])
        self.image.fill((225, 225, 225))

        self.render_play(0, 0)
        self.render_stop(35, 0)
        self.render_pause(70, 0)

    def render_play(self, x, y):
        ctx = pygame.Surface([30, 30])
        pygame.draw.polygon(ctx, (0, 255, 0),
                            [(0, 0), (0, 30), (30, 15)])
        self.image.blit(ctx, (x, y))

    def render_pause(self, x, y):
        ctx = pygame.Surface([30, 30])
        pygame.draw.rect(ctx, (255, 255, 0), (0, 0, 12, 30))
        pygame.draw.rect(ctx, (255, 255, 0), (19, 0, 12, 30))
        self.image.blit(ctx, (x, y))

    def render_stop(self, x, y):
        ctx = pygame.Surface([30, 30])
        pygame.draw.rect(ctx, (255, 0, 0), (0, 0, 30, 30))
        self.image.blit(ctx, (x, y))

    def render_step(self, x, y):
        pass

    
