import pygame
import random

pygame.init()

def detect_collision(dx, dy, ball, rect):
  if dx > 0:
    delta_x = ball.right - rect.left
  else:
    delta_x = rect.right - ball.left
  if dy > 0:
    delta_y = ball.bottom - rect.top
  else:
    delta_y = rect.bottom - ball.top

  if abs(delta_x - delta_y) < 10:
    dx, dy = -dx, -dy
  if delta_x > delta_y:
    dy = -dy
  elif delta_y > delta_x:
    dx = -dx
  return dx, dy


def generate_map(map):
  block_list = []
  for i in range(len(map)):
    for j in range(len(map[i])):
      if map[i][j] != 'M' and map[i][j] != 'S':
        block_list.append({
          "pos": (i, j),
          "block": pygame.Rect(75 * j, 25 * i, 75, 25),
          "breakable": True,
          "stretch": False
        })
      elif map[i][j] == 'M':
        block_list.append({
          "pos": (i, j),
          "block": pygame.Rect(75 * j, 25 * i, 75, 25),
          "breakable": False,
          "stretch": False
        })
      elif map[i][j] == 'S':
        block_list.append({
          "pos": (i, j),
          "block": pygame.Rect(75 * j, 25 * i, 75, 25),
          "breakable": True,
          "stretch": True
        })
  return block_list


def main():
  done = False
  W, H = 675, 700
  FPS = 60

  screen = pygame.display.set_mode((W, H))
  clock = pygame.time.Clock()

  # Paddle
  paddle_width = 150
  paddle_height = 25
  paddle_speed = 20
  paddle_width_change = 0.015
  paddle = pygame.Rect(W // 2 - paddle_width // 2, H - paddle_height - 30, paddle_width, paddle_height)
  paddle_img = pygame.image.load("Lab8\\arkanoid\images\paddle.png");

  # Ball
  ball_radius = 10
  ball_speed = 6
  ball_speed_change = 0.0015
  ball_rect = int(ball_radius * 2 ** 0.5)
  ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
  dx, dy = 1, -1

  # Game Score
  game_score = 0
  game_score_fonts = pygame.font.SysFont('comicsansms', 40)
  game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
  game_score_rect = game_score_text.get_rect()
  game_score_rect.center = (210, 20)

  # Catching Sound
  collision_sound = pygame.mixer.Sound('Lab8\\arkanoid\\audio\catch.mp3')

  # Block Settings
  red_block = pygame.image.load("Lab8\\arkanoid\images\\red-block.png")
  orange_block = pygame.image.load("Lab8\\arkanoid\images\orange-block.png")
  green_block = pygame.image.load("Lab8\\arkanoid\images\green-block.png")
  cyan_block = pygame.image.load("Lab8\\arkanoid\images\cyan-block.png")
  blue_block = pygame.image.load("Lab8\\arkanoid\images\\blue-block.png")
  purple_block = pygame.image.load("Lab8\\arkanoid\images\purple-block.png")
  metal_block = pygame.image.load("Lab8\\arkanoid\images\metal-block.png")
  stretch_block = pygame.image.load("Lab8\\arkanoid\images\stretch-block.png")

  map_1 = [
    "MMMMMMMMM",
    "MGORMROGM",
    "SORRRRROS",
    "CGORRROGC",
    "BCGOROGCB",
    "PBCGOGCBP"
  ]

  block_list = generate_map(map_1)
  color_list = [red_block, orange_block, green_block, cyan_block, blue_block, purple_block, metal_block, stretch_block]
  color_id = {"R": 0, "O": 1, "G": 2, "C": 3, "B": 4, "P": 5, "M": 6, "S": 7}

  # Background
  background = pygame.image.load("Lab8\\arkanoid\images\\background.png")

  # Game Vver Screen
  lose_font = pygame.font.SysFont('comicsansms', 40)
  lose_text = lose_font.render('Game Over', True, (255, 255, 255))
  lose_text_rect = lose_text.get_rect()
  lose_text_rect.center = (W // 2, H // 2)

  # Game Over Flag
  flag_game_over = False

  # Win Screen
  win_font = pygame.font.SysFont('comicsansms', 40)
  win_text = win_font.render('You win yay', True, (0, 0, 0))
  win_text_rect = win_text.get_rect()
  win_text_rect.center = (W // 2, H // 2)

  # Restart Screen
  restart_font = pygame.font.SysFont('comicsansms', 40)
  restart_text = restart_font.render('Restart', True, (255, 255, 255))
  restart_text_rect = restart_text.get_rect()
  restart_text_rect.center = (W // 2, H // 2 + 100)

  # Ball Trail
  trail_points = []
  trail_length = 20

  # Alpha Surface
  alpha_surface = screen.convert_alpha()

  while not done:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
        exit(0)
      if event.type == pygame.MOUSEBUTTONDOWN:
        mousePos = pygame.mouse.get_pos()
        if restart_text_rect.collidepoint(mousePos) and flag_game_over:
          main()

    screen.blit(background, (0, 0))

    for info in (block_list):
      (i, j) = info["pos"]
      block = info["block"]
      color = color_list[color_id[map_1[i][j]]]
      screen.blit(color, block)

    paddle = pygame.Rect(paddle.left, paddle.top, paddle_width, paddle_height)
    paddle_img_resized = pygame.transform.scale(paddle_img, (paddle_width, 25))
    screen.blit(paddle_img_resized, paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ball_radius)

    # Ball Movement
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy

    # Collision Left
    if ball.centerx < ball_radius or ball.centerx > W - ball_radius:
      dx = -dx

    # Collision Top
    if ball.centery < ball_radius:
      dy = -dy

    # Collision With Paddle
    if ball.colliderect(paddle) and dy > 0:
      dx, dy = detect_collision(dx, dy, ball, paddle)

    # Collision Blocks
    hit_index = ball.collidelist(list(map(lambda info: info["block"], block_list)))

    if hit_index != -1:
      hit_rect = block_list[hit_index]["block"]
      if block_list[hit_index]["stretch"]:
        paddle_width = 300
      if block_list[hit_index]["breakable"]:
        block_list.pop(hit_index)
        game_score += 1
        collision_sound.play()
      dx, dy = detect_collision(dx, dy, ball, hit_rect)

    # Game Score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    # Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
      paddle.left -= paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < W:
      paddle.right += paddle_speed

    # Ball Trail
    alpha_surface.fill([0, 0, 0, 0])
    for i, (point) in enumerate(trail_points):
      pygame.draw.circle(alpha_surface, pygame.Color(255, 0, 0, int(i * (255 / len(trail_points)))), (point), (i) * ball_radius / len(trail_points))

    trail_points.append((ball.center))

    if (len(trail_points) > trail_length):
      trail_points.pop(0)

    screen.blit(alpha_surface, (0, 0))

    # Ball Speed / Paddle Width Change
    ball_speed += ball_speed_change
    paddle_width -= paddle_width_change

    # Win / Lose Screens
    if not len(list(filter(lambda info: info["breakable"], block_list))):
      screen.fill((255, 255, 255))
      screen.blit(win_text, win_text_rect)
    elif ball.bottom > H:
      screen.fill((0, 0, 0))
      screen.blit(lose_text, lose_text_rect)
      screen.blit(restart_text, restart_text_rect)
      flag_game_over = True

    pygame.display.flip()
    clock.tick(FPS)

main()