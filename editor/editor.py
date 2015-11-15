import pygame

from command import Command, CommandsBox
from program import Program
from events.click import ClickHandler
from levels import Levels, LevelBox

class Editor(ClickHandler):
    def __init__(self, rect, color, canvas, levels, world):
        self._editor_rect = rect
        self._editor = canvas.subsurface(self._editor_rect)
        self._color = color
        self._level = levels

        self._program = pygame.sprite.Group()
        self._program.add(Program(world))

        self._commands = pygame.sprite.Group()
        self._commands.add(CommandsBox(levels, self._program.sprites()[0], world, self))

        self._levels = pygame.sprite.Group()
        self._levels.add(Levels(1))
        
        self.update_children()

    def update_children(self):
        self.children = []

        if len(self._commands.sprites()) == 1:
            for command in self._commands.sprites()[0]._commands:
                self.children.append(command)

        if len(self._program.sprites()) == 1:
            self.children.append(self._program.sprites()[0])

        if len(self._levels.sprites()) == 1:
            for box in self._levels.sprites()[0]._boxes:
                self.children.append(box)

    def draw(self):
        self._editor.fill(self._color)

        self._commands.update()
        self._commands.draw(self._editor)
        for box in self._commands:
            box._commands.draw(self._editor)

        self._program.update()
        self._program.draw(self._editor)

        self._levels.update()
        self._levels.draw(self._editor)
        for level in self._levels:
            level._boxes.draw(self._editor)
