import random

##Solução inicial guosa simples
def initialSolution(graph, vertex, kColor):
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
            if len(colors) == 0: solution[x] = -1#random.randint(0, kColor - 1)
            else : solution[x] = random.choice(colors)

## Todos os vértices que um vértice específico está ligado      
def edgesFromVertex(graph, vertex):
    return graph[vertex]

def possibleColors (kColor):
    colors = list()
    for i in range(0, kColor):
        colors.append(i)
    return colors