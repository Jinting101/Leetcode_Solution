class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        buildings.sort()
        row_pts = {}
        col_pts = {}
        for c, r in buildings:
            if c not in col_pts:
                col_pts[c] = []
            col_pts[c].append((c, r))
            if r not in row_pts:
                row_pts[r] = []
            row_pts[r].append((c, r))
        set_rows = set()
        for r,lst in row_pts.items():
            if len(lst) <= 2:
                continue
            for pt in lst[1:-1]:
                set_rows.add(pt)
        set_cols = set()
        for c,lst in col_pts.items():
            if len(lst) <= 2:
                continue
            for pt in lst[1:-1]:
                set_cols.add(pt)
        return len(set_rows.intersection(set_cols))
            