import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

# create game window
screen_width = 1200
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ashen Fields')

bg_images = []
for i in range(1,5):
    bg_image = pygame.image.load(f"assets/background/bg-{i}.png").convert_alpha()
    bg_images.append(bg_image)
    
def draw_bg():
    for i in bg_images:
        screen.blit(i, (0,0))

# gameloop
run = True
while run:

    clock.tick(fps)

    draw_bg()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()