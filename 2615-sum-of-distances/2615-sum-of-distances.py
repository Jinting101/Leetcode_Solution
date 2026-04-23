class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dic = defaultdict(list)
        for i,x in enumerate(nums):
            dic[x].append(i)
        
        res = [0] * n
        
        for num, lst in dic.items():
            l = len(lst)
            if l == 1:
                continue
            ls = 0
            rs = sum(lst)
            for i,cur in enumerate(lst):
                rs -= cur
                curd = rs - cur*(l - 1 - i) + cur * i - ls
                res[lst[i]] = curd
                ls += cur

        return res