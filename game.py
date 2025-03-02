import pygame

pygame.init()


width = int(input("What size width do you want?(300 - 500): "))

height = int(input("What height width do you want?(300 - 500): "))
is_initialized = pygame.get_init()


myDisplay = pygame.display.set_mode((width, height))


pygame.draw.rect(myDisplay, (10, 25, 255 ), [100, 100, 400, 100], 0)
pygame.display.set_caption('Beans-Tac-Toe')


gamerunning = True

while gamerunning:
    myDisplay.fill((255, 255, 255))
    pygame.display.flip()


    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            gamerunning = False


pygame.quit()
