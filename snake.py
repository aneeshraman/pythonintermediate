# Basic Snake game with no size increase.
# Algorithm
# First import pygame library. Also import random library.
import pygame

# Then create the display window using pygame. Make sure that the window is resizable.
width = 100
height = 700
display = pygame.display.set_mode((width, height), pygame.RESIZABLE)

# Create the colors.
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# Next create a class for the snake. The snake would contain two boxes. These boxes are the head and tail of
# the snake. I can assign the starting of the snake to be anywhere (specific location).
# Try keeping the size of the head to be 10 x 10
class Snake:
    # Initializing the snake class
    def __init__(self):
        # Creating the moveX variable.
        self.moveX = 10
        # Creating the moveY variable.
        self.moveY = 10
        # First creating the coordinates for the topLeft position of the head.
        self.topLeftSnakeHead = (width * 1 / 2, height * 4 / 7)
        # Creating the snake head.
        self.snakeHead = pygame.draw.rect(display,
                                          blue,
                                          pygame.Rect(self.topLeftSnakeHead[0], self.topLeftSnakeHead[1],
                                                      10, 10)
                                          )

        # First creating the coordinates for the topLeft position of the tail.
        self.topLeftSnakeTail = (width * 1 / 2 + 10, height * 4 / 7)
        # Creating the snake tail.
        self.snakeTale = pygame.draw.rect(display,
                                          blue,
                                          pygame.Rect(self.topLeftSnakeTail[0], self.topLeftSnakeTail[1],
                                                      10, 10))

    def moveDown(self):
        # First creating the coordinates for the topLeft position of the head.
        self.topLeftSnakeHead = (self.topLeftSnakeHead[0], self.topLeftSnakeHead[1] + self.moveY)
        # Now creating the coordinates for the topLeft position of the head.
        self.topLeftSnakeTail = (self.topLeftSnakeHead[0], self.topLeftSnakeTail[1])

    def moveRight(self):
        # First creating the coordinates for the topLeft position of the head.
        self.topLeftSnakeHead = (self.topLeftSnakeHead[0] + self.moveX, self.topLeftSnakeHead[1])
        # Now creating the coordinates for the topLeft position of the tail.
        self.topLeftSnakeTail = (self.topLeftSnakeTail[0] + self.moveX, self.topLeftSnakeTail[1])

    def moveLeft(self):
        # First creating the coordinates for the topLeft position of the head.
        self.topLeftSnakeHead = (self.topLeftSnakeHead[0] + self.moveX, self.topLeftSnakeHead[1])

        # Now creating the coordinates for the topLeft position of the tail.
        self.topLeftSnakeTail = (self.topLeftSnakeTail[0] + self.moveX, self.topLeftSnakeTail[1])

    def moveUp(self):
        # First creating the coordinates for the topLeft position of the head.
        self.topLeftSnakeHead = (self.topLeftSnakeHead[0], self.topLeftSnakeHead[1] + self.moveY)

        # Now creating the coordinates for the topLeft position of the tail.
        self.topLeftSnakeTail = (self.topLeftSnakeHead[0], self.topLeftSnakeTail[1])


# Next create a class for the fruit. The fruit can have a random location on the screen.
class Fruit:
    # Initializing the fruit class.
    def __init__(self):
        # First creating the coordinates for the topLeft position of the head.
        pass
# Next create the frames per second variable. So that you can increase the speed of the game using this
# variable.
# Next create the movement x and movement y variables which would ensure the movement in the x and y
# direction.
# Next create the game loop. Remember to put the quit conditions in the game loop. Also remember to update
# the display after the fruit and the snake are created.
