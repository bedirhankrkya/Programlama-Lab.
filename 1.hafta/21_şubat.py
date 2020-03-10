# Selection sort sıralama algoritması
def Selection(inList=[7, 6, 8, 9, 3, 2, 10, 5, 1]):
    n = len(inList)
    swaps, comparison = 0, 0
    for key in range(n-1):
        for i in range(key+1,n):
            comparison += 1
            if inList[i] < inList[key]:
                swaps += 1
                inList[i], inList[key] = inList[key], inList[i]


# Bubble sort sıralama algoritması
def Bubble(inList=[7, 6, 8, 9, 3, 2, 10, 5, 1]):
    n = len(inList)
    swaps, comparison = 0, 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparison += 1
            if inList[j] > inList[j+1]:
                swaps += 1
                inList[j], inList[j+1] = inList[j+1], inList[j]
