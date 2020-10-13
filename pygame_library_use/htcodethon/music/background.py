# Importing the library pygame
import pygame

# Initializing pygame
pygame.init()

# Displaying the window
display_surface = pygame.display.set_mode((400, 400))
# Adding a caption to the display surface
pygame.display.set_caption("Image")

# Storing the background image in a variable
background_image = pygame.image.load(r"background.jpeg")

# Game loop
while True:
    # Defining the rgb values of colors
    white = (255, 255, 255)

    # Adding the white color to the background
    display_surface.fill(white)

    # To display a background image use the blit function present in the surface.
    # This function has the format(background_image, (0, 0))
    display_surface.blit(background_image, (0, 0))

    # Creating the program for exiting when the exit button is clicked.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        pygame.display.update()
