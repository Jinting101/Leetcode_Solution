class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        def check(a, b):
            return sorted(str(a)) == sorted(str(b))

        l = len(str(n))
        for i in range(31):
            curl = len(str(2**i))
            if curl == l and check(n, 2**i):
                return True
            elif curl > l:
                return False
        return False
