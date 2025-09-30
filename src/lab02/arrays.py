# def min_max(arr):
#     if len(arr) == 0:
#         return ValueError
#     else:
        # k = 0
        # k2 = float('inf')
        # for i in arr:
        #     if i >= k:
        #         k = i
        #     if i < k2:
        #         k2 = i
#         return(k2,k)
# print(min_max([]))

def unique_sorted(arr):
    if len(arr) == 0:
        return arr
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
            elif arr.count(i) != 1 and arr2.count(i) == 0:
                arr2.append(i)
        return arr2
#print(unique_sorted([1.0,1,2.5,2.5,0]))

def flatten(arr):
    arr2 = []
    for i in arr:
        for j in i:
            if type(j) != str:
                arr2.append(j)
            else:
                return TypeError
    return arr2
#print(flatten([[1, 2], "ab"]))








