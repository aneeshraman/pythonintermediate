import pygame

pygame.init()

white = (255, 255, 255)

black = (0, 0, 0)

red = (255, 0, 0)

green = (0, 255, 0)

blue = (0, 0, 255)

screen_size = (800, 600)

gameDisplay = pygame.display.set_mode(screen_size)
start_pos = (100, 100)

end_pos = (100, 200)

pygame.draw.line(gameDisplay, blue, start_pos, end_pos,
                 5)
# Syntax pygame_library_use.draw.line(Surface, Color, start_pos, end_pos)

pygame.draw.rect(gameDisplay, blue,
                 (400, 400, 50, 25))
# Syntax pygame_library_use.draw.rect(Surface, Color, Rect(start_pos, width, height))

pygame.display.update()

pygame.draw.circle(gameDisplay, white, (300, 300),
                   100)
# Syntax pygame_library_use.draw.circle(Surface, Color, center_coord, radius)

pygame.draw.polygon(gameDisplay, green, (
    (25, 75), (76, 125), (250, 375), (400, 200)
)
                    )
# Syntax pygame_library_use.draw.polygon(Surface, color, pointlist)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
