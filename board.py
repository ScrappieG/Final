from cell import Cell
import pygame
from sudoku_generator import  generate_sudoku

class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.locked_in = [["" for i in range(0, 9)] for i in range(0, 9)]
        self.sketched_in = [["" for i in range(0, 9)] for i in range(0, 9)]
        self.selected = selected = (None, None)

    def draw(self):
        button_font = pygame.font.Font(None, 70)
        sketch_font = pygame.font.Font(None, 45)
        number_font = pygame.font.Font(None, 60)

        for i in range(0, 10):
            if i % 3 == 0:
                thickness = 4
            else:
                thickness = 1

            pygame.draw.line(self.screen, "black", [180 + i * 60, 180], [180 + i * 60, self.height - 180], thickness)
        for i in range(0, 10):
            if i % 3 == 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(self.screen, "black", [180, 180 + i * 60], [self.width - 180, 180 + i * 60], thickness)

        # options
        # Render option text
        reset_button = button_font.render("Reset", 0, (255, 255, 255))
        restart_button = button_font.render("Restart", 0, (255, 255, 255))
        exit_button = button_font.render("Exit", 0, (255, 255, 255))

        # option surface
        reset_buttonSurface = pygame.Surface((reset_button.get_width() + 20, reset_button.get_height() + 20))
        reset_buttonSurface.fill("orange")
        reset_buttonSurface.blit(reset_button, (10, 10))

        restart_buttonSurface = pygame.Surface((restart_button.get_width() + 20, restart_button.get_height() + 20))
        restart_buttonSurface.fill("orange")
        restart_buttonSurface.blit(restart_button, (10, 10))

        exit_buttonSurface = pygame.Surface((exit_button.get_width() + 20, exit_button.get_height() + 20))
        exit_buttonSurface.fill("orange")
        exit_buttonSurface.blit(exit_button, (10, 10))

        # rectangles
        reset_rectangle = reset_buttonSurface.get_rect(center=((self.width // 3) - 100, self.height - (self.height // 12)))
        restart_rectangle = restart_buttonSurface.get_rect(center=(self.width // 2, self.height - (self.height // 12)))
        exit_rectangle = exit_buttonSurface.get_rect(center=((self.width - (self.width // 3)) + 100, self.height - (self.height // 12)))

        self.screen.blit(reset_buttonSurface, reset_rectangle)
        self.screen.blit(restart_buttonSurface, restart_rectangle)
        self.screen.blit(exit_buttonSurface, exit_rectangle)

        # Draws Selection box

        # Redundant, but breaks if you change it to just if self.selected[0] and self.selected[1], don't ask me why.

        if self.selected[0] != None and self.selected[1] != None:
            col = self.selected[1]
            row = self.selected[0]
            selection_box = pygame.draw.rect(self.screen, "orange", [180 + col * 60, 180 + row * 60, 60, 60], 3)

        # Draws sketched and locked in numbers

        for i, v in enumerate(self.sketched_in):
            for x, y in enumerate(v):
                if y != "":
                    sketched_text = sketch_font.render(y, 0, (100, 100, 100))
                    self.screen.blit(sketched_text, dest=[185 + i * 60, 185 + x * 60])

        for i, v in enumerate(self.locked_in):
            for x, y in enumerate(v):
                if y != "":

                    sketched_text = number_font.render(y, 0, (0, 0, 0))
                    self.screen.blit(sketched_text, dest=[198 + i * 60, 191 + x * 60])

        return reset_rectangle, restart_rectangle, exit_rectangle

    def select(self, row, col):
        self.selected = row, col
        return

    def click(self, x, y):
        row = y // 60
        col = x // 60

        if 2 < row < 12 and 12 > col > 2:
            row = row - 3
            col = col - 3
            self.select(row, col)
            return row, col
        else:
            self.select(None, None)
            return None

    def clear(self):
        self.locked_in[self.selected[1]][self.selected[0]] = ""
        return

    def sketch(self, number):
        self.sketched_in[self.selected[1]][self.selected[0]] = number
        return

    def place_number(self, value):
        self.locked_in[self.selected[1]][self.selected[0]] = value
        self.sketched_in[self.selected[1]][self.selected[0]] = ""
        return

    def reset_to_original(self):
        self.locked_in = [["" for i in range(0, 9)] for i in range(0, 9)]
        self.sketched_in = [["" for i in range(0, 9)] for i in range(0, 9)]
        return

    def is_full(self):
        for x in self.locked_in():
            for y in x:
                if y == "":
                    return False

        return True

    def update_board(self):

        return

    def find_empty(self):


        return

    def check_board(self):
        return


