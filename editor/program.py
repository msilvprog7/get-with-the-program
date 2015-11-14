import pygame
import constants
from constants import hex_to_rgb as h2r

BG_COLOR    = h2r("#333333")
COLOR_WHITE = h2r("#ffffff")

TITLE_SIZE = 30

STARTING_STEPS = ["step", "step", "step", "step"]

class Program(pygame.sprite.Sprite):
    def __init__(self, steps=STARTING_STEPS):
        # Call the parent constructor
        super(Program, self).__init__()

        self.image = pygame.Surface([constants.PRG_WIDTH, 384])
        self.image.fill(BG_COLOR)

        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = constants.LVL_WIDTH + constants.CMD_WIDTH
        self.step_list = steps

        self.render_text()
        self.render_actions()
        self.render_steps()

    def render_actions(self):
        self.actions = ProgramActions()
        right = self.image.get_width() - self.actions.image.get_width()
        self.image.blit(self.actions.image, (right, 10))

    def render_text(self):
        font = constants.get_font(TITLE_SIZE)
        text = font.render("Actions to Run", True, COLOR_WHITE)

        self.image.blit(text, (10, 10))

    def render_steps(self):
        self.steps = ProgramList(self.step_list)
        self.image.blit(self.steps.image, (10, 50))

class ProgramList(pygame.sprite.Sprite):
    BG_COLOR    = h2r("#0BD91E")

    def __init__(self, steps=[]):
        self.image = pygame.Surface([constants.PRG_WIDTH-20, 384-50])
        self.image.fill(BG_COLOR)

        for i, step in enumerate(steps):
            self.render_step(i, step)

    def render_step(self, i, step):
        font = constants.get_font(24)
        text = font.render(step, True, COLOR_WHITE)

        self.image.blit(text, (20, i*30))

class ProgramActions(pygame.sprite.Sprite):
    PLAY_COLOR    = h2r("#0BD91E")
    PAUSE_COLOR   = h2r("#E3AD0B")
    STOP_COLOR    = h2r("#CC0000")
    STEP_COLOR    = h2r("#0085BF")
    DISABLE_COLOR = h2r("#999999")

    ICON_Y = 8

    def __init__(self):
        super(ProgramActions, self).__init__()

        self.image = pygame.Surface([170, 50])
        self.image.fill(BG_COLOR)

        self.render_play(5, 0, True)
        self.render_step(45, 0, True)
        self.render_stop(85, 0, False)
        self.render_pause(125, 0, False)

    def get_ctx(self):
        ctx = pygame.Surface([30, 30])
        ctx.fill(BG_COLOR)
        return ctx

    def enabled_color(self, c, e):
        if e:
            return c
        else:
            return self.DISABLE_COLOR

    def render_play(self, x, y, enabled):
        ctx = self.get_ctx()
        color = self.enabled_color(self.PLAY_COLOR, enabled)
        pygame.draw.polygon(ctx, color,
                            [(0, 0), (0, 30), (30, 15)])
        self.image.blit(ctx, (x, y))

    def render_pause(self, x, y, enabled):
        ctx = self.get_ctx()
        color = self.enabled_color(self.PAUSE_COLOR, enabled)
        pygame.draw.rect(ctx, color, (0, 0, 12, 30))
        pygame.draw.rect(ctx, color, (19, 0, 12, 30))
        self.image.blit(ctx, (x, y))

    def render_stop(self, x, y, enabled):
        ctx = self.get_ctx()
        color = self.enabled_color(self.STOP_COLOR, enabled)
        pygame.draw.rect(ctx, color, (0, 0, 30, 30))
        self.image.blit(ctx, (x, y))

    def render_step(self, x, y, enabled):
        ctx = self.get_ctx()
        color = self.enabled_color(self.STEP_COLOR, enabled)
        pygame.draw.polygon(ctx, color,
                            [(0, 0), (15, 15), (15, 0), (30, 15), (15, 30), (15, 15), (0, 30)])
        self.image.blit(ctx, (x, y))
