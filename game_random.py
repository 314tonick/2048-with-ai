from constants import THEME, COORD, BEST, set_value
import pygame

import random


def is_loose():
    global count
    global grid

    c = count
    copy0 = [line.copy() for line in grid]
    move_left()
    copy1 = [line.copy() for line in grid]
    move_right()
    copy2 = [line.copy() for line in grid]
    move_down()
    copy3 = [line.copy() for line in grid]
    move_up()
    copy4 = [line.copy() for line in grid]
    if copy0 == copy1 and copy0 == copy2 and copy0 == copy3 and copy0 == copy4:
        return True
    else:
        count = c
        grid = copy0
        return False


def print_grid():
    print('<GRID>')
    for e__ in grid:
        print(' '.join(map(str, e__)))
    print('</GRID>')


def draw_grid():
    for y in range(n):
        for x in range(n):
            field_surface.blit(images[grid[y][x]],
                               (50 + 400 / 21 * (x + 1) + 400 / 21 * 4 * x, 50 + 400 / 21 * (y + 1) + 400 / 21 * 4 * y))


def list_sum(lst: list):
    r = []
    for elem in lst:
        r += elem
    return r


def add_number(choices: list = None):
    global grid
    if choices is None:
        choices = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
    c = random.choice(choices)
    if all(list_sum(grid)):
        print('YOU LOST!')
        grid = [[0] * n for _ in range(n)]
        add_number()
        # raise IndexError('No free cells!')
    while True:
        i, j = random.randint(0, n - 1), random.randint(0, n - 1)
        if not grid[i][j]:
            grid[i][j] = c
            return


def del_spaces():
    for i in range(n):
        j = 0
        while j < len(grid[i]):
            if grid[i][j]:
                j += 1
            else:
                del grid[i][j]


def move_left():
    global count
    cop = [line.copy() for line in grid]
    del_spaces()
    for i in range(n):
        for j in range(len(grid[i]) - 1):
            if grid[i][j] == grid[i][j + 1]:
                count += grid[i][j] * 2
                grid[i][j] *= 2
                grid[i][j + 1] = 0
    del_spaces()
    # Filling:
    for i in range(n):
        grid[i] = grid[i].copy() + [0] * (n - len(grid[i]))
    if cop != grid:
        add_number()


def move_right():
    global count

    cop = [line.copy() for line in grid]
    del_spaces()
    for i in range(n):
        for j in range(len(grid[i]) - 2, -1, -1):
            if grid[i][j] == grid[i][j + 1]:
                count += grid[i][j] * 2
                grid[i][j + 1] *= 2
                grid[i][j] = 0
    del_spaces()
    # Filling:
    for i in range(n):
        grid[i] = [0] * (n - len(grid[i])) + grid[i].copy()
    if cop != grid:
        add_number()


def transpose_array(lst: list):
    return [[lst[j][i] for j in range(n)] for i in range(n)]


def move_down():
    global grid
    global count
    cop = [line.copy() for line in grid]
    grid = transpose_array(grid)

    del_spaces()
    for i in range(n):
        for j in range(len(grid[i]) - 2, -1, -1):
            if grid[i][j] == grid[i][j + 1]:
                count += grid[i][j] * 2
                grid[i][j + 1] *= 2
                grid[i][j] = 0
    del_spaces()
    # Filling:
    for i in range(n):
        grid[i] = [0] * (n - len(grid[i])) + grid[i].copy()
    grid = transpose_array(grid)
    if cop != grid:
        add_number()


def move_up():
    global count
    global grid

    cop = [line.copy() for line in grid]
    grid = transpose_array(grid)

    del_spaces()
    for i in range(n):
        for j in range(len(grid[i]) - 1):
            if grid[i][j] == grid[i][j + 1]:
                count += grid[i][j] * 2
                grid[i][j] *= 2
                grid[i][j + 1] = 0
    del_spaces()
    # Filling:
    for i in range(n):
        grid[i] = grid[i].copy() + [0] * (n - len(grid[i]))
    grid = transpose_array(grid)
    if cop != grid:
        add_number()


images = {
    2 ** i: pygame.transform.scale(pygame.image.load(f'{THEME}_theme\\{2 ** i}.png'), (400 // 21 * 4, 400 // 21 * 4))
    for i in
    range(1, 22)}
print('{THEME}_theme\\0.png')
images[0] = pygame.transform.scale(pygame.image.load(f'{THEME}_theme\\0.png'), (400 // 21 * 4, 400 // 21 * 4))
n = 4  # Size of the grid.
# grid = [[0] * n for _ in range(n)]
# add_number()
# add_number()
grid = [
    [4, 2, 4, 2],
    [2, 4, 2, 4],
    [4, 2, 16, 8],
    [2**20, 4, 128, 16],
]
count_image, best_image, restart_image, settings_image = \
    pygame.image.load(f'{THEME}_theme\\count.png'), pygame.image.load(f'{THEME}_theme\\best.png'), \
    pygame.image.load(f'{THEME}_theme\\restart.png'), pygame.image.load(f'{THEME}_theme\\settings.png')
pygame.init()
count = 0
font1 = pygame.font.SysFont('Consolas', 70, bold=True)
font2 = pygame.font.SysFont('Consolas', 50)
background_when_loose = pygame.Surface((500, 675), pygame.SRCALPHA)
background_when_loose.fill((70, 70, 70, 100))
pygame.draw.rect(background_when_loose, (40, 40, 40, 250), (55, 360, 380, 60))
background_when_loose.blit(font1.render('GAME OVER!', True, (200, 30, 40, 50)), (60, 360))
screen = pygame.display.set_mode((500, 675))
field_surface = pygame.Surface((500, 500))
field = pygame.transform.scale(pygame.image.load(f'{THEME}_theme\\field{n}.png'), (400, 400))
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            set_value('BEST', BEST)
            exit()
        if e.type == pygame.KEYUP and is_loose():
            grid = [[0] * n for _ in range(n)]
            add_number()
            add_number()
            count = 0
        # if e.type == pygame.KEYUP and e.key == pygame.K_UP:
        #     move_up()
        # if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
        #     move_down()
        # if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
        #     move_left()
        # if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
        #     move_right()
        # if e.type == pygame.MOUSEBUTTONUP and pygame.rect.Rect((405, 25, 65, 65)).collidepoint(pygame.mouse.get_pos()) \
        #         or e.type == pygame.KEYUP and e.key == pygame.K_r:
        #     grid = [[0] * n for _ in range(n)]
        #     add_number()
        #     add_number()
        #     count = 0
    random.choice([move_up, move_right, move_left, move_down])()
    screen.fill((0, 0, 0))
    field_surface.blit(field, COORD['field'])
    BEST = max(BEST, count)
    draw_grid()
    screen.blit(field_surface, COORD['field_surface'])
    if is_loose():
        screen.blit(background_when_loose, (0, 0))
    screen.blit(restart_image, COORD['restart'])
    screen.blit(font2.render(str(count), True, (0, 255, 0)), (230, 35))
    screen.blit(count_image, COORD['count'])
    screen.blit(font2.render(str(BEST), True, (255, 0, 0)), (230, 115))
    screen.blit(best_image, COORD['best'])
    screen.blit(settings_image, COORD['settings'])
    pygame.time.delay(200)
    pygame.display.flip()
