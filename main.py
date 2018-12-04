import fileLoader
import ILS
import sys
import time
arquivos = ["cmb03", "cmb06", "cmb07", "cmb04", "cmb09", "cmb10"]

arquivoDeEntradafsd, arquivoDeSaida, iteracoes, pertubacao =input().split(" ")

pertubacao = 0.15
iteracoes = 40
for arquivoDeEntrada in arquivos:
    tempo = 0
    saida = 0
    for i in range(5):
        inicio = time.time()
        graph = {}
        weights = []
        kColor = fileLoader.loadFile(graph, weights, arquivoDeEntrada)

        ils =  ILS.ILS(graph, len(weights), int(kColor), weights, int(iteracoes), float(pertubacao))
        saida = saida + ils.run()
        fim = time.time()
        tempo = tempo + (fim - inicio)
    saida = saida/5
    tempo = tempo /5
    print("arquivo", arquivoDeEntrada)
    print ("tempo médio", tempo)
    print("saida media", saida)
    print("=========================")
    #pertubacao+=0.


