class MyCalendarTwo(object):

    def __init__(self):
        self.calendar = []
        self.overlaps = []

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

        for i,j in self.overlaps:
            if start < j and end > i:
                return False # Found a pre-existing overlap

        for i,j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start,i), min(end,j)))
        self.calendar.append((start,end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)