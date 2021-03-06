import pygame
import random

from pygame.locals import *
from typing import List, Tuple
from copy import deepcopy


Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:

    def __init__(self, width: int=640, height: int=480, cell_size: int=10, speed: int=10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        self.grid = self.create_grid(randomize=True)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()
            self.get_next_generation()
            self.draw_lines()
            pygame.display.flip()
            clock.tick(self.speed)

    def create_grid(self, randomize: bool=False) -> Grid:
        grid = [[0] * self.cell_width for x in range(self.cell_height)]
        if randomize:
            for i in range(self.cell_height):
                for j in range(self.cell_width):
                    grid[i][j] = random.randint(0, 1)
        return grid

    def draw_grid(self) -> None:
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                color = pygame.Color('red')
                if self.grid[i][j] == 1:
                    color = pygame.Color('black')
                pygame.draw.rect(self.screen, color,
                                 (self.cell_size * j, self.cell_size * i, self.cell_size, self.cell_size))

    def get_neighbours(self, cell: Cell) -> Cells:
        cells = []
        x, y = cell
        for i in range(max(x-1, 0), min(self.cell_height, x+2)):
            for j in range(max(0, y-1), min(self.cell_width, y+2)):
                if i == x and j == y:
                    continue
                cells.append(self.grid[i][j])
        return cells

    def get_next_generation(self) -> Grid:
        new = deepcopy(self.grid)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 0:
                    if sum(self.get_neighbours((i, j))) == 3:
                        new[i][j] = 1
                else:
                    if sum(self.get_neighbours((i, j))) not in [2, 3]:
                        new[i][j] = 0
        self.grid = new
        return self.grid

if __name__ == '__main__':
    game = GameOfLife(500, 500, 20)
    game.run()

"""
print(game.cell_width)
print(game.cell_height)
print(game.get_neighbours((0, 0)))
print(game.get_neighbours((2, 3)))
print(game.get_neighbours((0, 7)))
print(game.get_neighbours((5, 0)))
print(game.get_neighbours((5, 7)))
"""
#print(game.get_neighbours((10, 10)))

