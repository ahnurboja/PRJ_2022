import random
import matplotlib.pyplot as plt
import numpy as np
from randomAlgorithm import RandomAlgorithm
from enumeration import EnumerationAlgorithm
from SA import SimulatedAnnealing
import copy

class AlgorithmRunner:

    def __init__(self, I, M):
        self.solutions = []
        self.efficiencies = []
        self.performances = []

        randomAlgorithm = RandomAlgorithm(copy.deepcopy(I), copy.deepcopy(M), 1000)
        enumerationAlgorithm = EnumerationAlgorithm(copy.deepcopy(I), copy.deepcopy(M))
        simulatedAnnealing = SimulatedAnnealing(copy.deepcopy(I), copy.deepcopy(M), 1000)

        self.totalW = 0
        for m in M:
            self.totalW += m.w

        self.algorithms = [
            randomAlgorithm,
            enumerationAlgorithm,
            simulatedAnnealing
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

    def createGraphs(self):
        names = ["Random", "Enumeration", "SA"]

        fig, axs = plt.subplots(1, 2, figsize=(10, 5))
        axs[0].bar(names, self.efficiencies)
        axs[0].set_ylim(ymin=0,ymax=1)
        axs[0].set_ylabel("efficiency")
        axs[1].bar(names, self.performances)
        axs[1].set_ylabel("performance")
        fig.suptitle('Global Efficiency & Performance')

        plt.show()
            