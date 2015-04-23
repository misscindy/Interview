# EPI 19 _ 03

DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def flip_dfs(grid, start):
    cell_color = grid[start[0]][start[1]]
    # print cell_color
    _flip(grid, start, cell_color)


def _flip(grid, cur_pos, color):
    r, c = cur_pos
    for a, b in DIR:
        nxt_pos = r + a, c + b
        if is_valid(grid, nxt_pos, color):
            grid[nxt_pos[0]][nxt_pos[1]] = not color
            _flip(grid, nxt_pos, color)


def _flip_bfs(grid, r, c):
    color = grid[r][c]
    grid[r][c] = not color

    queue = [(r, c)]

    while queue:
        x, y = queue.pop(0)
        for a, b in DIR:
            nxt_r, nxt_c = x + a, y + b
            if is_valid(grid, (nxt_r, nxt_c), color):
                # print ~color
                grid[nxt_r][nxt_c] = not color
                queue.append((nxt_r, nxt_c))


def _flip2(grid, r, c):
    color = grid[r][c]
    grid[r][c] = not color
    for a, b in DIR:
        new_r, new_c = r + a, c + b
        if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == color:
            _flip2(grid, new_r, new_c)


def is_valid(grid, ndx, color):
    r, c = ndx
    m, n = len(grid), len(grid[0])
    if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != color:
        return False

    return True


if __name__ == "__main__":

    matrix_1 = [[1, 1, 1, 1],
                [0, 1, 1, 0],
                [1, 0, 1, 0],
                [1, 1, 0, 1],
                ]
    matrix_2 = [[1, 1, 1, 1],
                [0, 1, 1, 0],
                [1, 1, 1, 0],
                ]
    # flip_dfs(matrix_1, (3, 0))
    _flip_bfs(matrix_1, 3, 0)
    for i in matrix_1:
        print i
    # _flip2(matrix_1, 3, 0)
    # for i in matrix_1:
    #     print i


    # print search(matrix_2, (2, 0), (0, 3))




