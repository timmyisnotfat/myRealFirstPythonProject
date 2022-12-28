# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        square = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in square[i // 3][j // 3]:
                        print('第',i+1,'和第',j+1,"列出现错误")
                        return False
                    else:
                        row[i].add(board[i][j])
                        col[j].add(board[i][j])
                        square[i // 3][j // 3].add(board[i][j])
        return True
    def solveSudoku(self, board: list[list[str]]) -> None:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        square = [[set() for _ in range(3)]for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    square[i//3][j//3].add(board[i][j])
        def dfs(i,j):
            if board[i][j] != 0:
                if i==8 and j ==8:
                    self.flag = True
                    return
                if j < 8:
                    dfs(i,j+1)
                else:
                    dfs(i+1,0)
            else:
                for candi in range(1,10):
                    candi = str(candi)
                    if candi not in row[i] and candi not in col[j] and candi not in square[i//3][j//3]:
                        board[i][j] = candi
                        row[i].add(candi)
                        col[j].add(candi)
                        square[i//3][j//3].add(candi)
                        if i == 8 and j == 8:
                            self.flag = True
                            return
                        if j < 8:
                            dfs(i,j+1)
                        else:
                            dfs(i+1,0)
                        if self.flag:
                            return
                        board[i][j] = 0
                        row[i].remove(candi)
                        col[j].remove(candi)
                        square[i//3][j//3].remove(candi)
        self.flag = False
        dfs(0,0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s=Solution()
    board = [[5, 3, 0, 0, 7, 0, 0, 0, 0], \
            [6, 0, 0, 1, 9, 5, 0, 0, 0], \
            [0, 9, 8, 0, 0, 0, 0, 6, 0], \
            [8, 0, 0, 0, 6, 0, 0, 0, 3], \
            [4, 0, 0, 8, 0, 3, 0, 0, 1], \
            [7, 0, 0, 0, 2, 0, 0, 0, 6], \
            [0, 6, 0, 0, 0, 0, 2, 8, 0], \
            [0, 0, 0, 4, 1, 9, 0, 0, 5], \
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    if s.isValidSudoku(board):
        print('该数独是正确的')
        s.solveSudoku(board)
        print(board)
    else:
        print('该数独是错误的')
