from enum import Enum
from typing import NamedTuple, List, Optional
from generic_search import Node, dfs, bfs, node_to_path
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

    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal

    def successors(self, ml: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []
        if ml.row - 1 >= 0:
            locations.append(MazeLocation(ml.row - 1, ml.column))
        if ml.row + 1 < self.row:
            locations.append(MazeLocation(ml.row + 1, ml.column))
        if ml.column - 1 >= 0:
            locations.append(MazeLocation(ml.row, ml.column - 1))
        if ml.column + 1 < self.column:
            locations.append(MazeLocation(ml.row, ml.column + 1))
        return [
            l for l in locations
            if self.grid[l.row][l.column] != Cell.BLOCKED
        ]

    def mark(self, path: List[MazeLocation]):
        for maze_location in path:
            self.grid[maze_location.row][maze_location.column] = Cell.PATH
        self.grid[self.start.row][self.start.column] = Cell.START
        self.grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path: List[MazeLocation]):
        for maze_location in path:
            self.grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self.grid[self.start.row][self.start.column] = Cell.START
        self.grid[self.goal.row][self.goal.column] = Cell.GOAL


if __name__ == '__main__':
    maze = Maze()
    print(maze)

    solution_dfs: Optional[Node[MazeLocation]] = dfs(maze.start,
                                                     maze.goal_test,
                                                     maze.successors)
    if (solution_dfs is None):
        print("No solution found using depth-first-search!")
    else:
        path_dfs: List[MazeLocation] = node_to_path(solution_dfs)
        maze.mark(path_dfs)
        print(maze)
        maze.clear(path_dfs)

    solution_bfs: Optional[Node[MazeLocation]] = bfs(maze.start,
                                                     maze.goal_test,
                                                     maze.successors)
    if (solution_bfs is None):
        print("No solution found using depth-first-search!")
    else:
        path_bfs: List[MazeLocation] = node_to_path(solution_bfs)
        maze.mark(path_bfs)
        print(maze)
