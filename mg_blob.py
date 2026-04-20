import random
import pygame

# --- CONFIGURATION ---
BACKGROUND_PATH = "images/sprites/espace.png"
BLOB_PATH = "images/sprites/blob_et_moi.png"
OBJETS_SPRITES = ["images/sprites/patate_spatiale.png"]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

TOTAL_WIN_SCORE = 30
STEP_SCORE = 10
TIME_LIMIT = 45
FPS = 60


def random_speed():
    vx = random.uniform(-1.5, 1.5)
    vy = random.uniform(3, 5)
    return vx, vy


def game_over(screen, raison="PERDU !"):
    WIDTH, HEIGHT = screen.get_size()
    font = pygame.font.SysFont("consolas", 40)
    screen.fill(BLACK)
    msg = font.render(raison, True, (255, 255, 255))
    screen.blit(msg, msg.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
    pygame.display.flip()
    pygame.time.delay(4000)
    return "lose"


def win_animation(screen, background, blob_img, blob_rect):
    blob_moi = 1
    for i in range(60):
        blob_moi += 1
        blob_rect.y -= blob_moi
        screen.blit(background, (0, 0))
        screen.blit(blob_img, blob_rect)
        pygame.display.flip()
        pygame.time.delay(15)
    return "win"


def run(screen, WIDTH, HEIGHT, clock):
    try:
        from sound_event import SoundEvent

        laser_sound = SoundEvent(
            file="son/laser.wav",
            trigger="manual",
            start_time=0,
            volume=0.7
        )
        lose_sound = SoundEvent(
            file="son/ovni_win.WAV",
            trigger="manual",
            start_time=0,
            volume=0.75
        )
        background = pygame.image.load(BACKGROUND_PATH).convert()
        background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

        # --- VAISSEAU ---
        v_img = pygame.image.load(BLOB_PATH).convert_alpha()
        v_h = HEIGHT // 3
        v_w = int(v_h * (v_img.get_width() / v_img.get_height()))
        blob_img = pygame.transform.smoothscale(v_img, (v_w, v_h))
        blob_rect = blob_img.get_rect()
        blob_rect.midbottom = (WIDTH // 2, HEIGHT)

        # CRÉATION DU MASQUE DU VAISSEAU
        blob_mask = pygame.mask.from_surface(blob_img)

        # OBSTACLES
        surfaces_avec_masques = []
        for chemin in OBJETS_SPRITES:
            img = pygame.image.load(chemin).convert_alpha()
            h = HEIGHT // 4
            w = int(h * (img.get_width() / img.get_height()))
            scaled_img = pygame.transform.smoothscale(img, (w, h))
            # ON PRÉPARE LE MASQUE POUR CHAQUE OBSTACLE
            mask = pygame.mask.from_surface(scaled_img)
            surfaces_avec_masques.append((scaled_img, mask))

    except Exception as e:
        print(f"Erreur : {e}")
        return "lose"

    font = pygame.font.SysFont(None, 50)
    obstacles = []
    score = 0
    spawn_timer = 0
    start_time = pygame.time.get_ticks()
    step_distance = HEIGHT // 15

    running = True
    while running:
        clock.tick(FPS)
        elapsed = (pygame.time.get_ticks() - start_time) / 1000
        remaining = max(0, TIME_LIMIT - elapsed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: return "lose"
            if event.type == pygame.MOUSEBUTTONDOWN:
                for obj in obstacles[:]:
                    if obj["rect"].collidepoint(event.pos):
                        laser_sound.trigger_play()
                        obstacles.remove(obj)
                        score += 1
                        if score % STEP_SCORE == 0 and score < TOTAL_WIN_SCORE and score > 0:
                            blob_rect.y -= step_distance
                        if score >= TOTAL_WIN_SCORE:
                            return win_animation(screen, background, blob_img, blob_rect)

        spawn_timer += 1
        spawn_speed = 35 - (score // 5)
        if spawn_timer > max(15, spawn_speed):
            # On choisit l'image et son masque associé
            img_curr, mask_curr = random.choice(surfaces_avec_masques)
            rect = img_curr.get_rect()
            rect.x = random.randint(10, WIDTH - rect.width - 10)
            rect.y = -rect.height
            vx, vy = random_speed()
            obstacles.append({"rect": rect, "vx": vx, "vy": vy, "image": img_curr, "mask": mask_curr})
            spawn_timer = 0

        for obj in obstacles[:]:
            obj["rect"].x += obj["vx"]
            obj["rect"].y += obj["vy"]

            if obj["rect"].left <= 0 or obj["rect"].right >= WIDTH:
                obj["vx"] *= -1


            # On calcule l'écart entre les deux objets
            offset_x = obj["rect"].x - blob_rect.x
            offset_y = obj["rect"].y - blob_rect.y

            # On vérifie si les pixels se touchent
            if blob_mask.overlap(obj["mask"], (offset_x, offset_y)):
                lose_sound.trigger_play()
                return game_over(screen, "GAME OVER !")

            if obj["rect"].top > HEIGHT:
                obstacles.remove(obj)

        if remaining <= 0:
            return game_over(screen, "TEMPS ÉCOULÉ !")

        screen.blit(background, (0, 0))
        screen.blit(blob_img, blob_rect)
        for obj in obstacles:
            screen.blit(obj["image"], obj["rect"])

        prog_txt = font.render(f"Patates : {score}/{TOTAL_WIN_SCORE}", True, WHITE)
        time_txt = font.render(f"Temps : {int(remaining)}s", True, WHITE)
        screen.blit(prog_txt, (20, 20))
        screen.blit(time_txt, (WIDTH - 200, 20))

        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    info = pygame.display.Info()
    screen = pygame.display.set_mode((info.current_w, info.current_h))
    clock = pygame.time.Clock()
    run(screen, info.current_w, info.current_h, clock)
