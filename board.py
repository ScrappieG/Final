from cell import Cell
import pygame
from sudoku_generator import  generate_sudoku

class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        # List of rows, each row is a list of cells objects.

        self.cells = [[Cell(0,i,x, screen) for i in range(0,9)] for x in range(0,9)]

        # Stores the selected row and column for easier searching.

        self.selected = selected = (None, None)

    def draw(self):
        button_font = pygame.font.Font(None, 70)

        # Draws the grid lines.

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

        # Draws sketched and locked in numbers, selection box

        for row in self.cells:
            for cell in row:
                cell.draw()

        # For use in main.

        return reset_rectangle, restart_rectangle, exit_rectangle

    def select(self, row, col):

        # Sets the boards selected property to the row and column.

        self.selected = row, col

        # Updates all cells to deselect previously selected cells.

        for r in self.cells:
            for c in r:
                if c.selected:
                    c.selected = False

        # If the selection is not out of bounds, set the cell to be selected.

        if row != None and col != None:
            self.cells[col][row].selected = True
        return

    def click(self, x, y):

        # Gets position of cursor.

        row = y // 60
        col = x // 60

        # Checks if cursor is within the grid (smaller than the actual screen)

        if 2 < row < 12 and 12 > col > 2:
            row = row - 3
            col = col - 3

            # Selects the box using adjusted row and column values.

            self.select(row, col)
            return row, col
        else:

            # If invalid selection, removes the selection box.

            self.select(None, None)
            return None

    def clear(self):

        # Sets the selected cells value to the default.

        self.cells[self.selected[1]][self.selected[0]].set_cell_value(0)

        return

    def sketch(self, number):

        # Sets the sketched value of the cell to the number provided.
        selectedcell = self.cells[self.selected[1]][self.selected[0]]
        if not selectedcell.generated:
            selectedcell.set_sketched_value(number)


        return

    def place_number(self, value):

        # Sets the value of the cell to the number provided, removes the sketched value.
        selectedcell = self.cells[self.selected[1]][self.selected[0]]
        if not selectedcell.generated:
            selectedcell.set_sketched_value(0)
            selectedcell.set_cell_value(value)

        return

    def reset_to_original(self):

        # Sets all values (actual functionality ) of player controlled cells (intentional functionality) to none.

        for r in self.cells:
            for c in r:
                if not c.generated:
                    c.set_cell_value(0)
        return

    def is_full(self):

        # Goes through every cell, if one has the default value, returns false, otherwise, returns true.

        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False

        return True

    def update_board(self, update):
        for i, row in enumerate(self.cells):
            for x, cell in enumerate(row):
                if update[i][x] != 0:
                    self.cells[i][x].generated = True
                self.cells[i][x].set_cell_value(update[i][x])
        return

    def find_empty(self):
        found = None

        for i, row in enumerate(self.cells):
            for x,cell in enumerate(row):
                if cell.value == 0:
                    found = i,x

        return tuple(i,x)

    def check_board(self, solution):
        for i,r in enumerate(self.cells):
            for x,c in enumerate(r):
                if str(c.value) != str(solution[i][x]):
                    return False
        return True