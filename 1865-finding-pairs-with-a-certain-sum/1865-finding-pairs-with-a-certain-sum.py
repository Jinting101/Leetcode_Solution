class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.dic1 = {}
        self.dic2 = {}
        for x in nums1:
            self.dic1[x] = self.dic1.get(x, 0) + 1
        for x in nums2:
            self.dic2[x] = self.dic2.get(x, 0) + 1

    def add(self, index: int, val: int) -> None:
        prev = self.nums2[index]
        cur = prev + val
        self.nums2[index] = cur
        self.dic2[prev] -= 1
        if self.dic2[prev] == 0:
            self.dic2.pop(prev)
        self.dic2[cur] = self.dic2.get(cur, 0) + 1

    def count(self, tot: int) -> int:
        res = 0
        for x in self.dic1:
            comp = tot - x
            if comp in self.dic2:
                res += self.dic1[x] * self.dic2[comp]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
