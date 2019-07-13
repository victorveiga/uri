from math import inf;
from heapq import *;

def dijkstra(adj, s):
    d = [inf] * len(adj)
    d[s] = 0
    prev = [-1] * len(adj)
    visitado = [False] * len(adj)

    Q = [(0, s)]
    heapify(Q)

    while Q:
        u = heappop(Q)[1]
        if not visitado[u]:
            visitado[u] = True
            for v, w in adj[u]:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    prev[v] = u
                    heappush(Q, (d[v], v))
    return d, prev

def GetCaminho(APrev, destino):
    resultado = [];
    if APrev[destino] == -1:
        print('Inatingível')
    else:
        s = []
        while destino != -1:
            s.insert(0, destino)
            destino = APrev[destino]
        resultado = s;

    return resultado;

def GetArray(ALen):
    xArray = [];
    for n in range(ALen):
        xArray.append([]);

    return xArray;

def GetCusto(ACaminho, AEstradas):
    resultado = 0;
    x, y = -1, -1;
    x = ACaminho.pop(0);

    while len(ACaminho) > 0:
        y = ACaminho.pop(0);
        for n in AEstradas[x]:
            if n[0] == y:
                resultado = resultado + n[1];
                break;

        x = y;

    return resultado;

# 1123 - Desvio de Rota
xResultados = [];
QtdeCidades, QtdeEstradas, QtdeRotas, CidadeVeiculoConcertado = 1,1,1,1;
while True:
    QtdeCidades, QtdeEstradas, QtdeRotas, CidadeVeiculoConcertado = [int(n) for n in input().split(' ')];
    if sum([QtdeCidades, QtdeEstradas, QtdeRotas, CidadeVeiculoConcertado]) <= 0:
        break;

    xEstradas = GetArray(QtdeCidades);
    for n in range(QtdeEstradas):
        # CidadeU, CidadeV, Custo
        CidadeU, CidadeV, Custo = [int(n) for n in input().split(' ')];

        if (CidadeU >= QtdeRotas) and (CidadeV >= QtdeRotas):
            xEstradas[CidadeU].append((CidadeV, Custo));
            xEstradas[CidadeV].append((CidadeU, Custo));

        if (CidadeU >= QtdeRotas) and (CidadeV < QtdeRotas):
            xEstradas[CidadeU].append((CidadeV, Custo));

        if (CidadeU < QtdeRotas) and (CidadeV >= QtdeRotas):
            xEstradas[CidadeV].append((CidadeU, Custo));

        if (CidadeU < QtdeRotas) and (CidadeV < QtdeRotas) and (abs(CidadeU - CidadeV) == 1):
            xEstradas[CidadeU].append((CidadeV, Custo));
            xEstradas[CidadeV].append((CidadeU, Custo));

    aux = [];
    d, aux = dijkstra(xEstradas, CidadeVeiculoConcertado)
    destino = QtdeRotas - 1;
    caminho = GetCaminho(aux, destino);
    #print(caminho);
    #print(xEstradas);
    xResultados.append(GetCusto(caminho, xEstradas));

for n in xResultados:
    print(n)
