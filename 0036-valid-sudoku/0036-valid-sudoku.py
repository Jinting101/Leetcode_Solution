class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_line(board):
            for row in board:
                cur = [int(x) for x in row if x != '.']
                if len(cur) != len(set(cur)):
                    return False
            return True
        
        cols = [[row[i] for row in board] for i in range(9)]
        if not check_line(board) or not check_line(cols):
            return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                curb = board[i:i+3]
                cur = [row[j:j+3] for row in curb]
                curs = [x for row in cur for x in row if x != '.' ]
                if len(curs) != len(set(curs)):
                    return False
        return True