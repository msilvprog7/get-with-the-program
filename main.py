import pygame
from world.world import World
from editor.editor import Editor
from level import Level
from events.click import delegate

framerate = 60
size = width, height = 1024, 768

colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255)
}

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode(size)
    canvas = pygame.Surface(size)
    clock  = pygame.time.Clock()
    done   = False

    levels = [Level(1, '-------', ['Step']), Level(2, '---_---', ['Step', 'Jump'])]

    world = World(pygame.Rect(0, 0, 1024, 384), colors['black'], canvas)
    editor = Editor(pygame.Rect(0, 384, 1024, 384), colors['white'], canvas, levels[1])

    children = [world, editor]

    while not done:
        clock.tick(framerate)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                delegate(children, event)
            if event.type == pygame.QUIT:
                done = True

        #sprites.update()
        world.draw()
        screen.blit(world.world, (0, 0))
        editor.draw()
        screen.blit(editor._editor, (0, 384))
        #sprites.draw(screen)
        pygame.display.flip()


    pygame.quit()
