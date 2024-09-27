class MyCalendarTwo(object):

    def __init__(self):
        self.calendar = []  # Stores single booked intervals
        self.overlaps = []  # Stores double booked intervals

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # l = len(self.calendar)
        # for i, booking in enumerate(self.calendar):
        #     if not (end <= booking[0] or start >= booking[1]):
        #         dbtime = [max(start, booking[0]), min(end, booking[1])]
        #         for j in range(i+1, l):
        #             booking2 = self.calendar[j]
        #             if not (dbtime[1] <= booking2[0] or dbtime[0] >= booking2[1]):
        #                 return False
        # self.calendar.append([start, end])
        # return True


        # Check if the event overlaps with any double booking, which would cause a triple booking
        for s,e in self.overlaps:
            if start < e and end > s:
                return False # Found a pre-existing overlap; # Triple booking found
        
        # Add the overlapping parts to double bookings
        for s,e in self.calendar:
            if start < e and end > s:
            # if max(start, s) < min(end, e):
                self.overlaps.append((max(start,s), min(end,e)))
        self.calendar.append((start,end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)