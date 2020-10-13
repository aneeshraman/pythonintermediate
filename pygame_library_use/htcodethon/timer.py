# Importing the library pygame.
import pygame

# Initializing pygame.
pygame.init()

# Creating the colors using rgb values.
black = (0, 0, 0)

white = (255, 255, 255)

# Setting up the size of the display screen.
size = (700, 500)

# Displaying the screen.
screen = pygame.display.set_mode(size)

# Setting up the caption.
pygame.display.set_caption("Timers")

# Game loop condition
running = True

# Creating a clock for the timers.
clock = pygame.time.Clock()

# Creating a variable for storing font
# The format is pygame.font.Font(font_name, font_size)
font = pygame.font.Font("Jokerman", 25)
