class Solution(object):
    def lexicalOrder(self, n):
        \\\
        :type n: int
        :rtype: List[int]
        \\\

        # return sorted(range(1, n+1), key = lambda x : str(x))


        # lexical_order_list = []
        # def recursive_adder(x, n):
        #     if x > n:
        #         return
        #     lexical_order_list.append(x)
        #     prefix = x * 10
        #     for i in range(10):
        #         recursive_adder(prefix + i, n)
        # for i in range(1, 10):
        #     recursive_adder(i, n)
        # return lexical_order_list

        res = []
        cur = 1
        for i in range(n):
            # Add the current number to the result
            res.append(cur)
            # If the current number times 10 is less than or equal to n, move to the next level
            if cur * 10 <= n:
                cur *= 10
            # Otherwise, move to the next number at the current level
            else:
                # If we've reached the end of a level, divide by 10 to go back up one level
                if cur >= n:
                    cur //= 10
                cur += 1
                # Skip over any trailing zeroes (e.g. if cur = 19, skip over 190, 191, 192, etc.)
                while cur % 10 == 0:
                    cur //= 10
        return res