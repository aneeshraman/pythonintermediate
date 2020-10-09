import pygame

pygame.init()
win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Game of Squares")
blueX = 100
blueY = 100
redX = 300
redY = 300
blueVelocity = 6
redVel = 4
run = True


def drawGame():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (blueX, blueY, 20, 20))
    pygame.draw.rect(win, (255, 0, 0), (redX, redY, 40, 40))
    pygame.display.update()


while run:
    if 0 < blueX < 1260 and 0 < blueY < 700 and 0 < redX < 1240 and 0 < redY < 680:
        pygame.time.delay(100)

        if redX < blueX - 10:
            redX = redX + redVel
            drawGame()

        elif redX > blueX + 10:
            drawGame()
            redX = redX - redVel

        elif redY < blueY - 10:
            redY = redY + redVel

        elif redY > blueY + 10:
            redY = redY - redVel

        else:
            run = False

    else:
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        blueX -= blueVelocity

    if keys[pygame.K_RIGHT]:
        blueX += blueVelocity

    if keys[pygame.K_UP]:
        blueY -= blueVelocity

    if keys[pygame.K_DOWN]:
        blueY += blueVelocity

    drawGame()
    print(redX, redY, blueX, blueY)

pygame.quit()
