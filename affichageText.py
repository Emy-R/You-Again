import pygame
from constantes import *

pygame.font.init()
def get_font(screen): ## adapter le taille de la police à la taille de l'écran
    _, sh = screen.get_size()
    size = int(sh * 0.07)
    return pygame.font.Font("Kindergarden.ttf", size)

def play_story(screen, background_path, texts,couleur=(255, 255, 255)):
    font=get_font(screen)
    clock = pygame.time.Clock()
    running=True
    # charger fond
    bg = pygame.image.load(background_path).convert()
    bg = pygame.transform.smoothscale(bg, screen.get_size())
    screen.blit(bg, (0,0))
    pygame.display.flip()
    sw, sh = screen.get_size()
    hauteur_texte = sh // 2 - len(texts) * font.get_height()
    for texte in texts:
        width = font.render(texte, True, couleur).get_width()
        x_position = sw // 2 - width // 2

        for lettre in texte:
            lettre_surface = font.render(lettre, True, couleur)
            screen.blit(lettre_surface, (x_position, hauteur_texte))
            pygame.display.flip()
            pygame.time.wait(25)
            x_position += lettre_surface.get_width()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or \
                        (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    return

        hauteur_texte += font.get_height()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                running=False

def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        width = font.render(test_line, True, (0,0,0)).get_width()

        if width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "

    lines.append(current_line)
    return lines

def play_lore(screen, background_path, texts, couleur=(105,32,5)):

    clock = pygame.time.Clock()
    running = True

    bg = pygame.image.load(background_path).convert()
    bg = pygame.transform.smoothscale(bg, screen.get_size())

    sw, sh = screen.get_size()
    font = get_font(screen)

    margin = 50
    max_width = sw - 2 * margin

    # --- WRAP ---
    wrapped_lines = []
    for texte in texts:
        wrapped_lines.extend(wrap_text(texte, font, max_width))


    y_offset = sh  # commence en bas de l'écran

    scroll_speed = 0.75  # vitesse

    while running:

        screen.blit(bg, (0, 0))

        y = y_offset

        # afficher texte
        for line in wrapped_lines:
            text_surface = font.render(line, True, couleur)
            x = sw // 2 - text_surface.get_width() // 2
            screen.blit(text_surface, (x, y))
            y += font.get_height() + 5

        # texte pour skip
        skip_font = pygame.font.Font("Kindergarden.ttf", int(sh * 0.04))
        skip_text = "cliquer pour passer, scroll clavier disponible"
        skip_surface = skip_font.render(skip_text, True, (255, 255, 255))
        # rendre transparent
        skip_surface.set_alpha(120)  # 0 = invisible, 255 = opaque
        x = sw // 2 - skip_surface.get_width() // 2
        y = sh - skip_surface.get_height() - 20  # en bas avec marge

        screen.blit(skip_surface, (x, y))
        pygame.display.flip()

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                    return
                if event.key == pygame.K_DOWN:
                    y_offset -= 20
                if event.key == pygame.K_UP:
                    y_offset += 20

            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False


        y_offset -= scroll_speed

        # fin
        total_height = len(wrapped_lines) * (font.get_height() + 5)

        if y_offset < -total_height:
            return

        pygame.event.pump()
        clock.tick(60)
