class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = {chr(x):[0]*rows for x in range(ord('A'), ord('Z')+1)}

    def setCell(self, cell: str, value: int) -> None:
        self.grid[cell[0]][int(cell[1:])-1] = value

    def resetCell(self, cell: str) -> None:
        self.grid[cell[0]][int(cell[1:])-1] = 0

    def getValue(self, formula: str) -> int:
        res = 0
        a, b = formula[1:].split('+')
        if a.isdigit():
            res += int(a)
        else:
            res += self.grid[a[0]][int(a[1:])-1]
        if b.isdigit():
            res += int(b)
        else:
            res += self.grid[b[0]][int(b[1:])-1]
        return res



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)