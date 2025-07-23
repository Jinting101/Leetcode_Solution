class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        low, high = 'ba', 'ab'
        if x < y:
            x, y = y, x
            low, high = high, low

        # First pass: remove high-value pairs
        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= 2 and stack[-2] + stack[-1] == high:
                res += x
                stack.pop()
                stack.pop()

        # Second pass: remove low-value pairs from remaining string
        new_stack = []
        for ch in stack:
            new_stack.append(ch)
            if len(new_stack) >= 2 and new_stack[-2] + new_stack[-1] == low:
                res += y
                new_stack.pop()
                new_stack.pop()
                
        return res