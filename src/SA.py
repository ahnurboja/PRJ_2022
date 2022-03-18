from scheduler import *
from datetime import datetime, timedelta
from faker import Faker
fake = Faker()
import random
import math

class SimulatedAnnealing:


    # now = datetime.now().replace(microsecond=0, second=0, minute=0)
    now = datetime(2021,12,10,5)

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

    def getCost(self, S):
        tempS = S[:]
        tempS = self.removeOverlaps(tempS)
        return 1 - (sum(m.w for m in tempS) / sum(m.w for m in self.M))

    def simAnneal(self, imax):
        currS = self.pickRandomSolution()
        bestS = currS
        T = 100
        for i in range(1, imax+1):
            propS = self.getNeighbour(currS)
            currT = self.getTemp(i, T)

            if self.getCost(propS) <= self.getCost(currS):
                currS = propS
                if self.getCost(propS) <= self.getCost(bestS):
                    bestS = propS
            elif math.exp( (self.getCost(currS)-self.getCost(propS)) / currT ) > random.randint(0,1):
                currS = propS
            
        return bestS

    def run(self):

        S = self.simAnneal(10)

        return (self.removeOverlaps(S), 10)