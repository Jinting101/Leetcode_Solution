class Solution(object):
    def diffWaysToCompute(self, expression, memo={}):
        \\\
        Returns all possible results of computing the expression 
        by splitting it at each operator.

        :type expression: str
        :rtype: List[int]
        \\\
        # Base case: expression is a number
        if expression.isdigit():
            return [int(expression)]

        # Memoization
        if expression in memo:
            return memo[expression]

        results = []
        for i, char in enumerate(expression):
            # Check if character is an operator
            if char in \-+*\:
                # Recursively compute left and right expressions
                left_results = self.diffWaysToCompute(expression[:i], memo)
                right_results = self.diffWaysToCompute(expression[i+1:], memo)

                # Combine results using the operator
                for left in left_results:
                    for right in right_results:
                        results.append(self.compute(left, right, char))

        # Store results in memo
        memo[expression] = results
        return results

    def compute(self, m, n, op):
        \\\
        Helper function to compute the result of two numbers 
        with the given operator.

        :type m: int
        :type n: int
        :type op: str
        :rtype: int
        \\\
        if op == \+\:
            return m + n
        elif op == \-\:
            return m - n
        else:
            return m * n