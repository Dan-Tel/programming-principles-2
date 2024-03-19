import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BALL_RADIUS = 25
SPEED = 20
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
done = False

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

moving_up = moving_down = moving_left = moving_right = False

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        moving_up = True
      elif event.key == pygame.K_DOWN:
        moving_down = True

      if event.key == pygame.K_LEFT:
        moving_left = True
      elif event.key == pygame.K_RIGHT:
        moving_right = True
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_UP:
        moving_up = False
      elif event.key == pygame.K_DOWN:
        moving_down = False

      if event.key == pygame.K_LEFT:
        moving_left = False
      elif event.key == pygame.K_RIGHT:
        moving_right = False
  
  if moving_up:
    if y >= BALL_RADIUS:
      norm_coef = 1

      if (moving_left or moving_right):
        norm_coef = 1 / (2 ** (1 / 2))

      y -= norm_coef * SPEED
  elif moving_down:
    if y < SCREEN_HEIGHT - BALL_RADIUS:
      norm_coef = 1

      if (moving_left or moving_right):
        norm_coef = 1 / (2 ** (1 / 2))

      y += norm_coef * SPEED
    
  if moving_left:
    if x >= BALL_RADIUS:
      norm_coef = 1

      if (moving_up or moving_down):
        norm_coef = 1 / (2 ** (1 / 2))

      x -= norm_coef * SPEED
  elif moving_right:
    if x <= SCREEN_WIDTH - BALL_RADIUS:
      norm_coef = 1
      
      if (moving_up or moving_down):
        norm_coef = 1 / (2 ** (1 / 2))

      x += norm_coef * SPEED
  
  screen.fill(WHITE)
  pygame.draw.circle(screen, RED, (x, y), BALL_RADIUS)
  pygame.display.flip()

  clock.tick(FPS)