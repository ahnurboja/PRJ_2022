from scheduler import *
from datetime import datetime, timedelta

class EnumerationAlgorithm:

    I = [] # Set of individuals
    M = [] # Set of meetings to be scheduled
    # now = datetime.now().replace(microsecond=0, second=0, minute=0)
    now = datetime(2021,12,10,5)
    totalWeights = 0 # Total weights of the unscheduled meetings

    def __init__(self, I, M):
        self.I = I
        self.M = M
    
    def perdelta(self, start, end, delta):
        curr = start
        while curr < end:
            yield curr
            curr += delta
    
    def clash(self, m1, m2):
        return max(m1.t,m2.t) < min(m1.t+timedelta(hours=m1.l),m2.t+timedelta(hours=m2.l)) and len(set(m1.A).intersection(m2.A)) > 0
    
    def run(self):
        S = []
        for m in self.M:
            m.t = self.now
            allClashes = False
            for s in S:
                allClashes = True
                if self.clash(m,s):
                    m.t = s.t+timedelta(hours=s.l)
                else:
                    allClashes = False
            if not allClashes or m.t+timedelta(hours=m.l) <= m.d:
                S.append(m)
        return (S, 1)