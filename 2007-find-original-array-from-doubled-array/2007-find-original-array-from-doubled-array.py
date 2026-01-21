class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 == 1:
            return []
        changed.sort()
        dic = {}
        for x in changed:
            dic[x] = dic.get(x, 0) + 1
        
        res = []
        
        for x in dic:
            if dic[x] == 0:
                continue
            while dic[x] > 0:
                if 2*x not in dic or dic[2*x] < dic[x]:
                    return []
                res.append(x)
                dic[2*x] -= 1
                dic[x] -= 1
        return res
        
        


        # 1 2 3 4 2 4 6 8

        # 1 2 2 3 4 4 6 8

        # 1 1 2 2 2 2 4 4