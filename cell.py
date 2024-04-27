import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

        self.sketched_value = None
        self.selected = False

        # Tracks if this cell is one that contains a generated number, or is a player controlled cell.

        self.generated = False

        pass

    def set_cell_value(self, value):
        self.value = value
        return

    def set_sketched_value(self, value):
        self.sketched_value = value
        return

    def draw(self):
        sketch_font = pygame.font.Font(None, 45)
        number_font = pygame.font.Font(None, 60)

        sketched_text = sketch_font.render(self.sketched_value, 0, (100, 100, 100))
        locked_text = number_font.render(self.value, 0, (0, 0, 0))

        # IF the cell has sketched and real values, draws those values.

        if self.sketched_value != "":
            self.screen.blit(sketched_text, dest=[185 + self.col * 60, 185 + self.row * 60])
        if self.value != "":
            self.screen.blit(locked_text, dest=[198 + self.col * 60, 191 + self.row * 60])

        # draws the selection box if the cell is selected.

        if self.selected:
            selection_box = pygame.draw.rect(self.screen, "orange", [180 + self.col * 60, 180 + self.row * 60, 60, 60], 3)

        return
