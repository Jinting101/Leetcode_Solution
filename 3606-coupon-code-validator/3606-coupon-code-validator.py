class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def validate_code(code):
            if not code:
                return False
            for x in code:
                if (not x.isalpha()) and (not x.isdigit()) and x != "_":
                    return False
            return True
        
        blines = ["electronics", "grocery", "pharmacy", "restaurant"]
        dic = {x:[] for x in blines}
        for i,c in enumerate(code):
            if validate_code(c) and isActive[i] and businessLine[i] in blines:
                dic[businessLine[i]].append(c)
        
        res = []
        for cat in dic:
            if not dic[cat]:
                continue
            lst = sorted(dic[cat])
            res.extend(lst)
        return res