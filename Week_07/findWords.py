dx=[-1,1,0,0]
dy=[0,0,-1,1]
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []
        if not words:
            return []
        self.result = set()
        root = {}
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char,{})
            node['#'] = '#'
        self.m,self.n = len(board),len(board[0])
        for i in xrange(self.m):
            for j in xrange(self.n):
                if board[i][j] in root:
                    self.dfs(board, i, j, "", root)
        return list(self.result)
    def dfs(self,board,i,j,current_word,current_dict):
            current_word += board[i][j]
            current_dict = current_dict[board[i][j]]
            if '#' in current_dict:
                self.result.add(current_word)
            tmp,board[i][j] = board[i][j],'@'
            for k in range(4):
                x,y = i + dx[k],j + dy[k]
                if 0<=x<self.m and 0<=y<self.n and board[x][y] != '@' and board[x][y] in current_dict:
                    self.dfs(board,x,y,current_word,current_dict)
            board[i][j] = tmp