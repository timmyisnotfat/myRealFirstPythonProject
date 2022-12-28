import sys

class Solution:
    def isValidSudoku(self, board):
        row = [set() for i in range(9)]
        col = [set() for j in range(9)]
        block = [[set() for i in range(3)] for j in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in block[i // 3][j // 3]:
                        print('The row',i+1,'and the column',j+1,"occur error")
                        return False
                    else:
                        row[i].add(board[i][j])
                        col[j].add(board[i][j])
                        block[i // 3][j // 3].add(board[i][j])

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
                for Cdd in range(1,10):
                    if Cdd not in row[i] and Cdd not in col[j] and Cdd not in block[i//3][j//3]:
                        board[i][j] = Cdd
                        row[i].add(Cdd)
                        col[j].add(Cdd)
                        block[i//3][j//3].add(Cdd)
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
                        row[i].remove(Cdd)
                        col[j].remove(Cdd)
                        block[i//3][j//3].remove(Cdd)
        self.flag = False
        dfs(0,0)
        return True


if __name__ == '__main__':
    s = Solution()
    input_file = sys.argv[1]
    filereader = open(input_file, 'r')
    board = []
    for row in filereader:
            _str = list(row.rstrip().replace(',', ''))
            board.append([int(x) for x in _str])

    if s.isValidSudoku(board):
        print('The Sudoku is valid')
        s.isValidSudoku(board)
        for i in range(9):
            for j in range(9):
                if(j == 8):
                    print(board[i][j])
                else:
                    print(board[i][j], end=',')
    else:
        print('The Sudoku is not valid')
