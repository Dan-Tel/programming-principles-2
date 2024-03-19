import pygame
import datetime

pygame.init()

SCREEN_WIDTH = 829
SCREEN_HEIGHT = 836
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False
clock = pygame.time.Clock()

clock_img = pygame.image.load("Lab7\images\main-clock.png")
left_hand = pygame.image.load("Lab7\images\left-hand.png")
right_hand = pygame.image.load("Lab7\images\\right-hand.png")

def get_center(screen_w, screen_h, w, h):
  return ((screen_w - w) // 2, (screen_h - h) // 2)

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  screen.blit(clock_img, get_center(SCREEN_WIDTH, SCREEN_HEIGHT, clock_img.get_width(), clock_img.get_height()))

  now = datetime.datetime.now()
  rotated_left_hand = pygame.transform.rotate(left_hand, -now.second * 6 + 90)
  rotated_right_hand = pygame.transform.rotate(right_hand, -now.minute * 6 + 90)

  screen.blit(rotated_left_hand, get_center(SCREEN_WIDTH, SCREEN_HEIGHT, rotated_left_hand.get_width(), rotated_left_hand.get_height()))
  screen.blit(rotated_right_hand, get_center(SCREEN_WIDTH, SCREEN_HEIGHT, rotated_right_hand.get_width(), rotated_right_hand.get_height()))
  pygame.display.flip()

  clock.tick(FPS)