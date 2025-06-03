class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        opened = set()
        res = 0
        q = deque(initialBoxes)
        box_access = [0] * len(status)
        while q:
            box = q.popleft()
            box_access[box] = 1
            if box not in opened and status[box]:
                opened.add(box)
                res += candies[box]
                for key in keys[box]:
                    status[key] = 1
                    if key not in opened and box_access[key]:
                        q.append(key)
                for nei_box in containedBoxes[box]:
                    if nei_box not in opened:
                        q.append(nei_box)
                        box_access[box] = 1
        return res