from generateInputs import InputGenerator
from algorithmRunner import AlgorithmRunner
import matplotlib.pyplot as plt
import numpy as np
from time import time
import schedulerUtils as su

class ComplexityAnalyzer:

    maxComplexity = 100

    def __init__(self):

        start = time()
        self.generator = InputGenerator(self.maxComplexity)
        print("Input Generator Running Time: ", time()-start)

    
    def run(self):
        efficiencies3DArray = []
        performance3DArray = []
        for i in range(50):
            print(i+1)
            efficiencies2DArray = []
            performance2DArray = []
            for complexity in range(1, self.maxComplexity+1, 10):
                input = self.generator.generateInput(complexity)
                runner = AlgorithmRunner(*input)
                runner.runAlgorithms()
                efficiencies2DArray.append(runner.efficiencies)
                performance2DArray.append(runner.performances)
            efficiencies3DArray.append(efficiencies2DArray)
            performance3DArray.append(performance2DArray)

        efficiencies = np.mean(np.array(efficiencies3DArray), axis=0)

        complexities = list(range(1, self.maxComplexity+1, 10))

        plt.plot(complexities, np.array(efficiencies)[:,0], label='Random Algorithm')
        plt.plot(complexities, np.array(efficiencies)[:,1], label='Enumeration Algorithm')
        plt.plot(complexities, np.array(efficiencies)[:,2], label='Simulated Annealing')
        # plt.plot(complexities, np.array(efficiencies)[:,3], label='Genetic Algorithm')
        plt.legend()
        plt.show()


analyzer = ComplexityAnalyzer()
analyzer.run()
