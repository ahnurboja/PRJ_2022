from scheduler import *
import schedulerUtils as su
from datetime import datetime, timedelta
from faker import Faker
fake = Faker()
import random
import math

class SimulatedAnnealing:


    # now = datetime.now().replace(microsecond=0, second=0, minute=0)
    now = datetime(2021,12,10,5)
    counter = 0 # Counter for number of solutions searched.

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
    
    def pickRandomTime(self, m):
        maxStartDate = m.d - timedelta(hours=m.l)
        t = fake.date_time_between(start_date=self.now, end_date=maxStartDate).replace(microsecond=0, second=0, minute=0)
        return t

    def getNeighbour(self, S):
        randIdx = random.randint(0, len(S)-1)

        S[randIdx].t = self.pickRandomTime(S[randIdx])
        return(S)

    def getTemp(self, i, T):
        return T*(0.95**i)

    def getCost(self, S):
        tempS = S[:]
        return 1 - (su.getUtility(S) / sum(m.w for m in self.M))

    def simAnneal(self):
        currS = self.pickRandomSolution()
        bestS = currS
        T = 100
        for i in range(1, self.n+1):
            self.counter += 1
            propS = self.getNeighbour(currS)
            currT = self.getTemp(i, T)

            if self.getCost(propS) <= self.getCost(currS):
                currS = propS
                if self.getCost(propS) <= self.getCost(bestS):
                    bestS = propS
            elif math.exp( (self.getCost(currS)-self.getCost(propS)) / currT ) > random.uniform(0,1):
                currS = propS
            if currT < 1:
                return bestS
            
        return bestS

    def run(self):

        S = self.simAnneal()

        return (S, self.counter)