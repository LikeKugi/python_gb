import pygame

black = (0, 0, 0)
white = (255, 255, 255)

red = (255, 0, 0)
green = (0, 255, 0)

WIDTH = 190
HEIGHT = 190
MARGIN = 8
grid = []


def create_field(grid):
    for i in range(3):
        grid.append([])
        for j in range(3):
            grid[i].append(0)


def reset_field(grid):
    for i in range(3):
        for j in range(3):
            grid[i][j] = 0


def color_field(grid, scr):
    for i in range(3):
        for j in range(3):
            color = white
            if grid[i][j] == 1:
                color = red
            elif grid[i][j] == 2:
                color = green
            pygame.draw.rect(scr,
                             color,
                             [(MARGIN + WIDTH) * j + MARGIN,
                              (MARGIN + HEIGHT) * i + MARGIN,
                              WIDTH,
                              HEIGHT])


def check_winner(grid: list):
    for i in range(3):
        if (grid[i][0] == grid[i][1] == grid[i][2]) and grid[i][0] != 0:
            return grid[i][0]
    for j in range(3):
        if (grid[0][j] == grid[1][j] == grid[2][j]) and grid[0][j] != 0:
            return grid[0][j]
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != 0:
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[1][1] != 0:
        return grid[1][1]
    return 0


def gaming():
    create_field(grid)

    pygame.init()
    window_size = [600, 600]

    scr = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Grid")
    done = False
    clock = pygame.time.Clock()

    mover = (1, 2)
    move = 0

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                j = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                grid[row][j] = mover[move % 2]
                move += 1
                print("Click ", pos, "Grid coordinates: ", row, j)
        scr.fill(black)

        color_field(grid, scr)

        winner = check_winner(grid)

        if winner != 0 or move == 9:
            print(f'player {winner} won' if winner != 0 else 'PAIR')
            move = 0
            reset_field(grid)


        clock.tick(50)
        pygame.display.flip()

    pygame.quit()


def main():
    gaming()


if __name__ == '__main__':
    main()
