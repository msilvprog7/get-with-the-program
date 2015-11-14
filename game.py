import sys, pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Call the parent constructor
        super(Player, self).__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill((255, 255, 255))
        
        # Make our top-left corner the passed-in location
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.speed = [0, 5]

    def update(self):
        self.rect.x += self.speed[0]

        hits = pygame.sprite.spritecollide(self, self.walls, False)
        for hit in hits:
            if self.speed[0] > 0:
                self.rect.right = hit.rect.left
            else:
                self.rect.left = hit.rect.right

        self.rect.y += self.speed[1]

        hits = pygame.sprite.spritecollide(self, self.walls, False)
        for hit in hits:
            if self.speed[1] > 0:
                self.rect.bottom = hit.rect.top
            else:
                self.rect.top = hit.rect.bottom
                

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        # Call the parent constructor
        super(Wall, self).__init__()

        # Make a clue wall, the size of the specified parameters
        self.image = pygame.Surface([width, height])
        self.image.fill((50, 50, 255))

        # Make our top-left corner the passed-in location
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

def add_sprite(sprite, groups):
    for group in groups:
        group.add(sprite)
        
if __name__ == '__main__':
    pygame.init()
 
    framerate = 60
    size = width, height = 1024, 768
    color = 0, 0, 0

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    sprites = pygame.sprite.Group()
    walls = pygame.sprite.Group()

    wall = Wall(0, 0, 10, 600)
    add_sprite(wall, [walls, sprites])
    wall = Wall(10, 0, 790, 10)
    add_sprite(wall, [walls, sprites])
    wall = Wall(10, 200, 100, 10)
    add_sprite(wall, [walls, sprites])

    player = Player(50, 50)
    player.walls = walls
    sprites.add(player)
    
    while True:
        clock.tick(framerate)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        sprites.update()
        screen.fill(color)
        sprites.draw(screen)
        pygame.display.flip()

