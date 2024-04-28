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
                    return 30
                elif medium_rectangle.collidepoint(event.pos):
                    return 40
                elif hard_rectangle.collidepoint(event.pos):
                    return 50
            pygame.display.update()


def draw_game_end(screen, win):
    # Wipe away sudoku board.
    screen.fill("white")
    button_font = pygame.font.Font(None, 70)
    title_font = pygame.font.Font(None, 100)
    mode_font = pygame.font.Font(None, 80)

    exit_button = button_font.render("EXIT", 0, (255, 255, 255))
    exit_buttonSurface = pygame.Surface((exit_button.get_width() + 20, exit_button.get_height() + 20))
    exit_buttonSurface.fill("orange")
    exit_buttonSurface.blit(exit_button, (10, 10))
    exit_rectangle = exit_buttonSurface.get_rect(center=(1000,1000))

    restart_button = button_font.render("RESTART", 0, (255, 255, 255))
    restart_buttonSurface = pygame.Surface((restart_button.get_width() + 20, restart_button.get_height() + 20))
    restart_buttonSurface.fill("orange")
    restart_buttonSurface.blit(restart_button, (10, 10))
    restart_rectangle = restart_buttonSurface.get_rect(center=(1000,1000))

    if win == "Win":
        title_surface = title_font.render("You win!", 0, TITLE_FONT_COLOR)
        exit_rectangle = exit_buttonSurface.get_rect(center=(WIDTH // 2, HEIGHT - (HEIGHT // 5)))
        screen.blit(exit_buttonSurface, exit_rectangle)
    else:
        title_surface = title_font.render("Game over!", 0, TITLE_FONT_COLOR)
        restart_rectangle = restart_buttonSurface.get_rect(center=(WIDTH // 2, HEIGHT - (HEIGHT // 5)))
        screen.blit(restart_buttonSurface, restart_rectangle)

    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(title_surface, title_rectangle)


    return exit_rectangle, restart_rectangle

def main():
    # setup pygame
    selected_square = ""
    locked_in = [["" for i in range(0,9)] for i in range(0,9)]
    sketched_in = [["" for i in range(0,9)] for i in range(0,9)]

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    win = False

    horizontal = {"left":-1,"right":1}
    vertical = {"up":-1, "down":1}

    difficulty = draw_game_start(screen)

    # Instantiates board object under name newBoard.

    newBoard = Board(WIDTH,HEIGHT,screen, difficulty)

    running = True

    generatedSudoku, solution = sudoku_generator.generate_sudoku(9,difficulty)

    newBoard.update_board(generatedSudoku)

    # Does not close pygame, just switches to the end screen.

    end = False

    while running:

        if end:
            exit_rectangle, restart_rectangle = draw_game_end(screen, win)
        else:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            # fill the screen with a color to wipe away anything from last frame
            screen.fill("light blue")

            reset_rectangle, restart_rectangle, exit_rectangle = newBoard.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Controls the menu buttons.

                if reset_rectangle.collidepoint(event.pos):
                    newBoard.reset_to_original()
                elif restart_rectangle.collidepoint(event.pos):
                    end = False
                    win = False
                    difficulty = draw_game_start(screen)
                    newBoard = Board(WIDTH, HEIGHT, screen, difficulty)
                    generatedSudoku, solution = sudoku_generator.generate_sudoku(9, difficulty)

                    newBoard.update_board(generatedSudoku)

                elif exit_rectangle.collidepoint(event.pos):
                    print("a")
                    running = False
                    end = False

                else:
                    # Selects a square

                    newBoard.click(event.pos[0], event.pos[1])

            elif event.type == pygame.KEYDOWN:
                # Redundant, but breaks if changed, don't ask me why.

                if newBoard.selected[0] != None and newBoard.selected[1] != None:
                    # This sketches in a number.

                    if str.isdigit(pygame.key.name(event.key)):
                        newBoard.sketch(pygame.key.name(event.key))

                    # These two move the selected box with the arrow keys.

                    if pygame.key.name(event.key) in horizontal:

                        changed = newBoard.selected[1] + horizontal[pygame.key.name(event.key)]

                        if 0 <= changed <= 8:
                            newBoard.select(newBoard.selected[0], changed)

                    elif pygame.key.name(event.key) in vertical:

                        changed = (newBoard.selected[0] + vertical[pygame.key.name(event.key)])

                        if 0 <= changed <= 8:
                            newBoard.select(changed, newBoard.selected[1])

                    # This locks in a sketched number.

                    elif pygame.key.key_code(pygame.key.name(event.key)) == pygame.K_RETURN:
                        newBoard.place_number(
                            newBoard.cells[newBoard.selected[1]][newBoard.selected[0]].sketched_value)

                    # This erases a locked in number.

                    elif pygame.key.key_code(pygame.key.name(event.key)) == pygame.K_BACKSPACE:
                        newBoard.clear()

        full = newBoard.is_full()
        if full:
            result = newBoard.check_board(solution)
            if result:
                win = "Win"
            else:
                win = "Lose"
            end = True

        pygame.display.update()

        # flip() the display to put your work on screen

        pygame.display.flip()

    pygame.quit()
    return


if __name__ == "__main__":
    main()