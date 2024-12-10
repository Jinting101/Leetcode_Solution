class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)  # Use a set for quick lookups
        total_sum = 0  # Track the cumulative sum
        count = 0  # Track the count of valid numbers

        for i in range(1, n + 1):
            if i in banned_set:
                continue  # Skip banned numbers
            total_sum += i
            if total_sum > maxSum:
                break  # Stop if the sum exceeds maxSum
            count += 1

        return count

        
        banned = set(banned)
        cur, res = 0, 0
        avail = [i for i in range(1, n+1)][::-1]
        while avail and cur + avail[-1] <= maxSum:
            if avail[-1] in banned:
                avail.pop()
                continue
            cur += avail.pop()
            res += 1
        return res