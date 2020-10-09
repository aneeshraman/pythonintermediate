import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((800, 600))

gameDisplay.fill(black)
displayer = pygame.PixelArray(gameDisplay)

pygame.draw.line(gameDisplay, blue, (100, 200), (300, 450), 5)  # A line having the starting point to be (100, 200) and ending point to be (300, 450) and the thickness to be 5 pixels
pygame.draw.rect(gameDisplay, red, (400, 400, 50, 25))  # A rectangle which starts at the position (400, 400) and has a width of 50 pixels and a height of 25 pixels
pygame.draw.circle(gameDisplay, white, (150, 150), 75)  # A circle with a center at (150, 150) and radius of 75 pixels
pygame.draw.polygon(gameDisplay, green, ((25, 75), (76, 125), (250, 375), (400, 25), (60, 540)))    # A five sided figure with the end points being at coordinates (25, 75), (76, 125), (250, 375), (400, 25), (60, 540)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
