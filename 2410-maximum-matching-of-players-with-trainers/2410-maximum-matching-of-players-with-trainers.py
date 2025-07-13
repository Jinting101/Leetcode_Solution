class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        res = 0
        j, n = 0, len(trainers)
        for x in players:
            while j < n and x > trainers[j]:
                j += 1
            if j < n and x <= trainers[j]:
                res += 1
                j += 1
            if j >= n:
                break
        return res
