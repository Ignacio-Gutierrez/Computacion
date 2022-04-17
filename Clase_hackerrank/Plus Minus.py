def plusMinus(arr):
    
    positive = 0
    negative = 0
    zero = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative += 1
        else:
            zero += 1
    
    print(positive/len(arr))
    print(negative/len(arr))
    print(zero/len(arr))