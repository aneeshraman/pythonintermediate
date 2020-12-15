import pygame
pygame.init()
display = pygame.display.set_mode((1000, 700), pygame.RESIZABLE)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(display, (255, 255, 255), pygame.Rect(0, 0, 30, 30))
    pygame.display.update()
