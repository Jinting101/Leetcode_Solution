class MyCalendar(object):

    def __init__(self):
        self.events = []
        
    def book(self, start, end):
        \\\
        :type start: int
        :type end: int
        :rtype: bool
        \\\

        # sorted
        # l = len(self.all_bookings)
        # if l == 0:
        #     self.all_bookings.append([start, end])
        #     return True
        # for i, cur_booking in enumerate(self.all_bookings):
        #     if i < l-1 and start >= cur_booking[1] and end <= self.all_bookings[i+1][0]:
        #         self.all_bookings = self.all_bookings[:i+1] + [[start, end]] + self.all_bookings[i+1:]
        #         return True
        #     elif i == l-1 and start >= cur_booking[1]:
        #         self.all_bookings.append([start, end])
        #         return True
        #     elif i == 0 and end <= cur_booking[0]:
        #         self.all_bookings = [[start, end]] + self.all_bookings
        #         return True
        # return False

        # not sorted
        for s, e in self.events:
            # If the new event overlaps with any existing event
            if not (end <= s or start >= e):  # No overlap condition: (new_end <= old_start) or (new_start >= old_end)
                return False
        # If no overlap, add the event
        self.events.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)