import heapq
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

# Sort the intervals by their start times to process them in chronological order.
# Use a priority queue (min-heap) to track the end times of the intervals. The heap will help us manage the intervals that are currently active.
# If the start time of the new interval is greater than the earliest end time in the heap, this means the interval can be placed in an existing group. So, we remove the top of the heap and replace it with the new interval's end time.
# If the start time of the interval is earlier than all end times in the heap, it means we need a new group, and we add the new end time to the heap.
# At the end of processing all intervals, the size of the heap represents the number of groups needed, as each element in the heap corresponds to an active group.


        intervals.sort()
        pq = []
        for start, end in intervals:
            if pq and pq[0] < start:
                heapq.heappop(pq)
            heapq.heappush(pq, end)
        return len(pq)

        # start_times = sorted(i[0] for i in intervals)
        # end_times = sorted(i[1] for i in intervals)
        # end_ptr, group_count = 0, 0
        # for start in start_times:
        #     if start > end_times[end_ptr]:
        #         end_ptr += 1
        #     else:
        #         group_count += 1

        # return group_count

# We need to group intervals so that no intervals in the same group overlap. By sorting start and end times, we can track how many intervals overlap at any point. If a new interval starts after an earlier one ends, we can reuse that group. Otherwise, we need a new group.

# Sort start and end times: Sorting helps track when intervals start and end.

# Two pointers:
# start_ptr iterates through start times.
# end_ptr tracks the earliest end time. If the current interval starts after the earliest end, reuse a group by incrementing end_ptr; otherwise, create a new group.

# Result: The number of active groups after processing all intervals is the minimum number of groups required.

# If we look at two intervals, say [2, 3] and [1, 5], and you draw them on a number line, you'll notice that it makes no difference if you swap them to [1, 3] and [2, 5], because they only overlap between [2, 3], while they're separate in the intervals [1, 2) and (3, 5].