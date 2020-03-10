"""bir diziyi iki parçaya ayırıcaz 
1)sorted
2)unsorted
min---------------------------max
       unsorted  ↑   sorted
unsorted sıralandıtan sonra en buyuk terim sorted yerine aktarılır.



"""

""" İnsertion Short Algoritması"""


def insertionShort(arr) :
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while(j>=0) and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
print(insertionShort(arr=[5,6,2,9,1,7,3]))
        
"""Shell Short Algoritması"""
def ShellSort(array=[4, 3, 2, 1]):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j-gap] > temp:
                array[j] = array[j-gap]
                j = j - gap
            array[j] = temp
        #aralık değerini yarıya indirir.
        gap //= 2
    return array
        
    