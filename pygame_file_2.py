import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((400, 300))
pygame.display.set_caption("My first game")
clock = pygame.time.Clock()
crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit.")
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")

    pygame.display.update()

    clock.tick(60)

pygame.quit()
# quit()