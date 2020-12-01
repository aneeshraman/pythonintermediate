"""
Everything in pygame is surface. For example the game window/screen is a surface in fact. The objects drawn
on the window/screen are also examples of surfaces.

Events are user inputs. For example, the keys pressed, the left clicks of the mouse, etc.

We have to create a normal surface and then place it on the screen but the display surface is visible by default.
That means that you just need to create it.

There are two ways to get color. The pygame.Color("") function which contains some colors. Other method is to use
rgb which literally stands for red green blue.

Remember that when placing an object we are giving the coordinates for the top-left region of the object.

To create vectors in python we need to use the pygame.math.Vector2 for 2d and pygame.math.Vector3 for 3d.
"""

# Importing the pygame library.
import pygame

# Importing the random library.
import random

# Importing the vector2 function specifically
from pygame import Vector2

# Importing the sys library. The sys library is basically used to give system functionality to our code.
import sys


# Creating the Snake class to control the snake.
class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            # Creating the x and y positions
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size

            # Creating the rectangle for each block
            snake_rectangles = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            # Drawing the rectangles
            pygame.draw.rect(screen, (183, 111, 122), snake_rectangles)

    # Creating a method to move a snake
    def move_snake(self):
        body_copy = self.body[:-1]

        # Adding a new element to our body_copy at index 0.
        body_copy.insert(0, body_copy[0] + self.direction)


# Creating the Fruit class to control the fruit.
class Fruit:
    def __init__(self):
        # Creating the x and y coordinates of the fruit.
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        # Creating the rectangle
        fruit_rectangle = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)

        # Drawing the fruit rectangle.
        pygame.draw.rect(screen, (126, 166, 114), fruit_rectangle)


# Initializing pygame library.
pygame.init()

# Creating a screen for our game.
cell_size = 30
cell_number = 20
screen = pygame.display.set_mode(size=(cell_number * cell_size, cell_number * cell_size))

# Creating a clock that would maintain the speed of the while loop.
clock = pygame.time.Clock()

# Creating a instance of the fruit class
fruit = Fruit()

# Creating a instance of the snake class
snake = Snake()

# Creating a timer which would alert in 150 milliseconds. The screen_update is specifying a custom event and a time
# is being set up in the next line. This timer beeps in 150 milliseconds
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# Creating the game loop (Important)
while True:
    # Creating the event loop.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Checking if the event is occurring to according to our time.
        if event.type == SCREEN_UPDATE:
            snake.move_snake()

    # Coloring the original screen.
    screen.fill((175, 215, 70))

    # Drawing a fruit.
    fruit.draw_fruit()

    # Drawing the snake
    snake.draw_snake()

    # update all the changes `repeatedly` because of the while True loop.
    pygame.display.update()

    # So now I would set the frame rate that means that how many times the while loop can run per second.
    # Basically, 60 refers to the frame rate.
    clock.tick(60)
