class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        min_result = float('inf')
        row1_sum = sum(grid[0])
        row2_sum = 0
        
        for i in range(len(grid[0])):
            row1_sum -= grid[0][i]
            min_result = min(min_result, max(row1_sum, row2_sum))
            row2_sum += grid[1][i]
        
        return min_result

        # m, n = 2, len(grid[0])
        # directions = [(0, 1), (1, 0)]
        # visited = [[0]*n for i in range(m)]
        # best_path = []
        # max_reward = [0]
        # def dfs(r, c, cur_reward, cur_path):
        #     if not (0<=r<m and 0<=c<n and not visited[r][c]):
        #         return
        #     visited[r][c] = 1
        #     cur_path.append((r, c))
        #     cur_reward += grid[r][c]
        #     if r == m-1 and c == n-1 and cur_reward > max_reward[0]:
        #         max_reward[0] = cur_reward
        #         best_path[:] = cur_path[:]
        #     for x,y in directions:
        #         nr = r + x
        #         nc = c + y
        #         dfs(nr, nc, cur_reward, cur_path)
        #     visited[r][c] = 0
        #     cur_path.pop()
        # dfs(0, 0, 0, [])
        # for x,y in best_path:
        #     grid[x][y] = 0
        # visited = [[0]*n for i in range(m)]
        # best_path = []
        # max_reward = [0]
        # dfs(0, 0, 0, [])
        # return max_reward[0]