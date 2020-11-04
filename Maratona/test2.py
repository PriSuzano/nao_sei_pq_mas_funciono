import copy

#entradas do problema
N, K = list(map(int, input().split(' ')))
superiores = list(map(int , input().split()))

#dicionário no formato -> superior: [subordinados]
grafo = {}
for i in range(1,len(superiores)+1):
    grafo[i] = []
    for x,elem in enumerate(superiores):
        if elem==i and (x+1)!=i:
            if grafo[elem]:
                grafo[elem].append(x+1)
            else:
                grafo[i].append(x+1)

#dicionário no formato -> subordinado: [superior]
grafo_inv = {}
grafo_inv[1] = [1]
for nodo in grafo:
    for elem in grafo[nodo]:
        grafo_inv[elem] = [nodo]

#BFS para calcular o nível de cada nodo do grafo
levels = {}
def bfs(graph, start):
    global levels
    visited = []

    queue = [start]
    visited= [start]
    levels[start]= 0

    while queue:
        node = queue.pop(0)
        visited.append(node)
        neighbours = graph[node]

        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
                levels[neighbour]= levels[node]+1

bfs(grafo,1)

#DFS para visitar os nodos da folha até a raiz e criar dicionário no formato -> nodo folha: [sequência de nodos até a raiz]
def dfs(grafo_leafes_dfs, graph, node, visited):
    if node!=1:
        visited.append(node)
        for elem in graph[node]:
            dfs(grafo_leafes_dfs, grafo_inv, elem, visited)
    else:
        visited.append(1)
        visited.pop(0)
    return visited

grafo_leafes_dfs = {}
for nodo in grafo:
    if grafo[nodo] == []:
        grafo_leafes_dfs[nodo] = dfs(grafo_leafes_dfs, grafo_inv, nodo, [])

deeper = list(grafo_leafes_dfs.keys())[0]
for leaf in grafo_leafes_dfs:
    if len(grafo_leafes_dfs[deeper]) < len(grafo_leafes_dfs[leaf]):
        deeper = leaf

#loop para visitar os nodos da folha até a raiz e ir prendendo os mafiosos
stop = len(grafo_leafes_dfs[deeper])
grafo_result = copy.deepcopy(grafo_leafes_dfs)
arrested = []
K-=1
while K>=0 and len(arrested)!=len(superiores):
    deeper = list(grafo_result.keys())[0]
    for leaf in grafo_result:
        if len(grafo_result[deeper]) < len(grafo_result[leaf]):
            deeper = leaf

    arrested.append(deeper)
    K-=1
    
    for elem in grafo_leafes_dfs[deeper]:
        removed = grafo_result[deeper].pop(0)
        if removed not in arrested:
            arrested.append(removed)

        if(stop == len(grafo_result[deeper])+1):
            for leaf in grafo_result:
                if grafo_result[leaf][0] == removed:
                    grafo_result[leaf] = []

#printar resposta
print(len(arrested))