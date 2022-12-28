'''class Solution:
    def Sudoku(self, board):
        row = [set() for i in range(9)]
        col = [set() for j in range(9)]
        block = [[set() for i in range(3)] for j in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in block[i // 3][j // 3]:
                        print('The row',i+1,' and column',j+1," occur error")
                        return False
                    else:
                        row[i].add(board[i][j])
                        col[j].add(board[i][j])
                        block[i // 3][j // 3].add(board[i][j])

        def dfs(i,j): #solving the sakudo
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
                    if candi not in row[i] and candi not in col[j] and candi not in block[i//3][j//3]:
                        board[i][j] = candi
                        row[i].add(candi)
                        col[j].add(candi)
                        block[i//3][j//3].add(candi)
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
                        block[i//3][j//3].remove(candi)
        self.flag = False
        dfs(0,0)
        return True

if __name__ == '__main__':
    S = Solution()
    board = [5, 5, 0, 0, 7, 0, 0, 0, 0], \
            [6, 0, 0, 1, 9, 5, 0, 0, 0], \
            [0, 9, 8, 0, 0, 0, 0, 6, 0], \
            [8, 0, 0, 0, 6, 0, 0, 0, 3], \
            [4, 0, 0, 8, 0, 3, 0, 0, 1], \
            [7, 0, 0, 0, 2, 0, 0, 0, 6], \
            [0, 6, 0, 0, 0, 0, 2, 8, 0], \
            [0, 0, 0, 4, 1, 9, 0, 0, 5], \
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
    S.Sudoku(board)
    if S.Sudoku(board):
        print('The Sakudo is valid')
        print(board)
    else:
        print('The Sakudo is NOT valid')'''

# a = 2 // 3
#
# print(a)



data = [4,5,6,7,0,1,2]
val = 0
def try1(nums,target):
    if len(nums) == 0:
        return -1
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[l]:
            if nums[l] <= target <= nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] <= target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1

result = try1(data,val)
print(result)