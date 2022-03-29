from scheduler import *
import schedulerUtils as su
from datetime import datetime, timedelta
from faker import Faker
fake = Faker()
import math
import random
import copy
from time import time

class GeneticAlgorithm:
    
    # now = datetime.now().replace(microsecond=0, second=0, minute=0)
    now = datetime(2021,12,10,5)
    counter = 0

    def __init__(self, I, M, n):
        self.I = I
        self.M = M
        self.n = n

    def pickRandomSolution(self):

        # For each meeting in M, apply a random start time
        S = []
        for meeting in self.M:
            m = copy.deepcopy(meeting)
            maxStartDate = m.d - timedelta(hours=m.l)
            m.t = fake.date_time_between(start_date=self.now, end_date=maxStartDate).replace(microsecond=0, second=0, minute=0)
            S.append(m)

        return S
    
    def intersect(self, m1, m2):
        return max(m1.t,m2.t) < min(m1.t+timedelta(hours=m1.l),m2.t+timedelta(hours=m2.l)) and not set(m1.A).isdisjoint(m2.A)

    def getAvgFitness(self, P):
        start = time()
        total = 0
        for S in P:
            total += su.getUtility(S)*P[S]
        return total / sum(P.values())

    def getNeighbour(self, S):
        randIdx = random.randint(0, len(S)-1)
        newS = copy.deepcopy(S)
        newS[randIdx].t = self.pickRandomTime(newS[randIdx])
        return(newS)

    def pickRandomTime(self, m):
        maxStartDate = m.d - timedelta(hours=m.l)
        t = fake.date_time_between(start_date=self.now, end_date=maxStartDate).replace(microsecond=0, second=0, minute=0)
        return t

    def getBestSolution(self, P):
        S = []
        bestF = 0
        for s in P:
            f = su.getUtility(s)
            if (f > bestF):
                S = s
                bestF = f
        return S

    def run(self):
        currP = {}
        for i in range(30):
            S = tuple(self.pickRandomSolution())
            if S in currP:
                currP[S] = currP[S]+1
            else:
                currP[S] = 1
        for i in range(self.n):
            self.counter += 1
            newP = {}
            avgF = self.getAvgFitness(currP)
            for S in currP:
                if len(currP) == 1:
                    return (S, self.counter)
                currN = currP[S]
                f = su.getUtility(S)
                newN = math.floor(currN*(f/avgF))
                for i in range(newN):
                    newS = self.getNeighbour(copy.deepcopy(S))
                    if newS in newP:
                        newP[S] = newP[S]+1
                    else:
                        newP[S] = 1

            currP = newP
        bestS = self.getBestSolution(currP)
        return (bestS, self.counter)



