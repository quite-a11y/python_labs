def min_max(arr):
    if len(arr) == 0:
        raise ValueError
    else:
        k = arr[0]
        k2 = arr[0]
        for i in arr:
            if i > k:
                k = i
            if i < k2:
                k2 = i
        return(k2,k)


def unique_sorted(arr):
    if len(arr) == 0:
        return []
    else:
        arr2 = []
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                if arr[i] > arr[j]:
                    a = arr[i]
                    arr[i] = arr[j]
                    arr[j] = a
        for i in arr:
            if arr.count(i) == 1:
                arr2.append(i)
            elif arr.count(i) != 1:
                arr2.append(i)
        return arr2


def flatten(arr):
    arr2 = []
    for i in arr:
        if isinstance(i,(tuple,list)):
            for j in i:
                arr2.append(j)
        else:
            raise TypeError
    return arr2









