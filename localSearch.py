import InitialSolution

def firstimprovementLocalSearch(Instance, kColor, vertex, vertexWeight, graph):
    colorWeights = countColorWeights(vertex, Instance, kColor, vertexWeight)
    bestImprovement = colorWeights.copy()
    bestImprovementInstace = Instance.copy()
    #for x in range(0, kColor):
    for y in range (0, vertex):
        newColor = possibleColors (kColor, Instance, graph, y)
        if (newColor == -1): continue
        else:
            for color in newColor:
                newColorWeights = colorWeights.copy()
                if (Instance[y] != color):
                    newColorWeights[Instance[y]] = round(newColorWeights[Instance[y]] - float(vertexWeight[y]), 2)
                    newColorWeights[color] = round(newColorWeights[color] + float(vertexWeight[y]), 2)
                    if (max(newColorWeights) < max(bestImprovement)):
                        bestImprovementInstace = Instance.copy()
                        bestImprovementInstace[y] = color
                        bestImprovement = newColorWeights.copy()

    return bestImprovementInstace

def countColorWeights(vertex, instance, kColor, vertexWeight):
    colorWeights = [0] * kColor
    for x in range (0, vertex):
        colorWeights[instance[x]] = round(colorWeights[instance[x]] + float(vertexWeight[x]), 2)
    return colorWeights

##Possiveis cores
def possibleColors (kColor, instance, graph, vertex):
    colors = list()
    for i in range(0, kColor):
        colors.append(i)
    edges = InitialSolution.edgesFromVertex(graph, vertex)
    for y in edges:
        if instance[int(y)] in colors:
                colors.remove(instance[int(y)])
        if len(colors) == 0: return -1
    return colors