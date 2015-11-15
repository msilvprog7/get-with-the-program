import pygame
import constants
from constants import hex_to_rgb as h2r
from events.click import ClickHandler

BG_COLOR    = h2r("#333333")
COLOR_WHITE = h2r("#ffffff")

TITLE_SIZE = 30

STARTING_STEPS = ["Step", "Step", "Step", "Step"]

class Program(pygame.sprite.Sprite,ClickHandler):
    def __init__(self, world, steps=STARTING_STEPS):
        # Call the parent constructor
        super(Program, self).__init__()
        self.children = []

        self.image = pygame.Surface([constants.PRG_WIDTH, 384])
        self.image.fill(BG_COLOR)

        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = constants.LVL_WIDTH + constants.CMD_WIDTH
        self.step_list = steps

        self.render_text()

        self.render_actions(world)
        self.children.append(self.actions)

        self.render_steps()
        self.children.append(self.steps)

    def render_actions(self, world):
        self.actions = ProgramActions(0, 0, self.step_list, world)
        right = self.image.get_width() - self.actions.image.get_width()
        self.actions.rect.x = right
        self.actions.rect.y = 10
        self.image.blit(self.actions.image, (right, 10))

    def render_text(self):
        font = constants.get_font(TITLE_SIZE)
        text = font.render("Actions to Run", True, COLOR_WHITE)

        self.image.blit(text, (10, 10))

    def render_steps(self):
        self.steps = ProgramList(10, 50, self.step_list, self)
        self.image.blit(self.steps.image, (10, 50))

class ProgramList(pygame.sprite.Sprite):
    BG_COLOR    = h2r("#0085BF")

    def __init__(self, x, y, steps, parent):
        self.image = pygame.Surface([constants.PRG_WIDTH-20, 384-50])
        self.image.fill(self.BG_COLOR)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.steps = steps
        self.parent = parent

        for i, step in enumerate(steps):
            self.render_step(i, step)

    def click(self, event):
        y = event.pos[1] - self.rect.y
        pos = y / 30

        if pos < len(self.steps):
            ns = []
            for i, step in enumerate(self.parent.step_list):
                if i != pos: ns.append(step)
            self.parent.step_list = ns
            self.steps = ns
            print "deleted", pos
        print "clicked item", pos

        self.image.fill(self.BG_COLOR)
        for i, step in enumerate(self.steps):
            self.render_step(i, step)

        self.parent.image.blit(self.image, (10, 50))

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

    def __init__(self, x, y, l, world):
        super(ProgramActions, self).__init__()

        self.image = pygame.Surface([170, 50])
        self.image.fill(BG_COLOR)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.step_list = l
        self.world = world
        
        self.render_play(5, 0, True)
        self.render_step(45, 0, True)
        self.render_stop(85, 0, False)
        self.render_pause(125, 0, False)

    def click(self, event):
        x = event.pos[0] - self.rect.x
        print x, self.rect.x

        if x > 5 and x <= 35:
            print "clicked play"
            self.world.run(self.step_list)
        elif x > 45 and x <= 75:
            print "clicked step"
        elif x > 85 and x <= 115:
            print "clicked stop"
            self.world.restart()
        elif x > 125:
            print "clicked pause"
            self.world.pause()

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
