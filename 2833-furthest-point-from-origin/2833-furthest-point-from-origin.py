class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l, r = moves.count('L'), moves.count('R')
        return len(moves) - l - r + abs(l-r)