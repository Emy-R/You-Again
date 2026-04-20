import pygame

class AnimatedObject:
    def __init__(self, image_path, movement, duration, scale=1.0):
        """
        image_path : nom du fichier dans images/sprites/
        movement : liste de {time, x, y} avec x,y en ratios [0..1]
        duration : durée totale de l'animation (ms)
        scale : échelle du sprite (1.0 = taille normale)
        """
        original = pygame.image.load(f"images/sprites/{image_path}").convert_alpha()
        # Calcul de la taille du sprite selon l'échelle et la résolution
        screen = pygame.display.get_surface()
        sw, sh = screen.get_size()
        base_w, base_h = 1920, 1080  # résolution de référence
        width = int(original.get_width() * scale * (sw / base_w))
        height = int(original.get_height() * scale * (sh / base_h))
        self.image = pygame.transform.smoothscale(original, (width, height))

        self.movement = movement
        self.duration = duration
        self.start_time = pygame.time.get_ticks()
        self.x = movement[0]["x"]
        self.y = movement[0]["y"]

    def update(self, current_time):
        elapsed = current_time - self.start_time
        if elapsed > self.duration:
            elapsed = self.duration
        # Parcours des paliers temporels
        for i in range(len(self.movement) - 1):
            start = self.movement[i]
            end = self.movement[i + 1]
            if start["time"] <= elapsed <= end["time"]:
                dt = (elapsed - start["time"]) / (end["time"] - start["time"])
                self.x = start["x"] + (end["x"] - start["x"]) * dt
                self.y = start["y"] + (end["y"] - start["y"]) * dt
                break

    def draw(self, screen):
        """
        Affiche le sprite à la position calculée.
        """
        sw, sh = screen.get_size()
        px = int(self.x * sw)
        py = int(self.y * sh)
        screen.blit(self.image, (px, py))
