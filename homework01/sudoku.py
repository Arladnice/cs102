import random


def read_sudoku(filename):
    """ ��������� ������ �� ���������� ����� """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


def display(values):
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(values[row][col].center(width) + \
                      ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


def group(values, n):
    """
        ������������� �������� values � ������, ��������� �� ������� �� n \
        ���������
        >>> group([1,2,3,4], 2)
        [[1, 2], [3, 4]]
        >>> group([1,2,3,4,5,6,7,8,9], 3)
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        """
    return [[values[i * n + j] for j in range(n)] for i in range(n)]
    
    
def get_row(values, pos):
    """ ���������� ��� �������� ��� ������ ������, ��������� � pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """    
    return values[pos[0]]


def get_col(values, pos):
    """ ���������� ��� �������� ��� ������ �������, ���������� � pos
        >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], \
        (0, 0))
        ['1', '4', '7']
        >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], \
        (0, 1))
        ['2', '.', '8']
        >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], \
        (0, 2))
        ['3', '6', '9']
        """
    return [values[i][pos[1]] for i in range(len(values))]


def get_block(grid, pos):  
    """ ���������� ��� �������� ��� ������ ������, ��������� � pos
   
       >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
       ['1', '2', '.']
       >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
       ['4', '.', '6']
       >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
       ['.', '8', '9']
       """    
    row, col = pos
    row = (row // 3) * 3
    col = (col // 3) * 3
    A = []
    k = -1
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            A.append(grid[i][j])
    return A


def find_empty_positions(grid):
    """ ����� ������ ��������� ������� � �����
        >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], \
        ['7', '8', '9']])
        (0, 2)
        >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], \
        ['7', '8', '9']])
        (1, 1)
        >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], \
        ['.', '8', '9']])
        (2, 0)
        """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                return (i, j)


def find_possible_values(grid, pos):
    """ ������� ��������� ���� ��������� �������� ��� ��������� �������
        >>> grid = read_sudoku('C:\cs102\homework01\cs102/puzzle1.txt')
        >>> values = find_possible_values(grid, (0,2))
        >>> set(values) == {'1', '2', '4'}
        True
        >>> values = find_possible_values(grid, (4,7))
        >>> set(values) == {'2', '5', '9'}
        True
        """
    A = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    B = set(get_row(grid, pos))
    C = set(get_col(grid, pos))
    D = get_block(grid, pos)
    A -= B
    A -= C
    for i in range(3):
        A -= set(D[i])
    return A


def check_solution(solution):
    """ ���� ������� solution �����, �� ������� True, � ��������� \
    ������ False """
    for i in range(9):
        A = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}
        if A - set(get_row(solution, (i, 0))) != {'.'}:
            return False
        A = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}
        if A - set(get_col(solution, (0, i))) != {'.'}:
            return False
    for i in ((0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6)):
        A = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}
        for e in get_block(solution, i):
            A -= set(e)
        if A != {'.'}:
            return False
    return True


def generate_sudoku(N):
    """ ��������� ������ ������������ �� N ���������
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
        >>> grid = generate_sudoku(0)
        >>> sum(1 for row in grid for e in row if e == '.')
        81
        >>> solution = solve(grid)
        >>> check_solution(solution)
        True
        """
    N -= 81
    grid = [['.' for i in range(9)] for i in range(9)]
    grid = solve(grid)
    emptyElem = [(i, j) for i in range(9) for j in range(9)]
    for k in range(N):
        remElem = random.choice(emptyElem)
        emptyElem.remove(remElem)
        grid[remElem[0]][remElem[1]] = '.'
    return grid


def solve(grid):
    """ ������� �����, ��������� � grid
        ��� ������ ������?
            1. ����� ��������� �������
            2. ����� ��� ��������� ��������, ������� ����� ���������� �� \
            ���� �������
            3. ��� ������� ���������� ��������:
                3.1. ��������� ��� �������� �� ��� �������
                3.2. ���������� ������ ���������� ����� �����
        >>> grid = read_sudoku('puzzle1.txt')
        >>> solve(grid)
        [['5', '3', '4', '6', '7', '8', '9', '1', '2'], /
        ['6', '7', '2', '1', '9', '5', '3', '4', '8'], /
        ['1', '9', '8', '3', '4', '2', '5', '6', '7'], /
        ['8', '5', '9', '7', '6', '1', '4', '2', '3'], /
        ['4', '2', '6', '8', '5', '3', '7', '9', '1'], /
        ['7', '1', '3', '9', '2', '4', '8', '5', '6'], /
        ['9', '6', '1', '5', '3', '7', '2', '8', '4'], /
        ['2', '8', '7', '4', '1', '9', '6', '3', '5'], /
        ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
        """
    pos = find_empty_positions(grid)
    if not pos:
        return grid
    val = list(find_possible_values(grid, pos))
    if not val:
        return grid
    if not pos:
        return None
    x, y = pos
    for e in val:
        grid[x][y] = e
        grid1 = solve(grid)
        if not find_empty_positions(grid1):
            return grid1
    if grid1 == grid:
        grid[x][y] = '.'
    return grid1


if __name__ == '__main__':
    for fname in ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt']:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        display(solution)
        print(check_solution(solution))
