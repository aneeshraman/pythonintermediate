# Importing the pygame library
import pygame

# Initializing the pygame library
pygame.init()

# Setting the size of the display window
display_window_size = (500, 480)

# Creating the display window.
display_window = pygame.display.set_mode(display_window_size)

# Setting up the caption of the display window to be "The Goblin Game".
pygame.display.set_caption("The Goblin Game")

# Creating the right movements of the player.
player_walk_right = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
                     pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
                     pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]

# Creating the left movements of the player.
player_walk_left = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
                    pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
                    pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

# Creating the variable for background image by loading it.
background_image = pygame.image.load("background.jpg")

# Creating the variable for player standing image by loading it.
player_standing_image = pygame.image.load("standing.png")

# Creating a clock to time all the game movements.
clock = pygame.time.Clock()

# Using the mixer load function to load the bullet sound in the bullet sound variable.
bullet_sound = pygame.mixer.Sound("bullet.wav")

# Using the mixer load function to load the music sound in the music sound variable.
music_sound = pygame.mixer.Sound("music.mp3")

# Creating a replaying music player.
pygame.mixer.music.play(-1)

# Setting up the score variable to set up the scores.
score = 0


# Creating a class defining the characteristics of player.
class Player(object):
    # Initializing the Player class.
    def __init__(self, x_coordinate, y_coordinate, width, height):
        # Converting x and y coordinates and width and height to self so that they can be used in the whole class.
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.width = width
        self.height = height
        # Defining the velocity to be 5.
        self.velocity = 5
        # Defining that the player is not jumping by default.
        self.isJump = False
        # Defining jf the player is moving left or not.
        self.left_movement = False
        # Defining if the player is moving right or not.
        self.right_movement = False
        # Creating the walk count to be 0 so that the player doesn't start to move.
        self.walk_count = 0
        # Creating the jumping power to 10
        self.jump_power = 10
        # Defining if the player is standing or not.
        self.standing = True
        # Creating the region where the player would get hurt and would lose points.
        self.hurt_box = ((self.x_coordinate + 17, self.x_coordinate - 17),
                         (self.y_coordinate + 17, self.y_coordinate - 17),
                         29,
                         52
                         )
