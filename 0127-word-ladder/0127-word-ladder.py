class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        def check(x, y):
            dif = 0
            for i, cur in enumerate(x):
                if cur == y[i]:
                    continue
                dif += 1
                if dif > 1:
                    return
            adj[x].append(y)
            adj[y].append(x)

        adj = defaultdict(list)
        n = len(wordList)
        for i in range(n):
            for j in range(i+1, n):
                x, y = wordList[i], wordList[j]
                check(x, y)
        
        if beginWord not in wordList:
            for x in wordList:
                check(beginWord, x)
        
        q = deque([(beginWord, [])])
        visited = set([beginWord])
        res = 0
        while q:
            res += 1
            l = len(q)
            for i in range(l):
                cur, path = q.popleft()
                if cur == endWord:
                    return res
                for nei in adj[cur]:
                    if nei not in visited:
                        q.append((nei, path + [nei]))
                        visited.add(nei)  
        return 0
        
        q = deque([beginWord])
        visited = set([beginWord])
        res = 0
        print(adj)
        while q:
            l = len(q)
            for i in range(l):
                cur = q.popleft()
                if cur == endWord:
                    return res
                for nei in adj[cur]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            res += 1
        return 0
