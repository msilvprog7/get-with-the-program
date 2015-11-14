import pygame

from command import Command, CommandsBox
from program import Program

class Editor:
    def __init__(self, rect, color, canvas, level):
        self._editor_rect = rect
        self._editor = canvas.subsurface(self._editor_rect)
        self._color = color
        self._level = level

        self._commands = pygame.sprite.Group()
        self._commands.add(CommandsBox(level._tokens))

        self._program = pygame.sprite.Group()
        self._program.add(Program())

    def draw(self):
        self._editor.fill(self._color)
        self._commands.draw(self._editor)
        for box in self._commands:
            box._commands.draw(self._editor)
        self._program.draw(self._editor)