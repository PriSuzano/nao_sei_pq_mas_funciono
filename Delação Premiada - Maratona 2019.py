N, K = list(map(int, input().split(' ')))

superiores = list(map(int , input().split()))
grafo = {}

for i in range(1,len(superiores)+1):
    grafo[i] = []
    for x,elem in enumerate(superiores):

        if elem==i and (x+1)!=i:
            if grafo[elem]:
                grafo[elem].append(x+1)
            else:
                grafo[i].append(x+1)

v = []
v2 = []

cont = 0
pos = 0
pilha = [0]
maior = [1]
def dfs(v, grafo, no):
    global cont
    global K
    global pos
    global n
    global maior

    if no not in v:

        cont += 1

        v.append(no)

        if len(grafo[no]) == 2:
            pilha.append(cont)

        if grafo[no] == []:

            v2.append(maior)
            cont = pilha[len(pilha) - 1]
            pilha.remove(pilha[len(pilha) - 1])
            maior = maior[:cont]


        for elem in grafo[no]:
            maior.append(elem)


            try:
                dfs(v, grafo, elem)

            except:
                continue


dfs(v, grafo, 1)
v3 = []
v5= []
soma = 0
m = len(v2[0])
n = len(v2)
pos2 = v2[0]
for t in range(n):
    for y in v2:

        if len(y) > m:
            m = len(y)
            pos2 = y

    v3.append(pos2)
    v2.remove(pos2)
    m = 0
    pos2 = 0
for i in v3:
    if K == 0:
        break

    for k in i:
        if k in v:
            soma += 1
            v.remove(k)
    v5.append(soma)
    soma = 0
soma = 0
v6 = sorted(v5, reverse=True)

if K > len(v6):
    K = len(v6)
for g in range(K):
    if K == 0:
        break
    soma += v6[g]
    K -= 1
print(soma)
