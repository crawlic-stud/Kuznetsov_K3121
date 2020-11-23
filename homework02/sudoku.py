import pathlib
import typing as tp
import random
T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    group_res = []
    for i in range(0, len(values), n):
        group_res.append(values[i:i+n])
    return group_res
        
    pass


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    get_row_res = grid[pos[0]]
    return get_row_res
    


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    get_col_res = []
    for i1 in grid:
        get_col_res.append(i1[pos[1]])
    return get_col_res
    


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    get_block_res = []

    row, col = pos
    row_count, col_count = row // 3 * 3, col // 3 * 3

    for row in range(row_count, row_count + 3):
        get_block_res += grid[row][col_count: col_count + 3]

    return get_block_res


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    length = len(grid)
    for row in range(length):
        for col in range(length):
            if grid[row][col] == ".":
                return row, col


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    values = set('123456789')
    return values - set(get_row(grid, pos)) - set(get_col(grid, pos)) - set(get_block(grid, pos))


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    pos = find_empty_positions(grid)
    if not pos:
        return grid

    values = find_possible_values(grid, pos)
    row, col = pos

    for value in values:
        grid[row][col] = value

        solution = solve(grid)
        if solution is not None:
            return solution

    grid[row][col] = "."


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    for row in range(len(solution)):
        if set(solution[row]) != set("123456789"):
            return False

    for col in range(len(solution)):
        if set(get_col(solution, (0, col))) != set("123456789"):
            return False

    for row in range(len(solution), 3):
        for col in range(len(solution), 3):
            block = set(get_block(solution, (row, col)))
            if block != set("123456789"):
                return False

    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    grid = solve([["."] * 9 for _ in range(9)])
    N = 0 if N > 81 else 81 - N

    while N != 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        if grid[row][col] != '.':
            grid[row][col] = '.'
            N -= 1

    return grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print("Puzzle {fname} can't be solved")
        else:
            display(solution)
