class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        cum = [0] * n
        ans = []

        for i in range(1, n):
            cum[i] = cum[i - 1]
            if nums[i] % 2 == nums[i - 1] % 2:
                cum[i] += 1

        for q in queries:
            x, y = q
            falseCount = cum[y] - cum[x]
            ans.append(falseCount==0)

        return ans


        
        res = []
        for st, ed in queries:
            if st==ed:
                res.append(True)
            else:
                temp = True
                for i in range(st, ed):
                    if nums[i] % 2 == nums[i+1] % 2:
                        temp = False
                        break
                res.append(temp)
        return res