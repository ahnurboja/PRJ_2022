from generateInputs import InputGenerator
from algorithmRunner import AlgorithmRunner
import matplotlib.pyplot as plt
import numpy as np

class ComplexityAnalyzer:

    inputs = []
    maxComplexity = 250

    def __init__(self):

        generator = InputGenerator(self.maxComplexity)
        self.inputs = generator.generateInputs()

    
    def run(self):
        efficienciesArray = []
        performanceArray = []
        for input in self.inputs:
            runner = AlgorithmRunner(*input)
            runner.runAlgorithms()
            efficienciesArray.append(runner.efficiencies)
            performanceArray.append(runner.performances)

        complexities = list(range(1, self.maxComplexity+1, 10))

        plt.plot(complexities, np.array(efficienciesArray)[:,0], label='Random Algorithm')
        plt.plot(complexities, np.array(efficienciesArray)[:,1], label='Enumeration Algorithm')
        plt.plot(complexities, np.array(efficienciesArray)[:,2], label='Simulated Annealing')
        plt.legend()
        plt.show()


analyzer = ComplexityAnalyzer()
analyzer.run()
