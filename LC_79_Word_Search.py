class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        m, n = len(board), len(board[0])

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    visit_board = [[True]*n for i in range(m)]
                    if self._exist(board, visit_board, word, 0, (r, c)):
                        # print r, c
                        return True
        return False

    def _exist(self, board, visit_board, word, matched, pos):
        # backtracking
        if matched == len(word) - 1:
            print matched, pos
            return True

        # four directions
        DIR = {(-1, 0), (1, 0), (0, 1), (0, -1)}
        x, y = pos
        for a, b in DIR:
            temp_x, temp_y = x + a, y + b
            if (self.is_valid(temp_x, temp_y, visit_board) and board[temp_x][temp_y] == word[matched + 1]):
                visit_board[x][y] = False
                print temp_x, temp_y
                print visit_board

                if self._exist(board, visit_board, word, matched + 1, (temp_x, temp_y)):
                    return True
                visit_board[temp_x][temp_y] = True
        return False

    def is_valid(self, x, y, visit_board):
        m, n = len(visit_board), len(visit_board[0])
        if x < 0 or x > (m - 1) or y < 0 or y > (n - 1) or (not visit_board[x][y]):
            return False
        return True






a = Solution()
print a.exist(["aa"], "aaa")