def search_asc(arr, start, end, x):
    while start <= end:
        mid = start + (end-start) // 2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            start = mid+1
        elif x < arr[mid]:
            end = mid-1
    return -1


def search_desc(arr, start, end, x):
    while start <= end:
        mid = start + (end-start) // 2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            end = mid-1
        elif x < arr[mid]:
            start = mid+1
    return -1


def peak(arr, start, end):
    while start <= end:
        mid = start + (end-start) // 2
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid+1] > arr[mid]:
            start = mid+1
        elif arr[mid-1] > arr[mid]:
            end = mid-1


def search_bitonic(arr, key):
    index_max = peak(arr, 0, len(arr)-1)
    #print(index_max)
    x1 = search_asc(arr, 0, index_max-1, key)
    x2 = search_desc(arr, index_max, len(arr)-1, key)
    #print(x1, x2)
    return x1 if x2 == -1 else x2


if __name__ == '__main__':
    arr = [1, 3, 4, 5, 3]
    print(search_bitonic(arr, 3))
