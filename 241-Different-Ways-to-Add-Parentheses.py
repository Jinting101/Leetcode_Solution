class Solution(object):
    def diffWaysToCompute(self, expression, memo={}):
        \\\
        :type expression: str
        :rtype: List[int]
        \\\
        if expression.isdigit():
            return [int(expression)]
        if expression in memo:
            return memo[expression] 
        res = []
        for i in range(len(expression)):
            if expression[i] in \-+*\:
                res1 = self.diffWaysToCompute(expression[:i])
                res2 = self.diffWaysToCompute(expression[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, expression[i]))
        memo[expression] = res
        return res

    def helper(self, m, n, op):
        if op == \+\:
            return m+n
        elif op == \-\:
            return m-n
        else:
            return m*n
    