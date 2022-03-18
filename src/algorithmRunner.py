import random
from randomAlgorithm import RandomAlgorithm
from enumeration import EnumerationAlgorithm

class AlgorithmRunner:

    solutions = []
    efficiencies = []
    performances = []

    def __init__(self, I, M):
        randomAlgorithm = RandomAlgorithm(I, M)
        enumerationAlgorithm = EnumerationAlgorithm(I,M)

        self.totalW = 0
        for m in M:
            self.totalW += m.w

        self.algorithms = [
            randomAlgorithm,
            enumerationAlgorithm,
        ]

    def runAlgorithms(self):
        for algorithm in self.algorithms:
            (S, P) = algorithm.run()
            self.solutions.append(S)
            self.performances.append(P)
        self.calculateEfficiencies()
    
    def calculateEfficiencies(self):
        for S in self.solutions:
            weights = 0
            for m in S:
                weights += m.w
            self.efficiencies.append(weights/self.totalW)

            


from scheduler import Individual, Meeting
from datetime import datetime

i1 = Individual("i1")
i2 = Individual("i2")
i3 = Individual("i3")

m1 = Meeting('m1', [i1,i2,i3], i1, 2, 4.0, datetime(2021,12,10,17), None)
m2 = Meeting('m2', [i1,i2,i3], i2, 2, 3.0, datetime(2021,12,10,8), None)
m3 = Meeting('m3', [i1,i2,i3], i2, 4, 2.0, datetime(2021,12,10,17), None)
m4 = Meeting('m4', [i1,i2,i3], i2, 3, 1.0, datetime(2021,12,10,13), None)

I = [i1,i2,i3]
M = [m1,m2,m3,m4]
runner = AlgorithmRunner(I, M)
runner.runAlgorithms()

for i in range(len(runner.algorithms)):
    print('\n\n\nAlgorithm ', runner.algorithms[i], ':')
    print('\nSolution:\n', runner.solutions[i])
    print('\nEfficiency: ', runner.efficiencies[i])
    print('\nPerformances: ', runner.performances[i])