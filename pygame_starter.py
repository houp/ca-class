import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Pygame demo")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

    screen.fill((0, 0, 0))
    
    # drawing goes here
    
    pygame.display.flip()
    clock.tick(10)
    
pygame.quit()