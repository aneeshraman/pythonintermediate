# Ping Pong.

# Human Algorithm.
# First create a window.
# Then create one bar below
# Then create three or four unfixed bars.
# Then create a ball which would obey laws of motion.
# Computer algorithm.
# Import pygame library
import keyboard
import pygame
import random

# Create displayWidth and displayHeight variables.
displayWidth = 1000
displayHeight = 700

# Create display.

display = pygame.display.set_mode((displayWidth, displayHeight), pygame.RESIZABLE)

# Create the bar below.
white = (255, 255, 255)

bar1X = random.randint(10, display.get_width() // 3 - 100)
bar1Y = random.randint(10, display.get_height() // 2)
bar1Width = 100
bar1Height = 10

bar2X = random.randint(display.get_width() // 3, (display.get_width() * 2 // 3) - 100)
bar2Y = bar1Y
bar2Width = 100
bar2Height = 10

bar3X = random.randint(display.get_width() * 2 // 3, display.get_width() - 100)
bar3Y = bar2Y
bar3Width = 100
bar3Height = 10

black = (0, 0, 0)

ballX = 0
ballY = 0
ballRadius = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    bar = pygame.draw.rect(display, white, pygame.Rect(0, display.get_height() * 4 / 5, display.get_width(), 10))

    # Create unfixed bars.
    bar1 = pygame.draw.rect(display, white, pygame.Rect(bar1X, bar1Y, bar1Width, bar1Height))

    bar2 = pygame.draw.rect(display, white, pygame.Rect(bar2X, bar2Y, bar2Width, bar2Height))

    bar3 = pygame.draw.rect(display, white, pygame.Rect(bar3X, bar3Y, bar3Width, bar3Height))
    if keyboard.is_pressed("right") and bar1X + bar1Width < display.get_width() // 3:
        bar1X += 1

    elif keyboard.is_pressed("left") and bar1X >= 1:
        bar1X -= 1

    if keyboard.is_pressed("d") and bar2X + bar2Width < display.get_width() * 2 // 3:
        bar2X += 1

    elif keyboard.is_pressed("a") and bar2X > display.get_width() // 3:
        bar2X -= 1

    if keyboard.is_pressed("l") and bar3X < display.get_width() - bar3Width:
        bar3X += 1

    elif keyboard.is_pressed("j") and bar3X > display.get_width() * 2 // 3:
        bar3X -= 1

    ball = pygame.draw.circle(display, white, (ballX, ballY), ballRadius)

    pygame.display.update()

    display.fill(black)
