class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
            
        adj = defaultdict(list)
        n = len(wordList)

        def transform(x, y):
            dif = 0
            for a,b in zip(x, y):
                if a != b:
                    dif += 1
                    if dif > 1:
                        return False
            adj[x].append(y)
            adj[y].append(x)
        
        for i in range(n):
            for j in range(i+1, n):
                transform(wordList[i], wordList[j])
        
        if beginWord not in wordList:
            for x in wordList:
                transform(beginWord, x)

        res = 1
        q = deque([beginWord])
        visited = set()
        visited.add(beginWord)

        while q:
            l = len(q)
            for _ in range(l):
                word = q.popleft()
                if word == endWord:
                    return res
                for nei in adj[word]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            res += 1
        
        return 0
