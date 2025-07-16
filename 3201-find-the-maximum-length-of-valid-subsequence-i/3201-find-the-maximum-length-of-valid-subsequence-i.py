class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd, even, oddeven, evenodd = [], [], [], []
        for x in nums:
            if x % 2 == 1:
                odd.append(x)
                if not oddeven or (oddeven and oddeven[-1] % 2 == 0):
                    oddeven.append(x)
                if evenodd and evenodd[-1] % 2 == 0:
                    evenodd.append(x)
            else:
                even.append(x)
                if oddeven and oddeven[-1] % 2 == 1:
                    oddeven.append(x)
                if not evenodd or (evenodd and evenodd[-1] % 2 == 1):
                    evenodd.append(x)
        return max(len(odd), len(even), len(oddeven), len(evenodd))