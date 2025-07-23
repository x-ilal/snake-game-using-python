import pygame
import random
import time

pygame.init()

# Window size
x, y = 600, 400
win = pygame.display.set_mode((x, y))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Game settings
block_size = 10
snake_speed = 8
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# Message function
def message(msg, color):
    text = font.render(msg, True, color)
    win.blit(text, [x / 6, y / 3])

# Main game function
def gameLoop():
    game_over = False
    game_close = False

    X = x / 2
    Y = y / 2
    dx, dy = 0, 0

    snake_list = []
    length = 1

    foodx = round(random.randrange(0, x - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, y - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            win.fill(white)
            message("Game Over! Press Q to Quit or C to Play Again", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        # 🔁 MAIN GAME INPUT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -block_size
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = block_size
                    dy = 0
                elif event.key == pygame.K_UP:
                    dx = 0
                    dy = -block_size
                elif event.key == pygame.K_DOWN:
                    dx = 0
                    dy = block_size

        # Move snake head
        X += dx
        Y += dy

        # Wall collision
        # Move snake head
        X += dx
        Y += dy

        # ✅ Wrap around the screen
        if X >= x:
            X = 0
        elif X < 0:
            X = x - block_size

        if Y >= y:
            Y = 0
        elif Y < 0:
            Y = y - block_size


        win.fill(black)
        pygame.draw.rect(win, red, [foodx, foody, block_size, block_size])

        snake_head = [X, Y]
        snake_list.append(snake_head)

        if len(snake_list) > length:
            del snake_list[0]

        # Self collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw snake
        for part in snake_list:
            pygame.draw.rect(win, blue, [part[0], part[1], block_size, block_size])

        pygame.display.update()

        # Eating food
        if int(X) == int(foodx) and int(Y) == int(foody):
            foodx = round(random.randrange(0, x - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, y - block_size) / 10.0) * 10.0
            length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# 🔁 Start game
gameLoop()
