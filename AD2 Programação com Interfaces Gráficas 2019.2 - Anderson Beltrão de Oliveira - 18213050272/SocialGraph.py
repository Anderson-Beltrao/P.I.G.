from DiGraph import DiGraph
class SocialGraph(object):
    #@ class SocialGraph: invoca os comandos dados do arquivo texto e printa os resultados
    classe1 = DiGraph()
    contaArestas = 0
    def inic(self, linha):
        #@ def inic: método que diferencia os comandos dados
        self.linha = linha
        argumentos = self.linha.split()
        comando = argumentos[0]# criacao de commando associando a primeira palavra de cada linha do arquivo
        chave = argumentos[1]

        if comando == "add":
            #@ comando add: chama a função criaGrafo para criar o grafo com os dados fornecidos
            valor2 = argumentos[2]
            valor = str(argumentos[2]) + " " + str(argumentos[3])
            SocialGraph.classe1.criaGrafo(chave,valor,valor2)
            SocialGraph.contaArestas += 1
            addEdge = " (True) - " + str(SocialGraph.contaArestas) + " edges, " + str(SocialGraph.classe1.cNo) + " vertices"
            print(self.linha + " addEdge:" + addEdge)

        if comando == "remove":
            #@ comando remove: chama as funções rmvGrafo e rmvAresta para remover o nó solicitado e suas respectivas arestas
            SocialGraph.classe1.rmvGrafo(chave)

            for k,v in SocialGraph.classe1.grafo.items():
                SocialGraph.classe1.rmvAresta(k,v,chave)

            rA = SocialGraph.contaArestas - SocialGraph.classe1.rmvA
            rN = SocialGraph.classe1.cNo - 1
            SocialGraph.contaArestas = rA
            DiGraph.cNo = rN
            SocialGraph.classe1.listaNo.remove(chave)
            remove = "(True) - "+str(rA)+" edges, "+str(rN)+" vertices"
            print(self.linha+ " remove:" + remove )

        if comando =="showFriends":
            #@ comando showFriend: mostra(printa) os amigos da pessoa solicitada no comando
            dict = SocialGraph.classe1.grafo
            conjunto = set()
            for nomes,valor2 in dict.items():
                if nomes == chave:
                    for i in valor2:
                        if (len(i)) < 2:
                            conjunto.add(("<" + valor2 + ">"))
                        else:
                            conjunto.add(("<" + i + ">"))
            print(self.linha, conjunto)

        if comando == "recommendFriends":
            #@ comando recommendFriends: Método que apresenta(printa) nomes de amigos recomendados para a pessoa em questão
            lista = []
            SocialGraph.classe1.adjacentes()
            #valor = int(argumentos[2]) --- Ignorar
            valor = argumentos[2]
            c = set()
            c2 = set()
            listaAux = []
            rf1 = SocialGraph.classe1.adj[chave]
            for i in rf1:
                if i in SocialGraph.classe1.adj:
                    aux = SocialGraph.classe1.adj[i]
                    for j in aux:
                        c.add(j)
                c.discard(i)
            c.discard(chave)
            for i in c:
                if i not in rf1:
                    c2.add(i)
            c = c2
            #if valor > len(c): --- Ignorar
            if valor == "longDist":
                for i in c:
                    listaAux.append(i)
                for i in listaAux:
                    for xa,va in SocialGraph.classe1.adj.items():
                        if i == xa:
                            if type(va) is str:
                                if va not in c:
                                    if va not in rf1:
                                        c2.add(va)
                            else:
                                for j in va:
                                    if j not in c:
                                        if j not in rf1:
                                            c2.add(j)
                c = c2
            for i in c:
                j = "<" + i + ">"
                lista.append(j)
            print(self.linha, lista)