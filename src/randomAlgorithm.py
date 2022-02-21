# Input: individuals, unscheduledMeetings
# Output: inputListOfMeetings, numberOfSolutionsSearched

from scheduler import *
import sys
import random
from datetime import datetime, timedelta
from faker import Faker
fake = Faker()
import itertools


class RandomAlgorithm:

    counter = 0 # Counter for number of solutions searched.
    I = [] # Set of individuals
    M = [] # Set of meetings to be scheduled
    # now = datetime.now().replace(microsecond=0, second=0, minute=0)
    now = datetime(2021,12,10,5)
    totalWeights = 0 # Total weights of the unscheduled meetings

    def __init__(self, I, M):
        self.I = I
        self.M = M

    def pickRandomSolution(self):

        # For each meeting in M, apply a random start time
        S = []
        for m in self.M:
            maxStartDate = m.d - timedelta(hours=m.l)
            m.t = fake.date_time_between(start_date=self.now, end_date=maxStartDate).replace(microsecond=0, second=0, minute=0)
            S.append(m)

        return S

    # remove overlaps in set (greedy)
    def removeOverlaps(self, S):
        newS = set()
        for i in range(len(S)-1):
            m1 = S[i]
            for j in range(i+1, len(S)):
                m2 = S[j]
                if max(m1.t,m2.t) < min(m1.t+timedelta(hours=m1.l),m2.t+timedelta(hours=m2.l)) and len(set(m1.A).intersection(m2.A)) > 0:
                    # if there is an overlap: remove the lowest priority
                    if m1.w > m2.w:
                        newS.add(m1)
                    else:
                        newS.add(m2)
        return newS
    
    # calculate cost of solution S
    def getCost(self, S):
        return 1 - (sum(m.w for m in S) / sum(m.w for m in self.M))
    
    def run(self, n):
        currS = []
        currentCost = sys.maxsize
        for i in range(n):
            newS = self.pickRandomSolution()
            self.counter += 1
            newS = self.removeOverlaps(newS)
            newCost = self.getCost(newS)
            if newCost == 0:
                return (newS, newCost)
            elif newCost < currentCost:
                currS = newS
                currentCost = newCost
        
        return (currS, self.counter)
            

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

# i1.addMeetings([m1,m2])
# i3.addMeetings([m1,m2])
# i4.addMeetings([m1,m2,m3])
# i5.addMeetings([m2,m3])
# i6.addMeetings([m3])
# i7.addMeetings([m2,m3])
# i8.addMeetings([m1,m3])
# i9.addMeetings([m2,m3])
# i10.addMeetings([m2])


# # Unscheduled Meetings:
# m4 = Meeting([i1,i3,i5], i1, 1, 0.3, datetime(2021,12,10,18), None)
# m5 = Meeting([i1,i3,i4,i5,i6], i5, 2, 0.5, datetime(2021,12,10,10), None)
# m6 = Meeting([i1,i2,i4], i2, 1, 0.99, datetime(2021,12,10,23), None)
# m7 = Meeting([i1,i3,i5,i10], i1, 1, 0.2, datetime(2021,12,10,15), None)
# m8 = Meeting([i1,i3,i4,i5,i9], i5, 2, 0.6, datetime(2021,12,10,18), None)
# m9 = Meeting([i1,i7,i4,i8], i2, 1, 0.8, datetime(2021,12,10,16), None)

# I = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10]
# M = [m4,m5,m6,m7,m8,m9]

# algorithm = RandomAlgorithm(I, M)
# result = algorithm.run(10)
# print(result)
# print(algorithm.getCost(result[0]))