class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(box), len(box[0])
        res = [["."] * ROWS for _ in range(COLS)]
        for r in range(ROWS):
            i = COLS - 1
            for c in reversed(range(COLS)):
                if box[r][c] == "#":
                    res[i][ROWS - r - 1] = "#"
                    i -= 1
                elif box[r][c] == "*":
                    res[c][ROWS - r - 1] = "*"
                    i = c - 1
        return res

        m, n = len(box), len(box[0])
        res = [['.']*m for _ in range(n)]
        for r in range(m):
            stone = 0
            for c in range(n):
                if box[r][c] == '#':
                    stone += 1
                if box[r][c] == '*':
                    res[c][m-1-r] = '*'
                    if stone:
                        while stone > 0:
                            res[c-stone][m-1-r] = '#'
                            stone -= 1
                if stone and c == n-1:
                    while stone > 0:
                        res[c-stone+1][m-1-r] = '#'
                        stone -= 1
        return res
