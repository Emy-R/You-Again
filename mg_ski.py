import random
import pygame

# --- CONFIGURATION ---
BACKGROUND_PATH = "images/sprites/piste_de_ski.png"
PERSO_PATH = "images/sprites/père_Noël.png"
PATATE_PATH = "images/sprites/patate.png"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
OBJECTIF_ESQUIVES = 15  # Le nombre de patates à esquiver pour gagner


def run(screen, WIDTH, HEIGHT, clock):
    # CHARGEMENT DES IMAGES ET DES MASQUES
    try:
        from sound_event import SoundEvent

        ski_sound = SoundEvent(
            file="son/fruit_ninja.wav",
            trigger="manual",
            start_time=0,
            volume=0.75
        )
        back = pygame.image.load(BACKGROUND_PATH).convert()
        background = pygame.transform.smoothscale(back, (WIDTH, HEIGHT))

        # Personnage
        p_img = pygame.image.load(PERSO_PATH).convert_alpha()
        p_h = HEIGHT // 4
        p_w = int(p_h * (p_img.get_width() / p_img.get_height()))
        perso_img = pygame.transform.smoothscale(p_img, (p_w, p_h))
        perso_rect = perso_img.get_rect()
        perso_rect.midbottom = (WIDTH // 2, HEIGHT - 30)
        perso_mask = pygame.mask.from_surface(perso_img)

        # Patate
        c_img = pygame.image.load(PATATE_PATH).convert_alpha()
        c_h = HEIGHT // 6
        c_w = int(c_h * (c_img.get_width() / c_img.get_height()))
        patate_img = pygame.transform.smoothscale(c_img, (c_w, c_h))
        patate_mask = pygame.mask.from_surface(patate_img)

    except Exception as e:
        print(f"Erreur de chargement : {e}")
        return

    font = pygame.font.SysFont(None, 50)
    obstacles = []
    spawn_timer = 0
    score = 0

    running = True
    while running:
        clock.tick(FPS)

        # MOUVEMENTS (Clavier)
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_q]) and perso_rect.left > 0:
            ski_sound.trigger_play()
            perso_rect.x -= 15
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and perso_rect.right < WIDTH:
            ski_sound.trigger_play()
            perso_rect.x += 15

        for event in pygame.event.get():
            if event.type == pygame.QUIT: return "lose"

        # APPARITION DES PATATES
        spawn_timer += 1
        if spawn_timer > 35:  # Fréquence d'apparition
            c_rect = patate_img.get_rect()
            c_rect.x = random.randint(50, WIDTH - c_rect.width - 50)
            c_rect.y = -c_rect.height
            obstacles.append({"rect": c_rect, "speed": 10})
            spawn_timer = 0

        #  COLLISIONS ET SCORE
        for obs in obstacles[:]:
            obs["rect"].y += obs["speed"]

            # Calcul de l'offset pour le masque
            offset = (obs["rect"].x - perso_rect.x, obs["rect"].y - perso_rect.y)

            # COLLISION PIXEL (Si le dessin touche le dessin)
            if perso_mask.overlap(patate_mask, offset):
                return 'lose'

            # SCORE (Si la patate est évitée)
            if obs["rect"].top > HEIGHT:
                obstacles.remove(obs)
                score += 1

                # CONDITION DE VICTOIRE : 10 esquives
                if score >= OBJECTIF_ESQUIVES:
                    return "win"

        # DESSIN
        screen.blit(background, (0, 0))
        for obs in obstacles:
            screen.blit(patate_img, obs["rect"])
        screen.blit(perso_img, perso_rect)

        # HUD (Affichage du score)
        score_txt = font.render(f"Esquives : {score} / {OBJECTIF_ESQUIVES}", True, BLACK)
        screen.blit(score_txt, (20, 20))

        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    info = pygame.display.Info()
    screen = pygame.display.set_mode((info.current_w, info.current_h))
    run(screen, info.current_w, info.current_h, pygame.time.Clock())