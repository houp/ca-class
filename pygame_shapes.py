import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Pygame demo")
clock = pygame.time.Clock()

i=0
j=0

running = True
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

    screen.fill((0, 0, 0))
    
    i = (i+1) % 5
    j = (j+1) % 10
    
    rect = pygame.Rect(100*i, 50*j, 20-i, 20+j)
    color_green = (0, 255, 0) 
    pygame.draw.rect(screen, color_green, rect)
    
    color_red = (255, 0, 0) 
    pygame.draw.circle(screen, color_red, (500 - 100*i, 500 - 50*j), 20+i+j)
    
    pygame.display.flip()
    clock.tick(10)
    
pygame.quit()