class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visit = [[False for i in xrange(len(board[0]))] for j in xrange(len(board))]
        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                if word[0] == board[i][j]:
                    if self.expand(board,visit,i,j,word):
                        return True
        return False
    def expand(self,board,visit,i,j,word):
        if len(word) == 1 and board[i][j] == word:
            return True
        if word[0] == board[i][j]:
            visit[i][j] = True
            up = down = left = right = False
            if i > 0 and visit[i-1][j] == False:
                up = self.expand(board,visit,i-1,j,word[1:])
            if i < len(board)-1 and visit[i+1][j] == False:
                down = self.expand(board,visit,i+1,j,word[1:])
            if j > 0 and visit[i][j-1] == False:
                left = self.expand(board,visit,i,j-1,word[1:])
            if j < len(board[0])-1 and visit[i][j+1] == False:
                right = self.expand(board,visit,i,j+1,word[1:])
            if up or down or right or left:
                return True
            else:
                visit[i][j] = False
                return False
        else:
            return False
        