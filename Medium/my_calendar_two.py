class MyCalendarTwo:

    def __init__(self):
        self.forest = {} # forest of trees

    def overlap(self, start: int, end: int, startOver: int, endOver: int) -> bool:
        if start >= startOver and start < endOver:
            return True
        if end > startOver and end <= endOver:
            return True
        if start <= startOver and end >= endOver:
            return True
        return False

    def book(self, start: int, end: int) -> bool:
        for (s, e) in self.forest.keys():
            if start >= s and end < e:
                for child_start, child_end in self.forest[(s,e)]:
                    if self.overlap(start, end, child_start, child_end):
                        return False
                self.forest([s, e]).append([start, end])
        
            if start < s and end < e:
                roots = self.forest.values().sort()
                
        
        if (start, end) not in self.forest:
            self.forest[(start, end)] = []
            
                    





# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)