class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1, lst2 = version1.split('.'), version2.split('.')
        while len(lst1) < len(lst2):
            lst1.append('0')
        while len(lst2) < len(lst1):
            lst2.append('0')
        for x,y in zip(lst1, lst2):
            x, y = int(x), int(y)
            if x < y:
                return -1
            if x > y:
                return 1
        return 0
        