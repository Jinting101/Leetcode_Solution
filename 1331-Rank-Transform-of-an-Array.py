class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr2 = (sorted(set(arr)))
        rank_dict = {value: idx + 1 for idx, value in enumerate(arr2)}
        argsort = [rank_dict[num] for num in arr]
        return argsort
        