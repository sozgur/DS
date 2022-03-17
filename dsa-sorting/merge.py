# merge two sorted array as new sorted array
def merge(arr1, arr2):
    result = []
    i = 0
    j = 0
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    while i < len_arr1 and j < len_arr2:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len_arr1:
        result.append(arr1[i])
        i += 1

    while j < len_arr2:
        result.append(arr2[j])
        j += 1

    return result


# divede the array and sort them while merge
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
        

