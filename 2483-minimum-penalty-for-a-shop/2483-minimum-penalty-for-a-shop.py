class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        res = 0
        score = customers.count("Y")
        minscore = score
        for i in range(1, n+1):
            p = customers[i-1]
            if p == "Y":
                score -= 1
            if p == "N":
                score += 1
            if score < minscore:
                res = i
                minscore = score
        return res
