def compareTriplets(a, b):

    alice = 0
    bob = 0

    for i in range(3):
        if a[i] > b[i]:
            a += 1
        elif a[i] < b[i]:
            b += 1
            
    return [alice, bob]