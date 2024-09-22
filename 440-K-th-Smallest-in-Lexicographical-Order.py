class Solution(object):
    def findKthNumber(self, n, k):
        \\\
        :type n: int
        :type k: int
        :rtype: int
        \\\
        cur = 1
        k -= 1
        while k > 0:
            steps = self.getSteps(n, cur, cur+1)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
                
        return cur

    def getSteps(self, n, n1, n2):
        steps = 0
        while n1 <= n:
            steps += min(n+1, n2) - n1
            n1 *= 10
            n2 *= 10
        return steps


# Define a function named \findKthNumber\ that takes in two parameters: \n\ and \k\. This function will return an integer, which is the kth lexicographically smallest integer in the range [1, n].

# Initialize a variable \cur\ to 1. This variable will keep track of the current number being considered.

# Decrement \k\ by 1, since the variable \cur\ has already been initialized to 1.

# Start a while loop that will continue until k is equal to 0. This loop will be used to find the kth lexicographically smallest number.

# Within the while loop, call the function \getSteps\ with three arguments: \n\, \cur\, and \cur+1\. This function will return the number of steps required to go from \cur\ to \cur+1\ while staying within the range of [1, n].

# If the number of steps required to go from \cur\ to \cur+1\ is less than or equal to k, increment \cur\ by 1 and decrement \k\ by the number of steps required to go from \cur\ to \cur+1\.

# If the number of steps required to go from \cur\ to \cur+1\ is greater than k, multiply \cur\ by 10 and decrement \k\ by 1.

# Once the while loop has terminated, return \cur\, which is the kth lexicographically smallest integer in the range [1, n].

# Define another function named \getSteps\ that takes in three parameters: \n\, \n1\, and \n2\. This function will return the number of steps required to go from \n1\ to \n2\ while staying within the range of [1, n].

# Initialize a variable \steps\ to 0. This variable will keep track of the number of steps required to go from \n1\ to \n2\.

# Start a while loop that will continue until \n1\ is greater than \n\. This loop will be used to count the number of steps required to go from \n1\ to \n2\.

# Within the while loop, add the minimum value between \n+1\ and \n2\ to \steps\ and subtract \n1\ from \n2\. This will give us the number of steps required to go from \n1\ to \n2\ while staying within the range of [1, n].

# Multiply \n1\ and \n2\ by 10 to get the next set of numbers to consider.

# Once the while loop has terminated, return \steps\, which is the number of steps required to go from \n1\ to \n2\ while staying within the range of [1, n].