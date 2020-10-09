import pygame

# Initialize the pygame
pygame.init()

playerImg = pygame.image.load('player.png')


# Player
def player(input_x, input_y):
    screen.blit(playerImg, (input_x, input_y))


running = True
while running:
    # Create the screen
    screen_x = int(input("Enter window screen x coordinate "))
    screen_y = int(input("Enter window screen y coordinate "))
    screen = pygame.display.set_mode((screen_x, screen_y))
    screen.fill((0, 0, 0))
    # Player
    player_x = input("Enter player x coordinate ")
    player_y = input("Enter player y coordinate ")

    player(player_x, player_y)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
