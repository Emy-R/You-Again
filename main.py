from constantes import *
from scene_manager import SceneManager
import mg_mamie
import mg_date
import mg_snake
import mg_fruit_ninja
import mg_ski
import mg_blob

# ---- Initialisation ----
pygame.init()

screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Patate Carnivore")

# ---- Dictionnaire mini-jeux ----
MINIGAMES = {
    "mg_mamie": mg_mamie.run,
    "mg_date": mg_date.run,
    "mg_snake": mg_snake.run,
    "mg_fruit_ninja": mg_fruit_ninja.run,
    "mg_blob": mg_blob.run,
    "mg_ski": mg_ski.run,
}

# ---- SceneManager ----
manager = SceneManager(screen, MINIGAMES)
manager.load_scene("menu")  # menu.json devient une scène normale


# ---- Boucle principale ----
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        manager.check_keyboard(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            manager.handle_click(pygame.mouse.get_pos())

    manager.update() # Mise à jour des animations
    manager.draw(debug=False) # pour afficher les zones
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
