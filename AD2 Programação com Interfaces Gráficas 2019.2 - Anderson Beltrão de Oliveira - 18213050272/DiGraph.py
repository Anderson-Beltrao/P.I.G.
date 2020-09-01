class DiGraph(object):
    grafo = dict()
    adj = dict()
    x1 = ""
    cNo = 1
    rmvA = 1
    listaNo = []
    #@ class DiGraph: classe na qual o grafo é criado, entre outros métodos
    def criaGrafo(self, chave, valor, valor2):
        #@ def criaGrafo: Método que cria o grafo usando um dicionário
        if DiGraph.cNo == 1:
            DiGraph.cNo += 1
            DiGraph.listaNo.append(valor2)
            DiGraph.listaNo.append(chave)
        else:
            if (valor2 not in DiGraph.listaNo):
                DiGraph.listaNo.append(valor2)
                DiGraph.cNo += 1
            if (chave not in DiGraph.listaNo):
                DiGraph.listaNo.append(chave)
                DiGraph.cNo += 1
        if chave not in DiGraph.grafo:
            DiGraph.grafo[chave] = (valor)
            DiGraph.x1 = []
            DiGraph.x1.append(valor)
        else:
            DiGraph.x1 = []
            for xave,walor in DiGraph.grafo.items():
                if xave == chave:
                    if type(walor) is str:
                        DiGraph.x1.append(walor)
                    else:
                        DiGraph.x1 = walor
            DiGraph.x1.append(valor)
            DiGraph.grafo[chave] = DiGraph.x1

    def rmvGrafo(self, chave):
        #@ def rmvGrafo: Método que remove um nó do grafo
        DiGraph.rmvA = 1
        if chave in DiGraph.grafo:
            if DiGraph.grafo[chave] == "":
                DiGraph.rmvA = 0
            DiGraph.grafo.pop(chave)
        else:
            DiGraph.rmvA = 0

    def rmvAresta(self, chave, valor, aresta):
        #@ def rmvAresta: Método que remove as arestas do nó removido

        if type(valor) is str:
            v2 = valor.split(" ")
            v3 = v2[0]
            if v3 == aresta:
                DiGraph.grafo[chave] = ""
                DiGraph.rmvA += 1
        else:
            cont = -1
            y = DiGraph.grafo[chave]
            for i in y:
                w = i.split(" ")
                q = w[0]
                cont += 1
                if q == aresta:
                    p = y[cont]
                    y.remove(p)
                    DiGraph.grafo[chave] = y
                    DiGraph.rmvA += 1

    def adjacentes(self):
        #@ def adjacentes: Método que cria um dicionário com apenas as arestas
        for chave, valor in DiGraph.grafo.items():
            lista = []
            if type(valor) is str:
                x = valor.split()
                lista.append(x[0])
            else:
                for i in valor:
                    z = i.split()
                    lista.append(z[0])
            DiGraph.adj[chave] = lista
