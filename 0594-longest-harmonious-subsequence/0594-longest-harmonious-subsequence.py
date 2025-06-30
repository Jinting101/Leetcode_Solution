class Solution:
    def findLHS(self, nums: List[int]) -> int:
        frequency_map = Counter(nums)
        max_length = 0

        for num in frequency_map:
            if num + 1 in frequency_map:
                current_length = frequency_map[num] + frequency_map[num + 1]
                max_length = max(max_length, current_length)

        return max_length


        
        nums.sort()
        dic = {}
        res = 0
        for i,x in enumerate(nums):
            if x not in dic:
                dic[x] = []
            elif len(dic[x]) > 1:
                dic[x].pop()
            dic[x].append(i)
        keys = list(dic.keys())
        for i in range(1, len(keys)):
            cur, prev = keys[i], keys[i-1]
            if cur - prev == 1:
                res = max(res, dic[cur][-1] - dic[prev][0] + 1)
        return res

