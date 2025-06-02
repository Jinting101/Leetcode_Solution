class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        l, r = min(ratings), max(ratings)
        dic = {i:[] for i in range(l, r+1)}
        res = [0]*(n+1)
        for i,x in enumerate(ratings):
            dic[x].append(i)
        for cur_rating in dic:
            for ind in dic[cur_rating]:
                if cur_rating == l:
                    res[ind] = 1
                elif ind == 0:
                    if ratings[ind] <= ratings[ind+1]:
                        res[ind] = 1
                    else:
                        res[ind] = res[ind+1] + 1
                elif ind == n-1:
                    if ratings[ind] <= ratings[ind-1]:
                        res[ind] = 1
                    else:
                        res[ind] = res[ind-1] + 1
                else:
                    if ratings[ind] > ratings[ind-1] and ratings[ind] > ratings[ind+1]:
                        res[ind] = max(res[ind-1], res[ind+1]) + 1
                    elif ratings[ind] > ratings[ind-1]:
                        res[ind] = res[ind-1] + 1
                    elif ratings[ind] > ratings[ind+1]:
                        res[ind] = res[ind+1] + 1
                    else:
                        res[ind] = 1
        return sum(res)

