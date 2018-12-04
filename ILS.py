import random
import InitialSolution
import localSearch

class ILS:
    def __init__(self, graph, vertex, kColor, vertexWeights, iteration, pertubationTax):
        self.graph = graph
        self.vertex = vertex
        self.kColor = kColor
        self.vertexWeights = vertexWeights
        self.iteration = iteration
        self.pertubationTax = pertubationTax

    def pertubation(self):
        instance = self.bestSolution.copy()
        for x in range (0, int(self.pertubationTax * self.vertex)):
            choosenVertex = random.randint(0, len(instance) - 1)
            Color = localSearch.possibleColors(self.kColor,instance, self.graph, choosenVertex)
            if (Color == -1):
                x = x - 1 
                continue
            else:
                instance[choosenVertex] = random.choice(Color)
        return instance
    
    def acceptanceCriteria(self, instance):
        bestSolutionMaxWeight = max(localSearch.countColorWeights(self.vertex, self.bestSolution, self.kColor, self.vertexWeights))
        instanceMaxWeight = max(localSearch.countColorWeights(self.vertex, instance, self.kColor, self.vertexWeights))
        if (instanceMaxWeight < bestSolutionMaxWeight):
            return instance
        else:
            return self.bestSolution

    def run(self):
        self.bestSolution = InitialSolution.initialSolution(self.graph, self.vertex, self.kColor, self.vertexWeights)
        #print ("Solução Inicial",max(localSearch.countColorWeights(self.vertex, self.bestSolution, self.kColor, self.vertexWeights)))
        while (0 != self.iteration):
            instance = self.pertubation()
            instance = localSearch.firstimprovementLocalSearch(instance,self.kColor, self.vertex, self.vertexWeights, self.graph)
            self.bestSolution = self.acceptanceCriteria(instance)
            self.iteration-=1
            #print (max(localSearch.countColorWeights(self.vertex, self.bestSolution, self.kColor, self.vertexWeights)))
        #print (self.bestSolution)
        #print ("Solução Final",max(localSearch.countColorWeights(self.vertex, self.bestSolution, self.kColor, self.vertexWeights)))
        return max(localSearch.countColorWeights(self.vertex, self.bestSolution, self.kColor, self.vertexWeights))


