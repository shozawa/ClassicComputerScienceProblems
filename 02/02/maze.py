from enum import Enum
from typing import NamedTuple, List
import random


class Cell(Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"


class MazeLocation(NamedTuple):
    row: int
    column: int


class Maze:
    def __init__(self, row=10, column=10, sparseness=0.2,
                 start=MazeLocation(0, 0), goal=MazeLocation(9, 9)):
        self.row = row
        self.column = column
        self.start = start
        self.goal = goal
        self.grid: List[List[Cell]] = [
            [Cell.EMPTY for c in range(self.column)] for r in range(self.row)]
        self.place_block(row, column, sparseness)
        self.grid[self.start.row][self.start.column] = Cell.START
        self.grid[self.goal.row][self.goal.column] = Cell.GOAL

    def place_block(self, row: int, column: int, sparseness: float) -> None:
        for row in range(row):
            for column in range(column):
                if random.uniform(0.0, 1.0) < sparseness:
                    self.grid[row][column] = Cell.BLOCKED

    def __str__(self) -> str:
        output = ''
        for row in self.grid:
            output += ''.join([c.value for c in row]) + '\n'
        return output


if __name__ == '__main__':
    maze = Maze()
    print(maze)
