import copy
import pathlib
import random
import time
import typing as tp

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
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
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    array = []
    for i in range(0, len(values), n):
        array.append(values[i: i + n])
    return array


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return grid[pos[0]]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    array = []
    for i in grid:
        array.append(i[pos[1]])

    return array


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    pos_x: int = pos[0] // 3
    pos_y: int = pos[1] // 3
    array_tmp = []
    array = []
    for x in range(pos_x * 3, pos_x * 3 + 3):
        array_tmp.append(group(grid[x], 3))
    for y in range(3):
        array += array_tmp[y][pos_y]
    return array


def find_empty_positions(grid: tp.List[tp.List[str]]):
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for x_pos in range(len(list(grid))):
        for y_pos in range(len(list(grid))):
            if grid[x_pos][y_pos] == ".":
                return x_pos, y_pos


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    return {'1', '2', '3', '4', '5', '6', '7', '8', '9'} - set(list(get_block(grid, pos))) - set(
        list(get_col(grid, pos))) - set(list(get_row(grid, pos)))


def replace_value(grid, x, y, i):
    array = copy.deepcopy(grid)
    array[int(x)][int(y)] = i
    return array


def take_solution(array) -> tp.Optional[tp.List[tp.List[str]]]:
    for i in array:
        if i != -1 and not (i is None):
            return i


def solve(grid: tp.List[tp.List[str]]):
    e_p = find_empty_positions(grid)

    if e_p is None:
        return grid

    array = list(find_possible_values(grid, e_p))
    if len(array) == 0:
        return -1

    return take_solution([solve(replace_value(grid, e_p[0], e_p[1], i)) for i in array])


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    for x_pos in range(len(list(solution))):
        for y_pos in range(len(solution)):
            if solution[x_pos][y_pos] == ".":
                return False
            if len(set(get_col(solution, (x_pos, y_pos)))) != 9:
                return False
            if len(set(get_row(solution, (x_pos, y_pos)))) != 9:
                return False
            if len(set(get_block(solution, (x_pos, y_pos)))) != 9:
                return False
    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """

    grid = [['8', '3', '5', '4', '1', '6', '9', '2', '7'], ['2', '9', '6', '8', '5', '7', '4', '3', '1'],
            ['4', '1', '7', '2', '9', '3', '6', '5', '8'], ['5', '6', '9', '1', '3', '4', '7', '8', '2'],
            ['1', '2', '3', '6', '7', '8', '5', '4', '9'], ['7', '4', '8', '5', '2', '9', '1', '6', '3'],
            ['6', '5', '2', '7', '8', '1', '3', '9', '4'], ['9', '8', '1', '3', '4', '5', '2', '7', '6'],
            ['3', '7', '4', '9', '6', '2', '8', '1', '5']]
    k = 81
    if N >= 81:
        return grid
    while k != N:
        tmp1 = random.randint(0, 8)
        tmp2 = random.randint(0, 8)
        if grid[tmp1][tmp2] != ".":
            k -= 1
            grid[tmp1][tmp2] = "."
    return grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        tmp = time.time()
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
        print(time.time() - tmp)
