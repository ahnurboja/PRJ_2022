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
    n = 20 # Number of iterations
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
    
    def removeOverlaps(self, S):
        overlaps = True
        while(overlaps):
            overlaps = False
            for i in range(len(S)-1):
                m1 = S[i]
                for j in range(i+1,len(S)):
                    m2 = S[j]
                    if max(m1.t,m2.t) < min(m1.t+timedelta(hours=m1.l),m2.t+timedelta(hours=m2.l)) and len(set(m1.A).intersection(m2.A)) > 0:
                        # if there is an overlap: remove the lowest priority
                        if m1.w > m2.w:
                            del S[j]
                        else:
                            del S[i]
                        overlaps = True
                        break
                else:
                    continue
                break
        return(S)
                    
                


    # calculate cost of solution S
    def getCost(self, S):
        return 1 - (sum(m.w for m in S) / sum(m.w for m in self.M))
    
    def run(self):
        currS = []
        currentCost = sys.maxsize
        for i in range(self.n):
            newS = self.pickRandomSolution()
            self.counter += 1
            newS = self.removeOverlaps(newS)
            newCost = self.getCost(newS)
            if newCost == 0:
                return (newS, newCost)
            elif newCost < currentCost:
                currS = newS
                currentCost = newCost
        S = self.removeOverlaps(currS)
        return (S, self.counter)