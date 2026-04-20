import pygame
import random
import sys
import math

pygame.init()

# ================= CONFIG =================
FPS = 60
GRAVITY = 0.5

# chemins images
BACKGROUND_PATH = "images/i227.png"

POTATO_PATH = "images/sprites/Patate.png"
PEANUT_PATH = "images/sprites/cacahuète.png"

POTATO_SLICE_1 = "images/sprites/Patate_coupee_1.png"
POTATO_SLICE_2 = "images/sprites/Patate_coupee_2.png"

PEANUT_SLICE_1 = "images/sprites/Cacahuete_coupee_1.png"
PEANUT_SLICE_2 = "images/sprites/Cacahuete_coupee_2.png"


def load_scaled(path, size=240):
    img = pygame.image.load(path).convert_alpha()
    ratio = img.get_width() / img.get_height()
    return pygame.transform.smoothscale(img, (size, int(size/ratio)))

font = pygame.font.SysFont(None, 50)

# ================= CLASSES =================

class Fruit:
    def __init__(self, WIDTH, HEIGHT):
        self.type = random.choice(["potato", "peanut"])
        self.image = potato_img if self.type == "potato" else peanut_img

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, WIDTH - 100)
        self.rect.y = HEIGHT + 50

        self.vx = random.uniform(-4, 4)
        self.vy = random.uniform(-28, -22)

        self.alive = True

    def update(self):
        self.vy += GRAVITY
        self.rect.x += self.vx
        self.rect.y += self.vy

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Piece:
    def __init__(self, image, pos, direction):
        self.image = image
        self.rect = self.image.get_rect(center=pos)

        self.vx = direction * random.uniform(3, 7)
        self.vy = random.uniform(-10, -5)

    def update(self):
        self.vy += GRAVITY
        self.rect.x += self.vx
        self.rect.y += self.vy

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# ================= UTILS =================

def line_rect_collision(p1, p2, rect):
    # check collision ligne souris / rectangle
    steps = 10
    for i in range(steps):
        x = p1[0] + (p2[0] - p1[0]) * i / steps
        y = p1[1] + (p2[1] - p1[1]) * i / steps
        if rect.collidepoint(x, y):
            return True
    return False

# ================= GAME =================

def run(screen, WIDTH, HEIGHT, clock, win_score=10, max_time=None):
    from sound_event import SoundEvent

    cut_sound = SoundEvent(
        file="son/fruit_ninja.wav",
        trigger="manual",
        start_time=0,
        volume= 0.75
    )
    background = pygame.image.load(BACKGROUND_PATH).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    global potato_img, peanut_img
    global potato_slice1, potato_slice2
    global peanut_slice1, peanut_slice2

    potato_img = load_scaled(POTATO_PATH)
    peanut_img = load_scaled(PEANUT_PATH)

    potato_slice1 = load_scaled(POTATO_SLICE_1)
    potato_slice2 = load_scaled(POTATO_SLICE_2)

    peanut_slice1 = load_scaled(PEANUT_SLICE_1)
    peanut_slice2 = load_scaled(PEANUT_SLICE_2)

    start_time = pygame.time.get_ticks()
    end_timer = 0

    fruits = []
    pieces = []

    score = 0
    game_over = False
    win = False

    spawn_timer = 0

    last_mouse_pos = None

    while True:
        clock.tick(FPS)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if max_time is not None:
            current_time = pygame.time.get_ticks()
            if current_time - start_time > max_time:
                return "lose"

        mouse_pos = pygame.mouse.get_pos()

        # spawn
        if not game_over and not win:
            spawn_timer += 1
            if spawn_timer > 40:
                fruits.append(Fruit(WIDTH, HEIGHT))
                spawn_timer = 0

        # update fruits
        for fruit in fruits[:]:
            fruit.update()

            # slice detection
            if last_mouse_pos:
                if line_rect_collision(last_mouse_pos, mouse_pos, fruit.rect):

                    if fruit.type == "peanut":
                        cut_sound.trigger_play()
                        game_over = True

                        pieces.append(Piece(peanut_slice1, fruit.rect.center, -1))
                        pieces.append(Piece(peanut_slice2, fruit.rect.center, 1))

                    else:
                        cut_sound.trigger_play()
                        score += 1

                        pieces.append(Piece(potato_slice1, fruit.rect.center, -1))
                        pieces.append(Piece(potato_slice2, fruit.rect.center, 1))

                    fruits.remove(fruit)

            # remove if off screen
            if fruit.rect.y > HEIGHT + 100:
                fruits.remove(fruit)

        # update pieces
        for p in pieces:
            p.update()

        # win condition
        if score >= win_score:
            win = True

        # draw
        screen.blit(background, (0, 0))

        for fruit in fruits:
            fruit.draw(screen)

        for p in pieces:
            p.draw(screen)

        # score
        text = font.render(f"Score: {score}", True, (0,0,0))
        screen.blit(text, (20, 20))

        # end screens
        if game_over:
            end_timer += 1
            if end_timer > FPS:
                return "lose"

        if win:
            end_timer +=1
            if end_timer > FPS:
                return "win"

        pygame.display.flip()

        last_mouse_pos = mouse_pos


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    WIDTH, HEIGHT = screen.get_size()
    clock = pygame.time.Clock()
    run(screen,WIDTH,HEIGHT,clock)
