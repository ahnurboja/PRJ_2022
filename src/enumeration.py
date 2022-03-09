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
    
    def getSolution(self):

        S = []

        for m in self.M:
            # print('\n\n\nChecking for Meeting m :\n',m,'\n\n')
            m.t = self.now
            allClashes = False
            for s in S:
                allClashes = True
                # print('\tcurrent start time of m = ',m.t)
                # print('\tchecking for clash with s:\n\t',s)
                if self.clash(m,s):
                    # print('\t\tCLASH!')
                    m.t = s.t+timedelta(hours=s.l)
                else:
                    allClashes = False
            if not allClashes or m.t+timedelta(hours=m.l) <= m.d:
                # print('adding to S')
                S.append(m)
        
        # print(S)
                
        return S
    
# # Example:
# i1 = Individual("i1", [])
# i2 = Individual("i2", [])
# i3 = Individual("i3", [])
# i4 = Individual("i4", [])
# i5 = Individual("i5", [])
# i6 = Individual("i6", [])
# i7 = Individual("i7", [])
# i8 = Individual("i8", [])
# i9 = Individual("i9", [])
# i10 = Individual("i10", [])

# # Scheduled Meetings:
# m1 = Meeting([i1,i3,i4,i5], i1, 1, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,9))
# m2 = Meeting([i1,i3,i4,i5], i3, 1, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,11))
# m3 = Meeting([i4,i5], i4, 2, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,16))


# # Unscheduled Meetings:
# m4 = Meeting([i1,i3,i5], i1, 1, 0.3, datetime(2021,12,10,18), None)
# m5 = Meeting([i1,i3,i4,i5,i6], i5, 2, 0.5, datetime(2021,12,10,10), None)
# m6 = Meeting([i1,i2,i4], i2, 1, 0.99, datetime(2021,12,10,23), None)
# m7 = Meeting([i1,i3,i5,i10], i1, 1, 0.2, datetime(2021,12,10,15), None)
# m8 = Meeting([i1,i3,i4,i5,i9], i5, 2, 0.6, datetime(2021,12,10,18), None)
# m9 = Meeting([i1,i7,i4,i8], i2, 1, 0.8, datetime(2021,12,10,16), None)

# I = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10]
# M = [m4,m5,m6,m7,m8,m9]

# algorithm = EnumerationAlgorithm(I, M)
# print(algorithm.getSolution())
# result = algorithm.run(10)
# print(result)
# print(algorithm.getCost(result[0]))