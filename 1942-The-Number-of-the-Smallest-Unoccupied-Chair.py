import heapq
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        order = sorted(range(len(times)), key = lambda x: times[x][0])  # <-- 1)
        emptySeats, takenSeats = list(range(len(times))), []            # <-- 2)

        for i in order:                                                 # <-- 3)
            ar, lv = times[i]

            while takenSeats and takenSeats[0][0] <= ar:  # Free chairs that are vacated before the current arrival time
                heapq.heappush(emptySeats, heappop(takenSeats)[1])
            seat = heapq.heappop(emptySeats)                                # Assign the smallest available chair

            if i == targetFriend: return seat       # If this is the target friend, return their chair number

            heapq.heappush(takenSeats,(lv, seat))      # Mark the chair as being used until the friend's leave time
        return -1  # Should never reach here

# We sort friends by their arrival times.
# We initialize available seats and taken seats as heaps.
# We track freed seats that become available.
# We assign the smallest available seat to the next friend, and we check whether that friend is the target.
# We add the current seat to takenSeats with the departure time.