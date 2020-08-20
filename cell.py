from pygame import draw

class Cell:
    def __init__(self, width, height, x, y, color=(255, 255, 255)):
        self.width, self.height = width, height
        self.x, self.y = x, y
        self.color = color

    def __repr__(self):
        return f'<Cell: {self.width}x{self.height}>'

    def draw(self, surface):
        rect = (self.x*self.width, self.y*self.height, self.width, self.height)
        draw.rect(surface, self.color, rect)

    def selected(self, pos):
        return self.x == pos[0]//self.width and self.y == pos[1]//self.height