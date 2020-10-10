# The increase in x means that the object has moved towards the right. Similarly, the decreasing of x means that the
# objects has moved towards the left.

# The increase in y means that the object has moved downwards. Similarly, the decreasing of y means that the object
# has moved upwards.

# Importing the pygame library
import pygame

# Initializing the pygame library
pygame.init()

# Defining the x and y pixels of the pygame display.
display_coordinates = (1280, 720)

# Creating the display display
display = pygame.display.set_mode(display_coordinates)

# Creating a caption for the game to Game of Squares
pygame.display.set_caption("Game of Squares")

# Creating coordinates (x, y) for the blue square (user controlled square).
blueX = 100
blueY = 100

# Creating coordinates (x, y) for the red square (computer controlled square).
redX = 300
redY = 300

# Setting up the velocity of the blue square to be 6 pixels.
blueVelocity = 6

# Setting up the velocity of the red square tp be 4 pixels.
redVelocity = 4

# As the redVelocity is less than the blueVelocity so, this signifies that the red square (the computer controlled
# square) is slower than the blue square (the player controlled square).

# Setting the width and the height of the blue square.
blueWidth = 20
blueHeight = 20

# Setting the width and the height of the red square.
redWidth = 40
redHeight = 40


# This means that the red square (the computer controlled square) is larger than the blue square (the user controlled
# square).

# Drawing the boxes on the pygame display.
def drawGame():
    # Defining the rgb values of the black color which are (0, 0, 0).
    black = (0, 0, 0)
    # Defining the rgb values of the red color which are (255, 0, 0).
    red = (255, 0, 0)
    # Defining the rgb values of the blue color which are (0, 0, 255).
    blue = (0, 0, 255)
    # Filling black (0, 0, 0) color as the background of the pygame display.
    display.fill(black)
    # Drawing the blue square.
    # To define the shape and place of Rectangle we give its (x, y, width, height)
    # Defining the blue Square (a special Rectangle).
    blueSquare = (blueX, blueY, blueWidth, blueHeight)
    # Drawing the blue square.
    # To draw a rectangle we need to give the surface, the color and then the defined shape and place of rectangle.
    pygame.draw.rect(display, blue, blueSquare)
    # Defining the location and the size of the red square.
    redSquare = (redX, redY, redWidth, redHeight)
    # Drawing the red square.
    pygame.draw.rect(display, red, redSquare)
    # Updating the pygame display.
    pygame.display.update()


# Setting up the running condition for the game loop.
running = True

# Starting with the game loop.
while running:
    # Delaying the loop for 100 milliseconds so that the game loads only after the window is fully loaded.
    pygame.time.delay(100)
    if 0 < redX < 1241 and 0 < redY < 681 and 0 < blueX < 1261 and 0 < blueY < 701:
        if redX + 10 < blueX:
            redX += redVelocity
            drawGame()

        if redX - 10 > blueX:
            redX -= redVelocity
            drawGame()

        if redY - 10 > blueY:
            redY -= redVelocity
            drawGame()

        if redY + 10 < blueY:
            redY += redVelocity
            drawGame()

        if redX + 10 >= blueX >= redX - 10 and redY - 10 <= blueY <= redY + 10:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            blueX -= blueVelocity

        if keys[pygame.K_RIGHT]:
            blueX += blueVelocity

        if keys[pygame.K_UP]:
            blueY -= blueVelocity

        if keys[pygame.K_DOWN]:
            blueY += blueVelocity

    else:
        running = False
