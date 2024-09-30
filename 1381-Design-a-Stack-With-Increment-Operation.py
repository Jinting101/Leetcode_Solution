class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.s=[None]*maxSize
        self.top=-1
        self.size=maxSize

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.top+1==self.size:
            return
        self.top+=1
        self.s[self.top]=x

    def pop(self):
        """
        :rtype: int
        """
        if self.top==-1:
            return -1
        val=self.s[self.top]
        self.top-=1
        return val

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if self.top==-1:
            return
        t=self.top
        for i in range(min(self.top+1, k)):
            self.s[i]=self.s[i]+val

# class CustomStack:

#     def __init__(self, maxSize: int):
#         self.stack = []
#         self.maxSize = maxSize
#         self.inc = []

#     def push(self, x: int) -> None:
#         if len(self.stack) == self.maxSize:
#             return
#         self.stack.append(x)
#         self.inc.append(0)

#     def pop(self) -> int:
#         if not self.stack:
#             return -1
#         if len(self.inc) > 1:
#             self.inc[-2] += self.inc[-1]
#         return self.stack.pop() + self.inc.pop()

#     def increment(self, k: int, val: int) -> None:
#         if self.stack:
#             self.inc[min(k, len(self.stack)) - 1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)