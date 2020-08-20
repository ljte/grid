from cell import Cell
from pygame import draw

class Grid:
    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell(width//rows, height//cols, i, j) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height

    def __repr__(self):
        return f'<Grid: {self.width}x{self.height}>'

    def draw(self, surface):
        for row in self.cells:
            for cell in row:
                cell.draw(surface)

        gap = self.width // self.rows
        for i in range(max(self.rows, self.cols)):
            draw.line(surface, (0, 0, 0), (0, i*gap), (self.width, i*gap))
            draw.line(surface, (0, 0, 0), (i*gap, 0), (i*gap, self.height))

    def cell_clicked(self, click):
        for row in self.cells:
            for cell in row:
                if cell.selected(click):
                    cell.color = (255, 0, 0)

    def clear(self):
        for row in self.cells:
            for cell in row:
                cell.color = (255, 255, 255)




