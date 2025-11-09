class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        cnt = [0]
        lst = [max(num1, num2), min(num1, num2)]
        def opera(lst):
            cnt[0] += 1
            lst[0] -= lst[1]
            lst[0], lst[1] = max(lst), min(lst)
            
        while lst[0] != 0 and lst[1] != 0:
            opera(lst)

        return cnt[0]