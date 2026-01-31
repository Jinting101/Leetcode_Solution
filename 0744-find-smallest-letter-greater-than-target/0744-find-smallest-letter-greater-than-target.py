class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = letters[0]
        for x in letters:
            if x > target:
                return x
        return res