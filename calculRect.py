import pygame
import sys

# --- CONFIG ---
IMAGE_PATH = "images/i217.png"  # Change selon image
SCREEN_WIDTH = 0  # 0 pour fullscreen auto
SCREEN_HEIGHT = 0

# --- INIT ---
pygame.init()
flags = pygame.FULLSCREEN if SCREEN_WIDTH == 0 else 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags)
pygame.display.set_caption("Zone Selector")
font = pygame.font.SysFont(None, 36)

# Charger et redimensionner image
img = pygame.image.load(IMAGE_PATH).convert_alpha()
sw, sh = screen.get_size()
img = pygame.transform.smoothscale(img, (sw, sh))

clicks = []  # stocke les 2 coins
running = True


def draw_text(text, pos):
    surf = font.render(text, True, (255, 255, 255))
    screen.blit(surf, pos)


while running:
    screen.blit(img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            clicks.append(pygame.mouse.get_pos())
            if len(clicks) == 2:
                sw, sh = screen.get_size()
                x0, y0 = clicks[0]
                x1, y1 = clicks[1]

                # Calcul en pourcentage
                x = min(x0, x1) / sw
                y = min(y0, y1) / sh
                width = abs(x1 - x0) / sw
                height = abs(y1 - y0) / sh

                # Affiche JSON à l'écran
                json_text = (
                    '{\n'
                    f'  "x": {x:.3f},\n'
                    f'  "y": {y:.3f},\n'
                    f'  "width": {width:.3f},\n'
                    f'  "height": {height:.3f},\n'
                    '  "target": "sceneX",\n'

                )
                print("\n--- JSON PRÊT ---\n")
                print(json_text)



                running = False

    # Dessiner rectangle temporaire pendant le clic
    if len(clicks) == 1:
        x, y = clicks[0]
        mx, my = pygame.mouse.get_pos()
        rect = pygame.Rect(min(x, mx), min(y, my), abs(mx - x), abs(my - y))
        pygame.draw.rect(screen, (255, 0, 0), rect, 3)

    if len(clicks) == 2:
        x0, y0 = clicks[0]
        x1, y1 = clicks[1]
        rect = pygame.Rect(min(x0, x1), min(y0, y1), abs(x1 - x0), abs(y1 - y0))
        pygame.draw.rect(screen, (255, 0, 0), rect, 3)

    if running:
        draw_text("Cliquez sur 2 coins pour définir la zone", (20, 20))
        draw_text("Appuyez sur ESC ou Q pour quitter", (20, 60))
        pygame.display.flip()

pygame.quit()
sys.exit()