from constants import *
import pygame

class Levels(pygame.sprite.Sprite):
    def __init__(self, current):
        super(Levels, self).__init__()

        self._current = current

        self.image = pygame.Surface([LVL_WIDTH, 384])
        self.image.fill(hex_to_rgb("#333333"))

        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 0

        self._boxes = pygame.sprite.Group()

        to_display = min(6, current)
        pos = 0
        for i in range(current - to_display + 1, to_display):
            self._boxes.add(LevelBox(i, True, pos))
            pos += 1
        self._boxes.add(LevelBox(to_display, False, pos))



class LevelBox(pygame.sprite.Sprite):
    def __init__(self, number, completed, position):
        super(LevelBox, self).__init__()
        text_color = "#FFFFFF"

        self.image = pygame.Surface([LVL_WIDTH, LVL_HEIGHT])
        if completed:
            self.image.fill(hex_to_rgb("#333333"))
            text_color = "#CCCCCC"
        else:
            self.image.fill(hex_to_rgb("#555555"))

        self.rect = self.image.get_rect()
        self.rect.y = position * 64
        self.rect.x = 0

        font = get_font(TOKEN_SIZE)
        text = font.render(str(number), True, hex_to_rgb(text_color))

        self.image.blit(text, ((LVL_WIDTH - text.get_width())/2, (LVL_HEIGHT - text.get_height())/2))
