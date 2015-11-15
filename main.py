import pygame
from world.world import World
from world.characters import Player
from world.gameover import GameOver

from editor.editor import Editor
from level import Level
from events.click import delegate

framerate = 60
size = width, height = 1024, 768

colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'green': (0, 255, 0)
}

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode(size)
    canvas = pygame.Surface(size)
    clock  = pygame.time.Clock()
    done   = False

    # World units
    unit_size = (64, 64)

    # Create main entities
    player = Player(position=(0, 0), size=unit_size, color=colors['green'])
    player.set_sprite_sheet("resources/blob_hero.bmp")

    levels = [Level(1, '---------------!', ['Step'], (0, 192), unit_size), \
        Level(2, '---_-_----_----!', ['Step', 'Jump'], (0, 192), unit_size), \
        Level(3, '---__-_--------!', ['Step', 'Jump', 'Walk', 'Run'], (0, 192), unit_size), \
        Level(4, '------^--^---_-!', ['Step', 'Jump', 'Walk', 'Run', 'Roll'], (0, 192), unit_size), \
        Level(5, '---^^---__--^--!', ['Step', 'Jump', 'Walk', 'Run', 'Roll'], (0, 192), unit_size), \
        Level(6, '---__---^^-_-_-!', ['Step', 'Jump', 'Walk', 'Run', 'Roll'], (0, 192), unit_size), \
        Level(7, '--&-_---^^--_--!', ['Step', 'Jump', 'Walk', 'Run', 'Roll'], (0, 192), unit_size), \
        Level(8, '-^---&&--^---^^!', ['Step', 'Jump', 'Walk', 'Run', 'Roll'], (0, 192), unit_size), \
        Level(9, '---^^-^^-^^-^^-!', ['Step', 'Jump', 'Walk', 'Run', 'Roll'], (0, 192), unit_size), \
        Level(10, '-_-^-_-&---__-!', ['Step', 'Jump', 'Walk', 'Run', 'Roll'], (0, 192), unit_size)]
    
    world_rect = pygame.Rect(0, 0, 1024, 384)
    world = World(canvas, world_rect, colors['white'], player, levels)
    game_over = GameOver(canvas, world_rect, world)
    world.set_bg(pygame.transform.scale(pygame.image.load("resources/background2.bmp"), (1024, 384)))

    editor = Editor(pygame.Rect(0, 384, 1024, 384), colors['white'], canvas, levels, world)

    children = [editor, game_over]

    

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

        if world.game_over:
            game_over.draw()
            screen.blit(game_over.image, (0, 0))
        
        editor.draw()
        screen.blit(editor._editor, (0, 384))
        #sprites.draw(screen)
        pygame.display.flip()


    pygame.quit()
