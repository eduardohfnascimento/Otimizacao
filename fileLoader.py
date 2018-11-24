def loadFile(graph, weights, kColor):
    fileObject = open("cmb/cmb01", "r")
    a, b, kColor = fileObject.readline().split()
    while (len(weights) < int(a)):
        line = fileObject.readline().split()
        for x in line:
            weights.append(x)
            graph[len(weights) - 1] = []
    for line in fileObject:
        if (len(line) == 1): break
        x, y = line.split()
        graph[int(x)].append(y)
        graph[int(y)].append(x)
    fileObject.close()