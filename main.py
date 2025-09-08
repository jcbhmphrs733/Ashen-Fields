import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

# create game window
screen_width = 1600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ashen Fields')

# gameloop
run = True
while run:

    clock.tick(fps)

    # draw background
    screen.fill((202, 228, 241))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()