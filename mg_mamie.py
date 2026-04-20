import random
import pygame


BACKGROUND_PATH = "images/i51.png"
MAMIE_PATH = "images/sprites/mamie_en_colere.png"
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIN_SCORE = 6
TIME_LIMIT = 10
FPS = 60

def random_speed():
    vx = random.choice([-1, 1]) * random.randint(8, 12)
    vy = random.choice([-1, 1]) * random.randint(8, 12)
    return vx, vy

def game_over():
    pygame.display.flip()
    return "lose"



def win(screen):

    WIDTH, HEIGHT = screen.get_size()
    font = pygame.font.SysFont("consolas", 50)

    screen.fill(BLACK)

    msg = font.render("VICTOIRE !", True, WHITE)
    screen.blit(msg, msg.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

    pygame.display.flip()
    pygame.time.delay(1500)

    return "win"

def run(screen, WIDTH, HEIGHT, clock):
    from sound_event import SoundEvent

    mamie_sound = SoundEvent(
        file="son/mamie.wav",
        trigger="manual",
        start_time=0,
        volume=0.75
    )

    font = pygame.font.SysFont(None, 50)

    background = pygame.image.load(BACKGROUND_PATH).convert()
    background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))


    mamie = pygame.image.load(MAMIE_PATH).convert_alpha()

    mamie_height = HEIGHT // 2.5
    ratio = mamie.get_width() / mamie.get_height()
    mamie_width = int(mamie_height * ratio)

    mamie = pygame.transform.smoothscale(mamie, (mamie_width, mamie_height))
    mamie_rect = mamie.get_rect()

    mamie_rect.x = random.randint(0, WIDTH - mamie_rect.width)
    mamie_rect.y = random.randint(0, HEIGHT - mamie_rect.height)

    vx, vy = random_speed()

    score = 0
    start_time = pygame.time.get_ticks()

    running = True

    while running:

        clock.tick(FPS)

        elapsed = (pygame.time.get_ticks() - start_time) / 1000
        remaining = max(0, TIME_LIMIT - elapsed)

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN :

                if mamie_rect.collidepoint(event.pos):
                    mamie_sound.trigger_play()
                    score += 1

                    mamie_rect.x = random.randint(0, WIDTH - mamie_rect.width)
                    mamie_rect.y = random.randint(0, HEIGHT - mamie_rect.height)

                    vx , vy = random_speed()

                    if score >= WIN_SCORE:
                        return win(screen)

        mamie_rect.x += vx
        mamie_rect.y += vy

        if mamie_rect.left <= 0 or mamie_rect.right >= WIDTH:
            vx = -vx

        if mamie_rect.top <= 0 or mamie_rect.bottom >= HEIGHT:
            vy = -vy

        if remaining <= 0:
            return game_over()

        screen.blit(background, (0, 0))
        screen.blit(mamie, mamie_rect)


        score_text = font.render(f"Score : {score}/{WIN_SCORE}", True, (0, 0, 0))
        screen.blit(score_text, (30, 20))

        timer_text = font.render(f"Temps : {int(remaining)}", True, (0, 0, 0))
        screen.blit(timer_text, (WIDTH - timer_text.get_width() - 30, 20))


        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    run(screen, 1920, 1080, clock)

