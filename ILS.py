import random

colorWeights = [0] * 12
##Solução inicial guosa simples
def initialSolution(graph, vertex, kColor, vertexWeight):
    solution = [-1] * int(vertex)
    solution[0] = random.randint(0, kColor - 1)
    while (min(solution) == -1):
        for x in range(1, int(vertex)):
            edges = edgesFromVertex(graph, x)
            colors = possibleColors(kColor)
            for y in edges:
                if (solution[int(y)] == -1):
                    continue
                if solution[int(y)] in colors:
                    colors.remove(solution[int(y)])
            if len(colors) == 0: solution[x] = -1
            else : solution[x] = random.choice(colors)
    for x in range (0, vertex):
        colorWeights[solution[x]] = round(colorWeights[solution[x]] + float(vertexWeight[x]), 2)
    print(colorWeights)
    firstimprovementLocalSearch(solution, colorWeights, kColor, vertex, vertexWeight)


## Todos os vértices que um vértice específico está ligado      
def edgesFromVertex(graph, vertex):
    return graph[vertex]

##Possiveis cores
def possibleColors (kColor):
    colors = list()
    for i in range(0, kColor):
        colors.append(i)
    return colors

def firstimprovementLocalSearch(Instance, colorWeights, kColor, vertex, vertexWeight):
    for x in range(0, kColor):
        for y in range (0, vertex):
            newColorWeights = colorWeights.copy()
            if (Instance[y] != x):
                newColorWeights[Instance[y]] = round(newColorWeights[Instance[y]] - float(vertexWeight[y]), 2)
                newColorWeights[x] = round(newColorWeights[x] + float(vertexWeight[y]), 2)
                if (max(newColorWeights) < max(colorWeights)):
                    Instance[y] = x
                    print(newColorWeights)
                    return Instance

def pertubation(Solution, kColor):
    for x in range (0, 5):
        Color = possibleColors(kColor)
        choosenVertex = random.randint(0, len(Solution) - 1)
        Color.remove(Solution[choosenVertex])
        Solution[choosenVertex] = random.choice(Color)

def countColorWeights(vertex, solution):
    colorWeights = []
    for x in range (0, vertex):
        colorWeights[solution[x]] = round(colorWeights[solution[x]] + float(vertexWeight[x]), 2)