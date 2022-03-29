import schedulerUtils as su
import matplotlib.pyplot as plt
import numpy as np
from genGA import GeneticAlgorithm
from randomAlgorithm import RandomAlgorithm
from enumeration import EnumerationAlgorithm
from SA import SimulatedAnnealing
from genGA import GeneticAlgorithm
import copy
from time import time

class AlgorithmRunner:

    def __init__(self, I, M):
        self.solutions = []
        self.efficiencies = []
        self.performances = []

        randomAlgorithm = RandomAlgorithm(copy.deepcopy(I), copy.deepcopy(M), 1000)
        enumerationAlgorithm = EnumerationAlgorithm(copy.deepcopy(I), copy.deepcopy(M))
        simulatedAnnealing = SimulatedAnnealing(copy.deepcopy(I), copy.deepcopy(M), 1000)
        geneticAlgorithm = GeneticAlgorithm(copy.deepcopy(I), copy.deepcopy(M), 5)

        self.totalW = 0
        for m in M:
            self.totalW += m.w

        self.algorithms = [
            randomAlgorithm,
            enumerationAlgorithm,
            simulatedAnnealing,
            geneticAlgorithm
        ]

    def runAlgorithms(self):
        # for algorithm in self.algorithms:
        #     (S, P) = algorithm.run()
        #     self.solutions.append(S)
        #     self.performances.append(P)
        # Random Algorithm:
        start = time()
        (S, P) = self.algorithms[0].run()
        self.solutions.append(S)
        self.performances.append(P)
        # print("Random Algorithm Running Time: ",time()-start)
        # Enumeration Algorithm:
        start = time()
        (S, P) = self.algorithms[1].run()
        self.solutions.append(S)
        self.performances.append(P)
        # print("Enumeration Algorithm Running Time: ",time()-start)
        # Simulated Annealing:
        start = time()
        (S, P) = self.algorithms[2].run()
        self.solutions.append(S)
        self.performances.append(P)
        # print("Simulated Annealing Running Time: ",time()-start)
        # # Genetic Algorithm:
        # start = time()
        # (S, P) = self.algorithms[3].run()
        # self.solutions.append(S)
        # self.performances.append(P)
        # print("Genetic ALgorithm Running Time: ",time()-start)


        self.calculateEfficiencies()
    
    def calculateEfficiencies(self):
        for S in self.solutions:
            self.efficiencies.append(su.getUtility(S)/self.totalW)

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
            