import pygame

pygame.init()



is_initialized = pygame.get_init()


myDisplay = pygame.display.set_mode((600, 600), pygame.RESIZABLE)

pygame.display.set_caption('Beans-Tac-Toe')


gamerunning = True

while gamerunning:


    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False


pygame.quit()
