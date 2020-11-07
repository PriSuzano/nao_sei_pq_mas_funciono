def binary_search(l, n):
    ini = 0
    end = len(l) - 1

    while(ini <= end):

        media = (ini + end) // 2

        if l[media] == n:
            print("Valor",l[media], "está encontra na posição", media)
            return 0
        if n > l[media]:
            ini = media + 1
        else:
            end = media - 1

    print("Valor não está na lista")
    return -1

binary_search([3, 6, 9, 10, 15], 16)
