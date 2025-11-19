def transpose(arr):
    if len(arr) == 0:
        return []
    else:
        for i in arr:
            if len(i) != len(arr[0]):
                raise ValueError
        arr2 = []
        for i in range(len(arr[0])):
            new = []
            for j in range(len(arr)):
                new.append(arr[j][i])
            arr2.append(new)
        return arr2


def row_sums(arr):
    if len(arr) == 0:
        return []
    arr2 = []
    for i in range(len(arr)):
        if len(arr[i]) != len(arr[0]):
            raise ValueError
        else:
            arr2.append(sum(arr[i]))
    return arr2


def col_sums(arr):
    if len(arr) == 0:
        return []
    for i in arr:
        if len(i) != len(arr[0]):
            raise ValueError
    a2 = []
    for i in range(len(arr[0])):
        s = 0
        for j in range(len(arr)):
            s += arr[j][i]
        a2.append(s)
    return a2
