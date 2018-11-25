import fileLoader
import ILS

graph = {}
weights = []
kColor = fileLoader.loadFile(graph, weights)
ILS.initialSolution(graph, len(weights), int(kColor), weights)