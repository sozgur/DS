def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swaped=False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
                swaped=True

        if swaped is False:
            break

    return arr

       
