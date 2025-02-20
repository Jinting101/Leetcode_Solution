class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def change(x, s, t):
            temp = list(x)
            for i in range(s, t+1):
                temp[i] = '0' if x[i] == '1' else '1'
            return ''.join(temp)
        
        lst = set(nums)
        l = len(nums[0])
        for x in nums:
            for i in range(l):
                for j in range(i, l):
                    temp = change(x, i, j)
                    if temp not in lst:
                        return temp
        
        return -1
