class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = [None] * 26

class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        # prefix_counts = {}
        # for word in words:
        #     prefix = ""
        #     for char in word:
        #         prefix += char
        #         prefix_counts[prefix] = prefix_counts.get(prefix, 0) + 1
        
        # result = [0] * len(words)
        # for i, word in enumerate(words):
        #     prefix = ""
        #     for char in word:
        #         prefix += char
        #         result[i] += prefix_counts[prefix]
        
        # return result

        root = TrieNode()

        for w in words:
            node = root
            for ch in w:
                index = ord(ch) - ord('a')
                if not node.children[index]:
                    node.children[index] = TrieNode()
                node = node.children[index]
                node.count += 1

        ans = []
        for w in words:
            sum = 0
            node = root
            for ch in w:
                index = ord(ch) - ord('a')
                node = node.children[index]
                sum += node.count
            ans.append(sum)
        return ans