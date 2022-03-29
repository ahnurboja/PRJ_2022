# Input: individuals, unscheduledMeetings
# Output: inputListOfMeetings, numberOfSolutionsSearched

from scheduler import *
import schedulerUtils as su
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

    def __init__(self, I, M, n):
        self.I = I
        self.M = M
        self.n = n

    def pickRandomSolution(self):

        # For each meeting in M, apply a random start time
        S = []
        for m in self.M:
            maxStartDate = m.d - timedelta(hours=m.l)
            m.t = fake.date_time_between(start_date=self.now, end_date=maxStartDate).replace(microsecond=0, second=0, minute=0)
            S.append(m)

        return S
                    
                


    # calculate cost of solution S
    def getCost(self, S):
        return 1 - (su.getUtility(S) / sum(m.w for m in self.M))
    
    def run(self):
        currS = []
        currentCost = sys.maxsize
        for i in range(self.n):
            newS = self.pickRandomSolution()
            self.counter += 1
            newCost = self.getCost(newS)
            if newCost == 0:
                return (newS, newCost)
            elif newCost < currentCost:
                currS = newS
                currentCost = newCost
        S = currS
        return (S, self.counter)