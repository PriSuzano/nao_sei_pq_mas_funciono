import operator

N, K = list(map(int, input().split(' ')))

superiores = list(map(int , input().split()))
grafo = {}

# for i in range(1,len(superiores)+1):
#     grafo[i] = []
#     for x,elem in enumerate(superiores):
#         if elem==i and (x+1)!=i:
#             if grafo[elem]:
#                 grafo[elem].append(x+1)
#             else:
#                 grafo[i].append(x+1)

grafo = {
    1:[2],
    2:[3,4],
    3:[5,6],
    4:[7,8],
    5:[9],
    6:[],
    7:[],
    8:[],
    9:[],
}

grafo_inv = {}
grafo_inv[1] = [1]
for nodo in grafo:
    for elem in grafo[nodo]:
        grafo_inv[elem] = [nodo]

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

leafes = {}
start_leaf = 1
for nodo in grafo:
    if grafo[nodo] == []:
        leafes[nodo] = levels[nodo]
        if levels[nodo] > levels[start_leaf]:
            start_leaf = nodo

visited = []
leaf_rem=[]
def dfs(K, visited, leafes, graph, node):
    # if K==0:
    #     print('K', K)
    #     print('visited', visited)
    #     print(len(visited)+1)
    #     return
    
    if node!=1 and node not in visited:
        print('1 if')
        print('K', K)
        print("node", node)
        
        leafes.pop(node, None)
        visited.append(node)

        for elem in graph[node]:
            dfs(K, visited, leafes, graph, elem)

    elif leafes != {}:
        print('2 if')
        K-=1
        print('K', K)
        print("node", node)
        if node != 1:
            K+=1
            s = visited.pop()

            if s not in leafes:
                visited.append(s)
            
            else:
                leaf_rem.append(s)
                leafes.pop(s, None)
                
            print(leaf_rem)
        
        maximum = max(leafes.items(), key=operator.itemgetter(1))[0]
        print('maximum', maximum)
        dfs(K, visited, leafes, graph, maximum)

    else:
        print('3 if')
        print('leafes', leafes)
        print('leaf_rem', leaf_rem)
        print('visited', visited)
        if K!=0:
            print('K', K)
            print(len(visited)+1+K)
        else:
            print(len(visited)+1)
        return


print('grafo', grafo)
print('grafo_inv', grafo_inv)
print('leafes', leafes)

K-=1
maximum = max(leafes.items(), key=operator.itemgetter(1))[0]
dfs(K, visited, leafes, grafo_inv, maximum)