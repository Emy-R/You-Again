import sys
import random
import pygame


CELL_SIZE = 28
GRID_W, GRID_H = 24, 24
WIDTH, HEIGHT = GRID_W * CELL_SIZE, GRID_H * CELL_SIZE
FPS = 60

SPRITE_PATH = "images/sprites/tondeuse_à_gazon.png"
FOOD_SPRITE_PATH = "images/sprites/Patate.png"
SPRITE_SCALE = 4
WIN_SCORE = 3


BLACK = (0, 0, 0)
LIGHT_GREEN = (136, 221, 136)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)


def draw_cell(surface, pos, color):
    
    x, y = pos
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, color, rect)


def make_barriers():

    left, right = 1, GRID_W - 2
    top, bottom = 1, GRID_H - 2

    barriers = set()


    for x in range(left, right + 1):
        barriers.add((x, top))
        barriers.add((x, bottom))


    for y in range(top, bottom + 1):
        barriers.add((left, y))
        barriers.add((right, y))


    holes = [(right, bottom - i) for i in range(SPRITE_SCALE)]

    for hole in holes:
        barriers.discard(hole)


    return barriers, holes

def load_sprite(path):
    
    try:
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.smoothscale(img, (SPRITE_SCALE*CELL_SIZE, SPRITE_SCALE*CELL_SIZE))
    except Exception:
        return None

def occupied_cells(pos):
    x, y = pos
    return {(x + dx, y + dy) for dx in range(SPRITE_SCALE) for dy in range(SPRITE_SCALE)}

def random_food(snake, barriers):
    xmin, xmax = 3, GRID_W -4
    ymin, ymax = 3, GRID_H -4
    free_cells = [
        (x, y)
        for x in range(xmin, xmax + 1)
        for y in range(ymin, ymax + 1)
        if (x, y) not in snake and (x,y) not in barriers
    ]
    if not free_cells:
        return None  
    return random.choice(free_cells)


def run(screen, WIDTH, HEIGHT, clock):
    snake_sprite = load_sprite(SPRITE_PATH)
    food_sprite = load_sprite(FOOD_SPRITE_PATH)
    barriers, holes  = make_barriers()
    background = pygame.image.load("images/sprites/fond_snake.png").convert()

    from sound_event import SoundEvent

    wall_sound = SoundEvent(
        file="son/explosion_perso.wav",
        trigger="manual",
        start_time=0,
        volume= 0.85
    )
    win_sound = SoundEvent(
        file="son/mg_snake.wav",
        trigger="manual",
        start_time=0,
        volume= 1

    )

    offset_x = (WIDTH - GRID_W * CELL_SIZE) // 2
    offset_y = (HEIGHT - GRID_H * CELL_SIZE) // 2

    while True:
        snake = [(GRID_W // 2, GRID_H // 2)]
        direction = (1, 0)
        food = random_food(snake,barriers)
        score = 0

        while True:
            clock.tick(3.5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wall_sound.trigger_play()
                    return "lose_wall"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and direction != (0, 1):
                        direction = (0, -1)
                    elif event.key == pygame.K_DOWN and direction != (0, -1):
                        direction = (0, 1)
                    elif event.key == pygame.K_LEFT and direction != (1, 0):
                        direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                        direction = (1, 0)

            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])


            hitbox_size = SPRITE_SCALE * CELL_SIZE * 0.3

            hitbox = pygame.Rect(
                new_head[0] * CELL_SIZE + (SPRITE_SCALE * CELL_SIZE - hitbox_size) / 2,
                new_head[1] * CELL_SIZE + (SPRITE_SCALE * CELL_SIZE - hitbox_size) / 2,
                hitbox_size,
                hitbox_size
            )

            if occupied_cells(new_head) & set(holes):
                win_sound.trigger_play()
                return "win"

            occ = occupied_cells(new_head)

            if any(cx < 0 or cx >= GRID_W or cy < 0 or cy >= GRID_H for (cx, cy) in occ):
                wall_sound.trigger_play()
                return "lose_wall"

            hit_cells_barrier = [
                (int(new_head[0] + 1.5), int(new_head[1] + 3.2)),
            ]

            collision_count = sum(1 for cell in hit_cells_barrier if cell in barriers)

            if collision_count >= 1:
                wall_sound.trigger_play()
                return "lose_wall"

            snake[0]= new_head

            if food:
                if food_sprite:
                    x, y = food

                    # hitbox patate
                    food_hitbox_size = SPRITE_SCALE * CELL_SIZE * 0.3
                    food_rect = pygame.Rect(
                        x * CELL_SIZE + (SPRITE_SCALE * CELL_SIZE - food_hitbox_size) / 2,
                        y * CELL_SIZE + (SPRITE_SCALE * CELL_SIZE - food_hitbox_size) / 2,
                        food_hitbox_size,
                        food_hitbox_size
                    )

                    screen.blit(
                        food_sprite,
                        (
                            offset_x + food[0] * CELL_SIZE,
                            offset_y + food[1] * CELL_SIZE
                        )
                    )

                if hitbox.colliderect(food_rect):
                    score += 1
                    food = random_food(snake, barriers)

                    if score >= WIN_SCORE:
                        return "lose"

            screen.fill((0, 0, 0))
            screen.blit(background, (offset_x, offset_y))

            # afficher le sprite par-dessus
            screen.blit(
                snake_sprite,
                (
                    offset_x + new_head[0] * CELL_SIZE,
                    offset_y + new_head[1] * CELL_SIZE
                )
            )

            if food:
                if food_sprite:
                    x, y = food
                    screen.blit(
                        food_sprite,
                        (
                            offset_x + food[0] * CELL_SIZE,
                            offset_y + food[1] * CELL_SIZE
                        )
                    )
                else:
                    draw_cell(screen, food, BLACK)

            pygame.display.flip()



if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    run(screen, 1920, 1080, clock)