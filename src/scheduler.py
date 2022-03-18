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
