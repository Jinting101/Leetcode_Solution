import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Max heap to always pick the character with the highest count.
        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, 'a'))
        if b > 0:
            heapq.heappush(pq, (-b, 'b'))
        if c > 0:
            heapq.heappush(pq, (-c, 'c'))

        result = []

        while pq:
            count1, char1 = heapq.heappop(pq)

            # If the last two characters are the same as char1.
            if len(result) >= 2 and result[-1] == char1 and result[-2] == char1:
                if not pq:
                    break  # No valid characters left to pick.

                count2, char2 = heapq.heappop(pq)
                result.append(char2)
                count2 += 1  # Decrease count (negated)

                if count2 < 0:
                    heapq.heappush(pq, (count2, char2))

                heapq.heappush(pq, (count1, char1))
            else:
                result.append(char1)
                count1 += 1  # Decrease count (negated)

                if count1 < 0:
                    heapq.heappush(pq, (count1, char1))

        return ''.join(result)


# Greedy Strategy: Always try to use the character with the highest remaining count. If that character has been used twice consecutively, switch to the next most frequent character.
# Priority Queue: Use a max-heap (or priority queue) to keep track of the character counts. This ensures that at every step, we can easily pick the character with the highest remaining count.
# Condition Handling: If the character with the highest count has been used twice in a row, we temporarily switch to the second-highest character to avoid three consecutive characters.
# Stop When No Characters Left: The process stops when no more characters can be added without violating the conditions.