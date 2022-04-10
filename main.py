import sys
import pygame
import random

size = width, height = 800, 800
blue = 0, 0, 255
player_length = 2

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


grid = []
for i in range(8):
    colume = []
    for j in range(8):
        tile = pygame.image.load("background.png").convert()
        colume.append(tile)
    grid.append(colume)

apple = pygame.image.load("apple.png").convert()

apple_cords = (random.randint(0, 7), random.randint(0, 7))
while apple_cords == (3, 3):
    apple_cords = (random.randint(0, 7), random.randint(0, 7))
apple_x, apple_y = apple_cords
grid[apple_x][apple_y] = apple

player_x = 3
player_y = 3
player_direction = "+x"
tail_cords = []
screen.fill(blue)
current_length = 1
while True:
    try:
        grid[player_x][player_y]
    except IndexError:
        sys.exit()
    clock.tick()
    clock.tick_busy_loop(60)
    pygame.time.wait(200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_direction = "-y"
            elif event.key == pygame.K_DOWN:
                player_direction = "+y"
            elif event.key == pygame.K_LEFT:
                player_direction = "-x"
            elif event.key == pygame.K_RIGHT:
                player_direction = "+x"
    player_pos = (player_x, player_y)
    if player_pos == (0 ,0):
        player_length += 1

    if i >= 0:
        head = pygame.image.load("snake.png").convert()
        player_pos = (player_x, player_y)
        tail_cords.append(player_pos)
        if player_direction == "+x":
            player_x += 1
            grid[player_x][player_y] = head
        elif player_direction == "-x":
            player_x -= 1
            if player_x < 0:
                sys.exit()
            grid[player_x][player_y] = head
        elif player_direction == "-y":
            player_y -= 1
            if player_y < 0:
                sys.exit()
            grid[player_x][player_y] = head
        elif player_direction == "+y":
            player_y += 1
            grid[player_x][player_y] = head
        player_pos = (player_x, player_y)
        if player_pos in tail_cords:
            sys.exit()
        if player_pos == apple_cords:
            player_length += 1
            apple_cords = (random.randint(0, 7), random.randint(0, 7))
            while apple_cords == player_pos or apple_cords in tail_cords:
                apple_cords = (random.randint(0, 7), random.randint(0, 7))
            apple_x, apple_y = apple_cords
            grid[apple_x][apple_y] = apple
        if player_length != current_length:
            current_length = player_length
        else:
            tail_pos = tail_cords[0]
            tail_x, tail_y = tail_pos
            grid[tail_x][tail_y] = tile
            del tail_cords[0]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            screen.blit(grid[i][j], (i * 101, j * 101))
    pygame.display.flip()


