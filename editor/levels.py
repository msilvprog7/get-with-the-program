from constants import *
import pygame

class Levels(pygame.sprite.Sprite):
    def __init__(self, current):
        super(Levels, self).__init__()

        self._current = current
        self._count = count

        self.image = pygame.Surface([LVL_WIDTH, 384])
        self.image.fill(hex_to_rgb("#333333"))

        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 0

        self._boxes = pygame.sprite.Group()

        to_display = min(6, current)
        pos = 0
        for i in range(current - to_display + 1, to_display):
            self._boxes.add(LevelBox(i, False, pos))
            pos += 1
        self._boxes.add(LevelBox(to_display, True, pos))



class LevelBox(pygame.sprite.Sprite):
    def __init__(self, number, completed, position):
        super(LevelBox, self).__init__()
