import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MUSIC_LIST = ["Eternity", "Healthcare", "Memory"]
FONT_REGULAR = pygame.font.Font("Lab7\\font\Montserrat-Regular.ttf", 14)
FONT_BLACK = pygame.font.Font("Lab7\\font\Montserrat-Black.ttf", 28)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False

is_playing = True
music_id = 1

button_1 = FONT_REGULAR.render("SPACE - toggle play/stop", True, BLACK)
button_2 = FONT_REGULAR.render("A - previous music", True, BLACK)
button_3 = FONT_REGULAR.render("D - next", True, BLACK)
current_music = FONT_BLACK.render(MUSIC_LIST[music_id - 1], True, BLACK)

def get_center(screen_w, screen_h, w, h):
  return ((screen_w - w) // 2, (screen_h - h) // 2)

def toggle_music(is_playing):
  if is_playing:
    pygame.mixer.music.play(-1)
  else:
    pygame.mixer.music.stop()
  
def change_music_id(music_id):
  if music_id > 3:
    return 1
  elif music_id < 1:
    return 3
  else:
    return music_id

def load_music(music_id, is_playing):
  pygame.mixer.music.load(f"Lab7\music\music-{music_id}.mp3")
  toggle_music(is_playing)

load_music(music_id, is_playing)

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        is_playing = not is_playing
        toggle_music(is_playing)
      if event.key == pygame.K_d:
        music_id = change_music_id(music_id + 1)
        load_music(music_id, is_playing)
      if event.key == pygame.K_a:
        music_id = change_music_id(music_id - 1)
        load_music(music_id, is_playing)

  current_music = FONT_BLACK.render(MUSIC_LIST[music_id - 1], True, BLACK)

  screen.fill(WHITE)
  screen.blit(button_1, (50, 50))
  screen.blit(button_2, (50, 65))
  screen.blit(button_3, (50, 80))
  screen.blit(current_music, get_center(SCREEN_WIDTH, SCREEN_HEIGHT, current_music.get_width(), current_music.get_height()))
  pygame.display.flip()
