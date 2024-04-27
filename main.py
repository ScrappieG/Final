import sudoku_generator
from cell import Cell
from board import Board
from sudoku_generator import SudokuGenerator, generate_sudoku
import pygame
import sys

# game size
WIDTH = 900
HEIGHT = 900
# colors
BUTTON_COLOR = "orange"
BACKGROUND_COLOR = "white"
TITLE_FONT_COLOR = "black"


def draw_game_start(screen):
    screen.fill("white")
    button_font = pygame.font.Font(None, 70)
    title_font = pygame.font.Font(None, 100)
    mode_font = pygame.font.Font(None, 80)

    # initialize title
    title_surface = title_font.render("Welcome to Sudoku", 0, TITLE_FONT_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(title_surface, title_rectangle)

    mode_surface = mode_font.render("Select Game Mode:", 0, TITLE_FONT_COLOR)
    mode_rectangle = mode_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(mode_surface, mode_rectangle)

    # Buttons
    # Render button text
    easy_button = button_font.render("EASY", 0, (255, 255, 255))
    medium_button = button_font.render("MEDIUM", 0, (255, 255, 255))
    hard_button = button_font.render("HARD", 0, (255, 255, 255))

    # Button surface
    easy_buttonSurface = pygame.Surface((easy_button.get_width() + 20, easy_button.get_height() + 20))
    easy_buttonSurface.fill(BUTTON_COLOR)
    easy_buttonSurface.blit(easy_button, (10, 10))

    medium_buttonSurface = pygame.Surface((medium_button.get_width() + 20, medium_button.get_height() + 20))
    medium_buttonSurface.fill(BUTTON_COLOR)
    medium_buttonSurface.blit(medium_button, (10, 10))

    hard_buttonSurface = pygame.Surface((hard_button.get_width() + 20, hard_button.get_height() + 20))
    hard_buttonSurface.fill(BUTTON_COLOR)
    hard_buttonSurface.blit(hard_button, (10, 10))

    # rectangles
    easy_rectangle = easy_buttonSurface.get_rect(center=((WIDTH//3) - 100, HEIGHT - (HEIGHT//3)))
    medium_rectangle = medium_buttonSurface.get_rect(center=(WIDTH//2, HEIGHT - (HEIGHT//3)))
    hard_rectangle = hard_buttonSurface.get_rect(center=((WIDTH - (WIDTH//3)) + 100, HEIGHT - (HEIGHT//3)))

    screen.blit(easy_buttonSurface, easy_rectangle)
    screen.blit(medium_buttonSurface, medium_rectangle)
    screen.blit(hard_buttonSurface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return easy_rectangle
                elif medium_rectangle.collidepoint(event.pos):
                    return medium_rectangle
                elif hard_rectangle.collidepoint(event.pos):
                    return hard_rectangle
            pygame.display.update()


def draw_game_end(screen, win):
    # Wipe away sudoku board.
    screen.fill("white")
    button_font = pygame.font.Font(None, 70)
    title_font = pygame.font.Font(None, 100)
    mode_font = pygame.font.Font(None, 80)

    if win == "Win":
        title_surface = title_font.render("You win!", 0, TITLE_FONT_COLOR)
    else:
        title_surface = title_font.render("Game over!", 0, TITLE_FONT_COLOR)

    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(title_surface, title_rectangle)


def draw_board(screen, selected_square, locked_in, sketched_in):
    button_font = pygame.font.Font(None, 70)
    sketch_font = pygame.font.Font(None, 45)
    number_font = pygame.font.Font(None, 60)

    for i in range(0,10):
        if i % 3 == 0:
            thickness = 4
        else: thickness = 1

        pygame.draw.line(screen, TITLE_FONT_COLOR, [180 + i * 60, 180], [180 + i * 60, HEIGHT-180], thickness)
    for i in range(0,10):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(screen, TITLE_FONT_COLOR, [180, 180 + i * 60], [WIDTH-180, 180 + i * 60], thickness)

    # options
    # Render option text
    reset_button = button_font.render("Reset", 0, (255, 255, 255))
    restart_button = button_font.render("Restart", 0, (255, 255, 255))
    exit_button = button_font.render("Exit", 0, (255, 255, 255))

    # option surface
    reset_buttonSurface = pygame.Surface((reset_button.get_width() + 20, reset_button.get_height() + 20))
    reset_buttonSurface.fill(BUTTON_COLOR)
    reset_buttonSurface.blit(reset_button, (10, 10))

    restart_buttonSurface = pygame.Surface((restart_button.get_width() + 20, restart_button.get_height() + 20))
    restart_buttonSurface.fill(BUTTON_COLOR)
    restart_buttonSurface.blit(restart_button, (10, 10))

    exit_buttonSurface = pygame.Surface((exit_button.get_width() + 20, exit_button.get_height() + 20))
    exit_buttonSurface.fill(BUTTON_COLOR)
    exit_buttonSurface.blit(exit_button, (10, 10))

    # rectangles
    reset_rectangle = reset_buttonSurface.get_rect(center=((WIDTH // 3) - 100, HEIGHT - (HEIGHT // 12)))
    restart_rectangle = restart_buttonSurface.get_rect(center=(WIDTH // 2, HEIGHT - (HEIGHT // 12)))
    exit_rectangle = exit_buttonSurface.get_rect(center=((WIDTH - (WIDTH // 3)) + 100, HEIGHT - (HEIGHT // 12)))

    screen.blit(reset_buttonSurface, reset_rectangle)
    screen.blit(restart_buttonSurface, restart_rectangle)
    screen.blit(exit_buttonSurface, exit_rectangle)

    # Draws Selection box

    if selected_square != "":
        rc = str.split(selected_square, ",")
        col = int(rc[0])
        row = int(rc[1])
        selection_box = pygame.draw.rect(screen, BUTTON_COLOR, [180 + col * 60, 180 + row * 60, 60, 60], 3)

    # Draws sketched and locked in numbers

    for i,v in enumerate(sketched_in):
        for x,y in enumerate(v):
            if y != "":
                sketched_text = sketch_font.render(y, 0, (100,100,100))
                screen.blit(sketched_text, dest=[185 + i * 60, 185 + x * 60])

    for i,v in enumerate(locked_in):
        for x,y in enumerate(v):
            if y != "":
                sketched_text = number_font.render(y, 0, (0,0,0))
                screen.blit(sketched_text, dest=[198 + i * 60, 191 + x * 60])

    return reset_rectangle, restart_rectangle, exit_rectangle


def main():
    # setup pygame
    selected_square = ""
    locked_in = [["" for i in range(0,9)] for i in range(0,9)]
    sketched_in = [["" for i in range(0,9)] for i in range(0,9)]

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    horizontal = {"left":-1,"right":1}
    vertical = {"up":-1, "down":1}

    draw_game_start(screen)

    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("light blue")

        # Defaults the selected square, row,column to none.
        rc = None
        col = None
        row = None

        # Draw sudoku lines, buttons, sketched and locked in numbers.
        reset_rectangle, restart_rectangle, exit_rectangle = draw_board(screen, selected_square, locked_in, sketched_in)

        # If a square is selected, sets row and column.

        if selected_square != "":
            rc = str.split(selected_square, ",")
            col = int(rc[0])
            row = int(rc[1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Controls the menu buttons.

                if reset_rectangle.collidepoint(event.pos):
                    return 0
                elif restart_rectangle.collidepoint(event.pos):
                    return 0
                elif exit_rectangle.collidepoint(event.pos):
                    running = False
                else:
                    # Selects a square if it is within the boundaries of the grid.

                    x,y = event.pos
                    row = y// 60
                    col = x // 60
                    if 2 < row < 12 and 12 > col > 2:
                        row = row - 3
                        col = col - 3
                        selected_square = ""+str(col)+ "," + str(row)
                        print(selected_square)
                    else:
                        selected_square = ""

            elif event.type == pygame.KEYDOWN:

                if rc:
                    # This sketches in a number.

                    if str.isdigit(pygame.key.name(event.key)):
                        sketched_in[col][row] = pygame.key.name(event.key)

                    # These two move the selected box with the arrow keys.

                    elif pygame.key.name(event.key) in horizontal:
                        changed = col + horizontal[pygame.key.name(event.key)]

                        if changed <= 8 and changed >= 0:
                            selected_square = "" + str(changed) + "," + str(row)

                    elif pygame.key.name(event.key) in vertical:
                        changed = row + vertical[pygame.key.name(event.key)]
                        if changed <= 8 and changed >= 0:
                            selected_square = "" + str(col) + "," + str(changed)

                    # This locks in a sketched number.

                    elif pygame.key.key_code(pygame.key.name(event.key)) == pygame.K_RETURN:
                        locked_in[col][row] = sketched_in[col][row]
                        sketched_in[col][row] = ""


            pygame.display.update()

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

    pygame.quit()
    return


if __name__ == "__main__":
    main()

