import datetime

from numpy import isin

# Individual:
class Individual:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "%s" % (self.name)
    

# Meeting (Unscheduled Meetings will have null t):
class Meeting:

    def __init__(self, name, A, h, l, w, d, t):
        self.name = name
        self.A = A
        self.h = h
        self.l = l
        self.w = w
        self.d = d
        self.t = t

    def __repr__(self):
        out = "\n%s:\n(Attendees: [" % (self.name)
        for i in self.A:
            out+="%s," % (i)
        out = out[:-1] + "],\n"

        return out + "Host: %s,\nLength: %s,\nWeight: %s,\nDeadline: %s,\nStart Time: %s)\n" % (self.h, self.l, self.w, self.d, self.t)
    
    def __eq__(self, other):
        if (isinstance(other, Meeting)):
            return self.name == self.name and self.A == other.A and self.h == other.h and self.l == other.l and self.w == other.w and self.d == other.d and self.t == other.t
        return False
    
    def __hash__(self):
        return id(self)

# # Example:
# i1 = Individual("i1", [])
# i2 = Individual("i2", [])
# i3 = Individual("i3", [])
# i4 = Individual("i4", [])
# i5 = Individual("i5", [])

# # Scheduled Meetings:
# m1 = Meeting([i1,i3,i4,i5], i1, 1, 1.0, datetime.datetime(2021,12,10,18),  datetime.datetime(2021,12,10,9))
# m2 = Meeting([i1,i3,i4,i5], i3, 1, 1.0, datetime.datetime(2021,12,10,18),  datetime.datetime(2021,12,10,11))
# m3 = Meeting([i4,i5], i4, 2, 1.0, datetime.datetime(2021,12,10,18),  datetime.datetime(2021,12,10,16))

# # Unscheduled Meetings:
# m4 = Meeting([i1,i3,i5], i1, 1, 1.0, datetime.datetime(2021,12,10,18), None)
# m5 = Meeting([i1,i3,i4,i5], i5, 2, 1.0, datetime.datetime(2021,12,10,18), None)
# m6 = Meeting([i1,i2,i4], i2, 1, 1.0, datetime.datetime(2021,12,10,18), None)