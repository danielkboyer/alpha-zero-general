import matplotlib.pyplot as plt
import numpy as np
import math
class Graph():
    
    def __init__(self):
        self.iteration = int(1)
        self.percents = [0]

    def add_iteration(self,percentBetter):
        self.iteration+=1
        better = percentBetter-50
        if better < 0:
            better = 0
        self.percents.append(better)

    def save_plot(self):
        xList = np.arange(0,self.iteration)
        plt.plot(xList,self.percents)
        plt.xlabel("Iteration")
        plt.ylabel("Percent Better")
        plt.xticks(xList)
        plt.title("NN compared to previous NN")
        plt.savefig(f'iteration{self.iteration-1}_percentage.png')

def main():
    g = Graph()
    g.add_iteration(65)
    g.save_plot()
    g.add_iteration(80)
    g.save_plot()
    g.add_iteration(5)
    g.save_plot()
    g.add_iteration(34)
    g.save_plot()
if __name__ == "__main__":
    main()
