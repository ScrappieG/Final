from cell import Cell
from board import Board
from sudoku_generator import SudokuGenerator, generate_sudoku
import pygame
import sys

# game size
WIDTH = 1080
HEIGHT = 720
# colors
BUTTON_COLOR = "orange"
BACKGROUND_COLOR = "white"
TITLE_FONT_COLOR = "black"


def draw_game_start(screen):
    title_font = pygame.font.Font(None, 100)
    mode_font = pygame.font.Font(None, 80)
    button_font = pygame.font.Font(None, 70)
    screen.fill("white")

    # initialize title
    title_surface = title_font.render("Welcome to Sudoku",0, TITLE_FONT_COLOR)
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



def main():
    # setup pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    draw_game_start(screen)

    screen.fill(BACKGROUND_COLOR)

    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("light blue")

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

    pygame.quit()
    return


if __name__ == "__main__":
    main()

