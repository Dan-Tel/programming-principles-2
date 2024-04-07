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
      if map[i][j] != "M" and map[i][j] != "S" and map[i][j] != " ":
        block_list.append({
          "pos": (i, j),
          "block": pygame.Rect(75 * j, 25 * i, 75, 25),
          "breakable": True,
          "stretch": False
        })
      elif map[i][j] == "M":
        block_list.append({
          "pos": (i, j),
          "block": pygame.Rect(75 * j, 25 * i, 75, 25),
          "breakable": False,
          "stretch": False
        })
      elif map[i][j] == "S":
        block_list.append({
          "pos": (i, j),
          "block": pygame.Rect(75 * j, 25 * i, 75, 25),
          "breakable": True,
          "stretch": True
        })
      elif map[i][j] == " ":
        block_list.append({
          "pos": (i, j),
          "block": pygame.Rect(75 * j, 25 * i, 0, 0),
          "breakable": True,
          "stretch": False
        })
  return block_list

def main():
  done = False
  flag_game_over = False
  flag_pause = False
  flag_settings = False
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
  paddle_img = pygame.image.load("Lab8\images\paddle.png");

  # Ball
  ball_radius = 10
  ball_speed = 6
  ball_speed_change = 0.0015
  ball_rect = int(ball_radius * 2 ** 0.5)
  ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
  dx, dy = 1, -1

  # Game Score
  game_score = 0
  game_score_fonts = pygame.font.SysFont("comicsansms", 40)
  game_score_text = game_score_fonts.render(f"Your game score is: {game_score}", True, (0, 0, 0))
  game_score_rect = game_score_text.get_rect()
  game_score_rect.center = (210, 20)

  # Catching Sound
  collision_sound = pygame.mixer.Sound("Lab8\\audio\catch.mp3")

  # Block Settings
  red_block = pygame.image.load("Lab8\images\\red-block.png")
  orange_block = pygame.image.load("Lab8\images\orange-block.png")
  green_block = pygame.image.load("Lab8\images\green-block.png")
  cyan_block = pygame.image.load("Lab8\images\cyan-block.png")
  blue_block = pygame.image.load("Lab8\images\\blue-block.png")
  purple_block = pygame.image.load("Lab8\images\purple-block.png")
  metal_block = pygame.image.load("Lab8\images\metal-block.png")
  stretch_block = pygame.image.load("Lab8\images\stretch-block.png")

  map_1 = [
    "      OOR",
    "      OOR",
    " S    OOO",
    " M     OO",
    "       OO",
    "  CCG    ",
    " BBBGG   ",
    " BBBGG   ",
    " GGBBG   ",
    " GGBBG   ",
    " GGBBC   ",
    " GGBBC   ",
    "  BBG    "
  ]

  block_list = generate_map(map_1)
  color_list = [red_block, orange_block, green_block, cyan_block, blue_block, purple_block, metal_block, stretch_block]
  color_id = {"R": 0, "O": 1, "G": 2, "C": 3, "B": 4, "P": 5, "M": 6, "S": 7}

  # Background
  background = pygame.image.load("Lab8\images\\background.png")

  # Game Over Screen
  lose_font = pygame.font.SysFont("comicsansms", 40)
  lose_text = lose_font.render("Game Over", True, (255, 255, 255))
  lose_text_rect = lose_text.get_rect()
  lose_text_rect.center = (W // 2, H // 2)

  # Win Screen
  win_font = pygame.font.SysFont("comicsansms", 40)
  win_text = win_font.render("You win yay", True, (0, 0, 0))
  win_text_rect = win_text.get_rect()
  win_text_rect.center = (W // 2, H // 2)

  # Restart Screen
  restart_font = pygame.font.SysFont("comicsansms", 30)
  restart_text = restart_font.render("Restart", True, (255, 255, 255))
  restart_text_rect = restart_text.get_rect()
  restart_text_rect.center = (W // 2, H // 2 + 100)

  # Pause Screen
  pause_font = pygame.font.SysFont("comicsansms", 40)
  pause_text = pause_font.render("Paused", True, (255, 255, 255))
  pause_text_rect = pause_text.get_rect()
  pause_text_rect.center = (W // 2, 100)

  # Pause Button
  pause_button_font = pygame.font.SysFont("comicsansms", 20)
  pause_button_text = pause_button_font.render("Click P to pause the game", True, (0, 0, 0))
  pause_button_text_rect = pause_button_text.get_rect()
  pause_button_text_rect.bottom = H - 5
  pause_button_text_rect.right = W - 10

  # Continue
  continue_font = pygame.font.SysFont("comicsansms", 30)
  continue_text = continue_font.render("Continue", True, (255, 255, 255))
  continue_text_rect = continue_text.get_rect()
  continue_text_rect.center = (W // 2, H // 2 + 50)

  # Settings Screen
  settings_title_font = pygame.font.SysFont("comicsansms", 40)
  settings_title_text = settings_title_font.render("Settings", True, (255, 255, 255))
  settings_title_text_rect = settings_title_text.get_rect()
  settings_title_text_rect.center = (W // 2, 100)

  settings_button_font = pygame.font.SysFont("comicsansms", 30)
  settings_button_text = settings_button_font.render("Settings", True, (255, 255, 255))
  settings_button_text_rect = settings_button_text.get_rect()
  settings_button_text_rect.center = (W // 2, H // 2)

  # Volume
  volume_font = pygame.font.SysFont("comicsansms", 30)
  volume_text = volume_font.render("Volume", True, (255, 255, 255))
  volume_text_rect = volume_text.get_rect()
  volume_text_rect.center = (W // 2, H // 2 - 140)

  volume_bar_width = 150
  volume_bar_division = 10
  volume_bar_gap = 3
  current_volume = 3
  volume_bar = []
  for i in range(volume_bar_division):
    volume_bar.append(pygame.Rect(
      W / 2 - volume_bar_width / 2 + volume_bar_gap + (volume_bar_gap + (volume_bar_width / volume_bar_division -  volume_bar_gap * 2) + volume_bar_gap) * i,
      H // 2 - 100,
      volume_bar_width / volume_bar_division -  volume_bar_gap * 2,
      20))

  # Difficulty
  difficulty_font = pygame.font.SysFont("comicsansms", 30)
  difficulty_text = difficulty_font.render("Difficulty", True, (255, 255, 255))
  difficulty_text_rect = difficulty_text.get_rect()
  difficulty_text_rect.center = (W // 2, H // 2 - 15)

  current_difficulty = 1

  easy_text = difficulty_font.render("Easy", True, (255, 255, 255))
  easy_text_rect = easy_text.get_rect()
  easy_text_rect.top = H // 2 + 10
  easy_text_rect.right = W // 2 - 75

  medium_text = difficulty_font.render("Medium", True, (100, 100, 100))
  medium_text_rect = medium_text.get_rect()
  medium_text_rect.top = H // 2 + 10
  medium_text_rect.centerx = W // 2

  hard_text = difficulty_font.render("Hard", True, (100, 100, 100))
  hard_text_rect = hard_text.get_rect()
  hard_text_rect.top = H // 2 + 10
  hard_text_rect.left = W // 2 + 75

  # Back
  back_font = pygame.font.SysFont("comicsansms", 30)
  back_text = back_font.render("Back", True, (255, 255, 255))
  back_text_rect = back_text.get_rect()
  back_text_rect.center = (W // 2, H // 2 + 100)

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
        for i in range(volume_bar_division):
          if volume_bar[i].collidepoint(mousePos) and (flag_pause and flag_settings):
            current_volume = i + 1

        if easy_text_rect.collidepoint(mousePos) and (flag_pause and flag_settings):
          current_difficulty = 1
        if medium_text_rect.collidepoint(mousePos) and (flag_pause and flag_settings):
          current_difficulty = 2
        if hard_text_rect.collidepoint(mousePos) and (flag_pause and flag_settings):
          current_difficulty = 3

        if restart_text_rect.collidepoint(mousePos) and (flag_game_over or flag_pause) and not flag_settings:
          main()
        if settings_button_text_rect.collidepoint(mousePos) and (flag_pause):
          flag_settings = True
        if back_text_rect.collidepoint(mousePos) and (flag_pause and flag_settings):
          flag_settings = False
        if continue_text_rect.collidepoint(mousePos) and (flag_pause and not flag_settings):
          flag_pause = not flag_pause
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
          flag_pause = not flag_pause
          if not flag_pause:
            flag_settings = False

    alpha_surface.fill([0, 0, 0, 0])

    if not flag_pause:
      screen.blit(background, (0, 0))

      for info in (block_list):
        (i, j) = info["pos"]
        block = info["block"]
        if (map_1[i][j] != " "):
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
          collision_sound.set_volume((current_volume + 1) / volume_bar_division)
          collision_sound.play()
        dx, dy = detect_collision(dx, dy, ball, hit_rect)

      # Game Score
      game_score_text = game_score_fonts.render(f"Your game score is: {game_score}", True, (255, 255, 255))
      screen.blit(game_score_text, game_score_rect)

      # Pause Button
      screen.blit(pause_button_text, pause_button_text_rect)

      # Paddle Control
      key = pygame.key.get_pressed()
      if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
      if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddle_speed

      # Ball Trail
      for i, (point) in enumerate(trail_points):
        pygame.draw.circle(alpha_surface, pygame.Color(255, 0, 0, int(i * (255 / len(trail_points)))), (point), (i) * ball_radius / len(trail_points))

      trail_points.append((ball.center))

      if (len(trail_points) > trail_length):
        trail_points.pop(0)

      screen.blit(alpha_surface, (0, 0))

      # Ball Speed / Paddle Width Change
      ball_speed += ball_speed_change * current_difficulty
      paddle_width -= paddle_width_change * current_difficulty

      # Win / Lose Screens
      if not len(list(filter(lambda info: info["breakable"], block_list))):
        screen.fill((255, 255, 255))
        screen.blit(win_text, win_text_rect)
      elif ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(lose_text, lose_text_rect)
        screen.blit(restart_text, restart_text_rect)
        flag_game_over = True
    else:
      # Pause Screen
      screen.fill((0, 0, 0))

      if flag_settings:
        screen.blit(settings_title_text, settings_title_text_rect)
        screen.blit(volume_text, volume_text_rect)
        screen.blit(difficulty_text, difficulty_text_rect)

        easy_text = difficulty_font.render("Easy", True, (100, 100, 100))
        medium_text = difficulty_font.render("Medium", True, (100, 100, 100))
        hard_text = difficulty_font.render("Hard", True, (100, 100, 100))

        if current_difficulty == 1:
          easy_text = difficulty_font.render("Easy", True, (255, 255, 255))
        elif current_difficulty == 2:
          medium_text = difficulty_font.render("Medium", True, (255, 255, 255))
        elif current_difficulty == 3:
          hard_text = difficulty_font.render("Hard", True, (255, 255, 255))

        screen.blit(easy_text, easy_text_rect)
        screen.blit(medium_text, medium_text_rect)
        screen.blit(hard_text, hard_text_rect)

        screen.blit(back_text, back_text_rect)

        for i in range(volume_bar_division):
          color = (255, 255, 255) if i < current_volume else (100, 100, 100)
          pygame.draw.rect(screen, color, volume_bar[i])
      else:
        screen.blit(pause_text, pause_text_rect)
        screen.blit(settings_button_text, settings_button_text_rect)
        screen.blit(continue_text, continue_text_rect)
        screen.blit(restart_text, restart_text_rect)

    pygame.display.flip()
    clock.tick(FPS)

main()