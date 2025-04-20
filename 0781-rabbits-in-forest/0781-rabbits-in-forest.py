class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        dic = {}
        for x in answers:
            dic[x] = dic.get(x, 0) + 1
        res = 0
        for x in dic:
            y = dic[x]
            curmin = x + 1
            res += (y // curmin) * curmin
            if y % curmin != 0:
                res += curmin
        return res