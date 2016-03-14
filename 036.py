class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        dict1 = []
        dict2 = []
        dict3 = []
        for i in range(0,9):
            dict1.append({})
            dict2.append({})
            dict3.append({})
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] != ".":
                    if board[i][j] not in dict1[i]:
                        dict1[i][board[i][j]] = 0
                    else:
                        return False
                    if board[i][j] not in dict2[j]:
                        dict2[j][board[i][j]] = 0
                    else:
                        return False
                    part = i//3*3+j//3
                    if board[i][j] not in dict3[part]:
                        dict3[part][board[i][j]] = 0
                    else:
                        return False
        return True
        