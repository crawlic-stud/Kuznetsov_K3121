import pathlib
import random
import typing as tp
from copy import deepcopy
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
        grid = [[random.randint(0, 1) for y in range(self.cols)] for x in range(self.rows)]
        if randomize:
            pass
        else:
            grid = [[0 for y in range(self.cols)] for x in range(self.rows)]
        return grid



    def get_neighbours(self, cell: Cell) -> Cells:
        cells = []
        x, y = cell
        for i in range(max(x-1, 0), min(self.rows, x+2)):
            for j in range(max(0, y-1), min(self.cols, y+2)):
                if i == x and j == y:
                    continue
                cells.append(self.curr_generation[i][j])
        return cells

    def get_next_generation(self) -> Grid:
        new = deepcopy(self.curr_generation)
        for i in range(len(self.curr_generation)):
            for j in range(len(self.curr_generation[i])):
                if self.curr_generation[i][j] == 0:
                    if sum(self.get_neighbours((i, j))) == 3:
                        new[i][j] = 1
                else:
                    if sum(self.get_neighbours((i, j))) not in [2, 3]:
                        new[i][j] = 0
        return new

    def step(self) -> None:
        self.prev_generation = deepcopy(self.curr_generation)
        self.curr_generation = self.get_next_generation()
        self.generations += 1
        pass

    @property
    def is_max_generations_exceeded(self) -> bool:
        return self.generations >= self.max_generations


    @property
    def is_changing(self) -> bool:
        return self.curr_generation != self.prev_generation

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


    def save(filename: pathlib.Path) -> None:
        for i in self.curr_generation:
            for elem in i:
                filename.write_text(str(elem).replace("'", ''))
            filename.write_text('\n')

game = GameOfLife((10, 10), True, 5)
#print(game.from_file('glider.txt'))
#print(game.from_file('grid.txt'))
