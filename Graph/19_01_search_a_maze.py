DIR = [(0, 1), (-1, 0), (0, -1), (1, 0)]
BLOCK, WHITE = 0, 1


def search(matrix, start, end):

    def is_valid(grid, pos):
        r, c = pos
        m, n = len(grid), len(grid[0])
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == BLOCK:
            return False
        return True

    def _search_path(grid, exit, cur_pos, path, visited):
        if cur_pos == exit:
            # print "here", path
            return path
        r, c = cur_pos
        for (a, b) in DIR:
            nxt_pos = (r + a, c + b)
            # print nxt_pos
            if is_valid(grid, nxt_pos) and (nxt_pos not in visited):
                # print nxt_pos, path
                path.append(nxt_pos)
                visited.add(nxt_pos)
                if _search_path(grid, exit, nxt_pos, path, visited):
                    # print "herro"
                    return path
                path.pop()
                # visited.remove(nxt_pos)
        return None

    def _search_path2(grid, exit, cur_pos, path):
        if cur_pos == exit:
            # print "here", path
            return True
        r, c = cur_pos
        for (a, b) in DIR:
            nxt_pos = (r + a, c + b)
            # print nxt_pos
            if is_valid(grid, nxt_pos):
                # print nxt_pos, path
                grid[nxt_pos[0]][nxt_pos[1]] = BLOCK
                path.append(nxt_pos)
                if _search_path2(grid, exit, nxt_pos, path):
                    return path
                path.pop()
                # visited.remove(nxt_pos)
        return False
    res, res2 = [], []
    _search_path(matrix, end, start, res, set(start))
    matrix[start[0]][start[1]] = BLOCK
    _search_path2(matrix, end, start, res2)
    return res, res2, matrix




if __name__ == "__main__":
    matrix_1 = [[1, 1, 1, 1],
                [0, 1, 1, 0],
                [1, 0, 1, 0],
                [1, 1, 1, 1],
                ]
    matrix_2 = [[1, 1, 1, 1],
                [0, 1, 1, 0],
                [1, 1, 1, 0],
                ]
    for i in (search(matrix_1, (3, 0), (0, 3))):
        print i
    # print search(matrix_2, (2, 0), (0, 3))


