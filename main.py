import pygame
from world.world import World
from world.characters import Player
from editor.editor import Editor

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

    # Create main entities
    player = Player(position=(0, 0), size=(15, 15), color=colors['white'])
    world = World(canvas, pygame.Rect(0, 0, 1024, 384), colors['black'], player)
    editor = Editor(pygame.Rect(0, 384, 1024, 384), colors['white'], canvas)
    
    while not done:
        clock.tick(framerate)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: done = True

        #sprites.update()
        world.draw()
        screen.blit(world.world, (0, 0))
        editor.draw()
        screen.blit(editor._editor, (0, 384))
        #sprites.draw(screen)
        pygame.display.flip()


    pygame.quit()
