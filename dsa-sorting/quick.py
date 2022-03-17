def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def pivot(arr, start, end):
    pivotIdx = start
    storeIdx = start+1
    for i in range(start+1, end+1):
        if arr[pivotIdx] > arr[i]:
            swap(arr, i, storeIdx)
            storeIdx += 1

    swap(arr, storeIdx-1, pivotIdx) 

    # return pivot idx
    return storeIdx-1

def quick_sort(arr):
    def helper(arr, left, right):
        if left < right:
            pivotIndx = pivot(arr, left, right)
            helper(arr, pivotIndx+1, right)
            helper(arr, left, pivotIndx-1)
        
        return arr

    return helper(arr, 0, len(arr)-1)

