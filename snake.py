# Human Algorithm. Ejecting machine algorithm.

#   Importing pygame library
import pygame
#   Importing keyboard library.
import keyboard

# Create display

#   Creating the displayWidth
displayWidth = 1000
#   Creating the displayHeight
displayHeight = 700
#   Creating the display
display = pygame.display.set_mode((displayWidth, displayHeight), pygame.RESIZABLE)
#   Recreating the displayWidth.
displayWidth = display.get_width()
#   Recreating the displayHeight
displayHeight = display.get_height()

# Create snake head. Note that the original position of the snake is it's center.

#   Creating the colors.
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
#   Creating snakeHeadX
snakeHeadX = (displayWidth / 2)
#   Creating snakeHeadY
snakeHeadY = (displayHeight / 2)
#   Creating snakeHeadWidth
snakeHeadWidth = 20
#   Creating snakeHeadHeight
snakeHeadHeight = 20
# Create snake tail.

#   Creating snakeTailX
snakeTailX = (snakeHeadX - 20)
#   Creating snakeTailY
snakeTailY = snakeHeadY
#   Creating snakeTailWidth
snakeTailWidth = 20
#   Creating snakeTailHeight
snakeTailHeight = 20

# Create fruit.

#   Creating fruitWidth
fruitWidth = 10
#   Creating fruitHeight
fruitHeight = 10
#   Creating fruitX.
import random
fruitX = random.randint(0, displayWidth-fruitWidth)
#   Creating fruitY
fruitY = random.randint(0, displayHeight-fruitHeight)
#   Creating fruit on rectangle on screen.
fruit = pygame.draw.rect(display, red, pygame.Rect(fruitX, fruitY, fruitWidth, fruitHeight))

# Display snake at every iteration of game loop.

#   Creating the game loop.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    # Display fruit at another location if snake eats the previous fruit.

    #   Creating snakeHead rectangle on the screen.
    snakeHead = pygame.draw.rect(display, blue, pygame.Rect(snakeHeadX, snakeHeadY, snakeHeadWidth, snakeHeadWidth))

    #   Creating snakeTail rectangle on the screen.
    snakeTail = pygame.draw.rect(display, blue, pygame.Rect(snakeTailX, snakeTailY, snakeTailWidth, snakeTailHeight))

    #   Taking input from the user.
    #       Taking right input from the user.
    if keyboard.is_pressed("right") and snakeHeadX + snakeHeadWidth <= displayWidth and snakeHeadY <= displayHeight:
        snakeTailX += 1
        snakeHeadX += 1

    #       Taking left input from the user.

    #   Updating the display
    pygame.display.update()

    #   Empty display
    display.fill(black)

