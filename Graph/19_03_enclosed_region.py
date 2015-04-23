W, B = 1, 0


def fill_enclosed(grid):
    reached = set()
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if r in (0, len(grid) - 1) or c in (0, len(grid[0]) - 1) and col == W and (r, c) not in reached:
                visit(grid, r, c, reached)
    # go through the matrix, for all white not in visited, color black
    print reached
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if (r, c) not in reached:
                grid[r][c] = B

DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def visit(grid, r, c, reached):
    reached.add((r, c))
    for a, b in DIR:
        n_r, n_c = r + a, c + b
        if 0 <= n_r < len(grid) and 0 <= n_c < len(grid[0]) and (r, c) not in reached and grid[n_r][n_c] == W:
            visit(grid, n_r, n_c, reached)



if __name__ == "__main__":

    matrix_1 = [[1, 1, 1, 1],
                [0, 0, 0, 0],
                [1, 0, 1, 0],
                [1, 1, 0, 1],
                ]
    matrix_2 = [[1, 1, 1, 1],
                [0, 1, 1, 0],
                [1, 1, 1, 0],
                ]
    # flip_dfs(matrix_1, (3, 0))
    fill_enclosed(matrix_1)
    for i in matrix_1:
        print i
    # _flip2(matrix_1, 3, 0)
    # for i in matrix_1:
    #     print i


    # print search(matrix_2, (2, 0), (0, 3))








