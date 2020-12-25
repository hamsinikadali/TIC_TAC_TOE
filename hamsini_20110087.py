# importing modules
import pygame
import sys
import numpy as np

# initializing pygame
pygame.init()

# constants
width_of_screen = 800
length_of_screen = 800
number_of_rows = 4
number_of_columns = 4

line_length = 15
winning_line_length = 15
block_size = 200
circle_radius = 60
circle_width = 15
crossmark_width = 25
space = 55

# olive green
circle_color = (85, 107, 47)
# green yellow
crossmark_color = (173, 255, 47)
# grey
background = (211, 211, 211)
# navy blue
line_color = (0, 0, 128)
# pink
winning_line_color =(255, 105,180)

# opening a window
window = pygame.display.set_mode((width_of_screen, length_of_screen))
pygame.display.set_caption('Tic Tac Toe')
window.fill(background)

grid = np.zeros((number_of_rows, number_of_columns))


# drawing horizontal and vertical lines
def draw_lines():
    # 1st horizontal line
    pygame.draw.line(window, line_color, (0, 200), (800, 200), line_length)
    # 2nd horizontal line
    pygame.draw.line(window, line_color, (0, 400), (800, 400), line_length)
    # 3rd horizontal line
    pygame.draw.line(window, line_color, (0, 600), (800, 600), line_length)

    # 1st vertical line
    pygame.draw.line(window, line_color, (200, 0), (200, 800), line_length)
    # 2nd vertical line
    pygame.draw.line(window, line_color, (400, 0), (400, 800), line_length)
    # 3rd vertical line
    pygame.draw.line(window, line_color, (600, 0), (600, 800), line_length)


# indicating player "2" and player "1" as "crossmark" and "circle" and drawing them
def draw_figures():
    for row in range(number_of_rows):
        for col in range(number_of_columns):
            # "1" player has circle shape
            if grid[row][col] == 1:
                pygame.draw.circle(window, circle_color, (int(col * 200 + 100), int(row * 200 + 100)), circle_radius,
                                   circle_width)
            # "2" player has cross mark shape
            elif grid[row][col] == 2:
                # 1st cross line
                pygame.draw.line(window, crossmark_color, (col * 200 + 55, row * 200 +145),
                                 (col * 200 + 145, row * 200 + 55), crossmark_width)
                # 2nd cross line
                pygame.draw.line(window, crossmark_color, (col * 200 + 55, row * 200 + 55),
                                 (col * 200 + 145, row * 200 + 145), crossmark_width)


# drawing horizontal winning line
def drawing_horizontal_winning_line(row, player):
    Y = row * 200 + 100

    if player == 1:
        a = circle_color
    elif player == 2:
        a = crossmark_color

    pygame.draw.line(window, a, (15, Y), (785, Y), winning_line_length)


# drawing vertical winning line
def drawing_vertical_winning_line(col, player):
    X = col * 200 + 100

    if player == 1:
        a = circle_color
    elif player == 2:
        a = crossmark_color

    pygame.draw.line(window, a, (X, 15), (X, 785), line_length)


def drawing_1st_diagonal(player):
    if player == 1:
        b = circle_color
    elif player == 2:
        b = crossmark_color

    pygame.draw.line(window, b, (15, 785), (785, 15), winning_line_length)


def drawing_2nd_diagonal(player):
    if player == 1:
        a = circle_color
    elif player == 2:
        a = crossmark_color

    pygame.draw.line(window, a, (15, 15), (785, 785), winning_line_length)


# checks whether square block is available
def available_square(row, col):
    return grid[row][col] == 0


# marking the square block
def marking_square(row, col, player):
    grid[row][col] = player


# checking if grid is full of symbols
def checking_if_grid_is_full():
    for row in range(number_of_rows):
        for col in range(number_of_columns):
            if grid[row][col] == 0:
                return False
    return True


# checking winner
def checking_win(player):
    # row winner checking
    for row in range(number_of_rows):
        if grid[row][0] == player and grid[row][1] == player and grid[row][2] == player and grid[row][3] == player:
            drawing_horizontal_winning_line(row, player)
            return True

    # column winner checking
    for col in range(number_of_columns):
        if grid[0][col] == player and grid[1][col] == player and grid[2][col] == player and grid[3][col] == player:
            drawing_vertical_winning_line(col, player)
            return True

    # 1st diagonal win check
    if grid[3][0] == player and grid[2][1] == player and grid[1][2] == player and grid[0][3] == player:
        drawing_1st_diagonal(player)
        return True

    # 2nd diagonal win chek
    if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player and grid[3][3] == player:
        drawing_2nd_diagonal(player)
        return True

    return False


# restarting if all square blocks are full
def restart():
    window.fill(background)
    draw_lines()
    for row in range(number_of_rows):
        for col in range(number_of_columns):
            grid[row][col] = 0


draw_lines()

player = 1
game_over = False

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            # shows us where the cursor is placed
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            selected_row = int(mouseY // 200)
            selected_col = int(mouseX // 200)

            if available_square(selected_row, selected_col):

                marking_square(selected_row, selected_col, player)

                if checking_win(player):
                    game_over = True
                # if game is not over , it turns over the player
                if player == 1:
                    player = 2
                else:
                    player = 1

                draw_figures()

    # displays the window after every turn
    pygame.display.update()
