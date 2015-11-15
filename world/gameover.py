import pygame
from editor.constants import get_font
from events.click import ClickHandler

GAME_OVER = pygame.Color(0, 0, 0)
COLOR_BTN = (0, 110, 180)

class GameOver():
    def __init__(self, canvas, rect, world):
        self.rect = rect
        self.image = canvas.subsurface(self.rect)
        self.image.set_alpha(200)
        self.world = world

    def click(self, event):
        if self.btn_rect.collidepoint(event.pos):
            self.world.game_over = False
            self.world.restart()

    def draw_button(self):
        btn_surface = pygame.Surface([300, 70])
        btn_surface.fill(COLOR_BTN)

        text = get_font(50).render("Try again?", True, (255, 255, 255))

        self.draw_center(text, btn_surface)
        (btn_x, btn_y) = self.draw_center(btn_surface, self.image)
        self.btn_rect = pygame.Rect(btn_x, btn_y, 300, 70)
        
    def draw_center(self, source, dest, offx = 0, offy = 0):
        w, h = source.get_width(), source.get_height()
        pw, ph = dest.get_width(), dest.get_height()

        dw, dh = ((pw / 2) - (w / 2) + offx), ((ph / 2) - (h / 2) + offy)

        dest.blit(source, (dw, dh))
        return (dw, dh)

    def draw(self):
        self.image.fill(GAME_OVER)

        text = get_font(100).render("You found a bug!", True, (255, 255, 255))

        self.draw_center(text, self.image, 0, -100)
        
        w, h = text.get_width(), text.get_height()
        pw, ph = self.image.get_width(), self.image.get_height()

        dw = (pw / 2) - (w / 2)
        dh = (ph / 2) - (h / 2)
        
        self.image.blit(text, (dw, dh - 100))
        self.draw_button()
