import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1



    def create_grid(self, randomize: bool = False) -> Grid:

        grid = [[0] * self.cols for x in range(self.rows)]
        if randomize:
            for i in range(self.cols):
                for j in range(self.rows):
                    grid[i][j] = random.randint(0, 1)
        return grid


    def get_neighbours(self, cell: Cell) -> Cells:
        # only alive neighbours
        cells = []
        x, y = cell
        for i in range(max(x-1, 0), min(self.rows, x+2)):
            for j in range(max(0, y-1), min(self.cols, y+2)):
                try:
                    if self.curr_generation[i][j]:
                        cells.append((i, j))
                    elif self.curr_generation[i][j] == 0:
                        cells.append((i, j))
                except:
                    pass
        cells.remove((x, y))
        return cells

    def get_next_generation(self) -> Grid:
        new = self.curr_generation
        for i in range(len(self.curr_generation)):
            for j in range(len(self.curr_generation[i])):
                if self.curr_generation[i][j] == 0:
                    if len(self.get_neighbours((i, j))) == 3:
                        new[i][j] = 1
                else:
                    if len(self.get_neighbours((i, j))) not in [2, 3]:
                        new[i][j] = 0
        self.curr_generation = new
        return new

    def step(self) -> None:
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()
        self.generations += 1
        pass

    @property
    def is_max_generations_exceeded(self) -> bool:
        if self.generations == self.max_generations:
            return True
        return False


    @property
    def is_changing(self) -> bool:
        if self.curr_generation != self.prev_generation:
            return True
        return False
        pass

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        file = open(filename)
        grid = []
        final = []
        cells = file.read()
        for i in cells:
            try:
                grid.append(int(i))
            except:
                final.append(grid)
                grid = []
                continue
        if [] in final:
            final.remove([])
        return final


    def save(self, filename: pathlib.Path) -> None:
        file = open(filename, 'w')
        for i in range(len(self.curr_generation)):
            file.write(str(self.curr_generation[i]) + "/n")
        file.close()
        pass

game = GameOfLife((10, 10), True, 5)
#print(game.from_file('glider.txt'))
#print(game.from_file('grid.txt'))
