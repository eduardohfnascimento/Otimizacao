import fileLoader
import ILS

graph = {}
weghts = []
kColor = fileLoader.loadFile(graph, weghts)
ILS.initialSolution(graph, len(weghts), int(kColor))