import pygame

class Editor:
    def __init__(self, rect, color, canvas):
        self._editor_rect = rect
        self._editor = canvas.subsurface(self._editor_rect)
        self._color = color

    def draw(self):
        self._editor.fill(self._color)
