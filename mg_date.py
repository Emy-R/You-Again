import pygame
import random


pygame.init()


WIDTH, HEIGHT = 1200, 700
FPS = 60
WIN_SCORE = 3

BACKGROUND_PATH = "images/i168.png"
GOOD_SPRITE_PATH = "images/sprites/moi.png"
BAD_SPRITE_PATHS = ["images/sprites/Blob.png", "images/sprites/burger_man.png", "images/sprites/charles.png"
                    , "images/sprites/chat.png", "images/sprites/Dieu_maths.png", "images/sprites/mec_mystérieux.png"
                    , "images/sprites/Patate_arc_en_ciel.png", "images/sprites/policier_Jo.png", "images/sprites/Sorcier.png"
                    , "images/sprites/Patate.png", "images/sprites/père_Noël.png"]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Zone d'apparition : 1/6 de l'écran
ZONE_W = WIDTH // 5
ZONE_H = HEIGHT // 5

ZONE_X = int(WIDTH * 0.58 - ZONE_W / 2)
ZONE_Y = int(HEIGHT * 0.18 - ZONE_H / 2)

# Temps d'affichage initial des sprites
INITIAL_SPAWN_TIME = 1000   # en ms
MIN_SPAWN_TIME = 250        # vitesse max
SPEED_UP = 60               # réduction du temps après chaque bon clic

def draw_spawn_zone(screen):
    rect = pygame.Rect(ZONE_X, ZONE_Y, ZONE_W, ZONE_H)
    pygame.draw.rect(screen, (255, 0, 0), rect, 3)

def load_image(path, size):
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.smoothscale(img, size)


def run(screen, WIDTH, HEIGHT, clock):
    from sound_event import SoundEvent

    true_sound = SoundEvent(
        file="son/test.wav",
        trigger="manual",
        start_time=0,
        volume=0.80
    )

    start_time = pygame.time.get_ticks()
    TIME_LIMIT = 30000

    font = pygame.font.SysFont(None, 60)
    big_font = pygame.font.SysFont(None, 120)

    # fond
    background = pygame.image.load(BACKGROUND_PATH).convert()
    background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

    # taille sprites adaptative
    SPRITE_SIZE = min(WIDTH, HEIGHT) // 4

    good_sprite = load_image(GOOD_SPRITE_PATH, (SPRITE_SIZE, SPRITE_SIZE))
    bad_sprites = [load_image(p, (SPRITE_SIZE, SPRITE_SIZE)) for p in BAD_SPRITE_PATHS]

    BUBBLE_X = 0.43 * WIDTH
    BUBBLE_Y = 0.08 * HEIGHT

    BUBBLE_W = 0.30 * WIDTH
    BUBBLE_H = 0.26 * HEIGHT

    ZONE_W = int(BUBBLE_W * 0.50)
    ZONE_H = int(BUBBLE_H * 0.50)

    ZONE_X = int(BUBBLE_X + BUBBLE_W * 0.25)
    ZONE_Y = int(BUBBLE_Y + BUBBLE_H * 0.32)

    # centre du sprite dans la bulle
    SPRITE_X = ZONE_X + ZONE_W // 2 - SPRITE_SIZE // 2
    SPRITE_Y = ZONE_Y + ZONE_H // 2 - SPRITE_SIZE // 2

    score = 0
    spawn_time = INITIAL_SPAWN_TIME
    last_change = pygame.time.get_ticks()

    game_over = False
    win = False

    current_rect = pygame.Rect(0, 0, SPRITE_SIZE, SPRITE_SIZE)
    current_image = good_sprite
    current_is_good = True

    def new_sprite():
        nonlocal current_image, current_rect, current_is_good

        current_is_good = random.random() < 0.45

        if current_is_good:
            current_image = good_sprite
        else:
            current_image = random.choice(bad_sprites)

        current_rect = current_image.get_rect(topleft=(SPRITE_X, SPRITE_Y))


    new_sprite()

    while True:

        clock.tick(FPS)
        now = pygame.time.get_ticks()
        time_left = max(0, (TIME_LIMIT - (now - start_time)) // 1000)

        if not game_over and now - start_time > TIME_LIMIT:
            game_over = True

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "lose"

            if not game_over and event.type == pygame.MOUSEBUTTONDOWN:

                if current_rect.collidepoint(event.pos):

                    if current_is_good:

                        true_sound.trigger_play()
                        score += 1

                        if score >= WIN_SCORE:
                            win = True
                            game_over = True

                        else:
                            spawn_time = max(MIN_SPAWN_TIME, spawn_time - SPEED_UP)
                            new_sprite()
                            last_change = now

                    else:
                        game_over = True

        if not game_over:
            if now - last_change >= spawn_time:
                new_sprite()
                last_change = now

        screen.fill((0, 0, 0))

        screen.blit(background, (0, 0))

        # timer
        if time_left <= 5:
            color = (255, 0, 0) if (now // 250) % 2 == 0 else (0, 0, 0)
        else:
            color = (0, 0, 0)

        timer_text = font.render(f"Temps : {time_left}", True, color)
        screen.blit(timer_text, (80, 80))


        if not game_over:
            screen.blit(current_image, current_rect)

        else:
            screen.fill((0, 0, 0))

            if win:
                WIDTH, HEIGHT = screen.get_size()
                font = pygame.font.SysFont("consolas", 50)

                screen.fill(BLACK)

                msg = font.render("VICTOIRE !", True, WHITE)
                screen.blit(msg, msg.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

                pygame.display.flip()
                pygame.time.delay(1500)
                return "win"

            else:
                return "lose"

        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((1200, 700))  # taille de test
    clock = pygame.time.Clock()

    result = run(screen, 1200, 700, clock)

    pygame.quit()

