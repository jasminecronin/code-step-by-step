class Date:
    month = 0
    day = 0
    
    def __init__(self, m, d):
        self.month = m
        self.day = d
        
    def days_in_month(self):
        if self.month == 2:
            return 28
        elif self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
            return 30
        else:
            return 31
        
    def get_day(self):
        return self.day
    
    def get_month(self):
        return self.month
    
    def next_day(self):
        self.day += 1
        if self.day > self.days_in_month():
            self.day = 1
            self.month += 1
            if self.month == 13:
                self.month = 1
                
    def __str__(self):
        return "{:02d}/{:02d}".format(self.month, self.day)
