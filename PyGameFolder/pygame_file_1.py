import pygame

pygame.init()

WHITE = (255, 255, 255)  
ORANGE = (255, 150, 100)

DISPLAY_WIDTH = 400
DISPLAY_HEIGH = 400 

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGH))

pygame.display.set_caption("My first game")

clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
  # --- Main event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
      print("User asked to quit.")
    elif event.type == pygame.KEYDOWN:
      print("User pressed a key.")
    elif event.type == pygame.KEYUP:
      print("User let go of a key.")
    elif event.type == pygame.MOUSEBUTTONDOWN:
      print("User pressed a mouse button")

    # --- Game logic should go here
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other
    # drawing commands above this,
    # or they will be erased with this command.

    gameDisplay.fill(ORANGE)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()

    # --- Limit to 60 frames per second
    clock.tick(60)
