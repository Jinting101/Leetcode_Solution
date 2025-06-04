class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        numFriends -= 1
        if numFriends == 0:
            return word
        cur, n = max(word), len(word)
        cur_indices = []
        for i,x in enumerate(word):
            if x == cur: cur_indices.append(i)
        curmax = ''
        for ind in cur_indices:
            endind = n-(numFriends-ind)
            curmax = max(curmax, word[ind:endind])
        return curmax