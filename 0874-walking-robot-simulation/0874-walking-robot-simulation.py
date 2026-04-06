class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set()
        for ob in obstacles:
            obs.add(tuple(ob))
        res = 0
        d = [0, 1]
        x, y = 0, 0
        for i, c in enumerate(commands):
            if c == -1:
                d[0], d[1] = d[1], -d[0]
            elif c == -2:
                d[0], d[1] = -d[1], d[0]
            else:
                for _ in range(c):
                    x += d[0]
                    y += d[1]
                    if (x,y) in obs:
                        x -= d[0]
                        y -= d[1]
                        break
                res = max(res, x**2 + y**2)
        return res