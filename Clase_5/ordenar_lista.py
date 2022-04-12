Lista = [1, 7, 3, 2, 8, 0]

def ordenar(Lista):
    for I in range(len(Lista)):
        for J in range(I + 1, len(Lista)):
            if Lista[I] > Lista[J]:
                TMP = Lista[I]
                Lista[I] = Lista[J]
                Lista[J] = TMP