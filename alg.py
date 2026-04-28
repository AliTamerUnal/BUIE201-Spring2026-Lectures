def find_A(LST, target):
    for i in range(len(LST)):
        if LST[i] == target:
            return i
    return -1

def find_B(LST, target):
    for a in LST:
        if a == target:
            return LST.index(a)
    return -1

def find_C(LST, target):
    for i, a in enumerate(LST):
        if a == target:
            return i
    return -1


def bubble_sort(LST):
    n = len(LST)
    for i in range(n):
        for j in range(0, n-i-1):
            if LST[j] > LST[j+1]:
                LST[j], LST[j+1] = LST[j+1], LST[j]
    return LST


find_A([1, 2, 3, 4, 5], 3)  # returns 2
find_B(["a", "b", "c"], "b")  # returns 1
find_C(["a", "b", "c"], "b")  # returns 1

bubble_sort([5, 2, 9, 1, 5, 6])  # returns [1, 2, 5, 5, 6, 9]

