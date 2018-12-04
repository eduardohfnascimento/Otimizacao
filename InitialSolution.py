import random

def initialSolution(graph, vertex, kColor, vertexWeight):
    solution = [-1] * int(vertex)
    #solution[0] = random.randint(0, kColor - 1)

    while (min(solution) == -1):
        #solution = [-1] * int(vertex)
        vertexShuflle = [[i] for i in range(vertex)]
        random.shuffle(vertexShuflle)
        for x in vertexShuflle:
            edges = edgesFromVertex(graph, x[0])
            colors = possibleColors(kColor)
            for y in edges:
                if (solution[int(y)] == -1):
                    continue
                if solution[int(y)] in colors:
                    colors.remove(solution[int(y)])
            if len(colors) == 0: 
                solution[x[0]] = -1
                break
            else : solution[x[0]] = random.choice(colors)
    return solution

## Todos os vértices que um vértice específico está ligado      
def edgesFromVertex(graph, vertex):
    return graph[vertex]

##Possiveis cores
def possibleColors (kColor):
    colors = list()
    for i in range(0, kColor):
        colors.append(i)
    return colors

