def binary_search(arr, start, end, x):
    while start <= end:
        mid = start + (end-start) // 2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            start = mid+1
        elif x < arr[mid]:
            end = mid-1
    return -1


def min_element_index(arr, start, end):
    while start <= end:
        n = len(arr)
        mid = start + (end-start) // 2
        prev = (mid-1+n) % n
        next = (mid+1) % n
        if arr[mid] < arr[prev] and arr[mid] < arr[next]:
            return mid
        elif arr[start] < arr[end]:
            return start
        elif arr[mid] > arr[end]:
            start = mid+1
        elif arr[mid] < arr[start]:
            end = mid-1


def find_element(arr, x):
    index_min = min_element_index(arr, 0, len(arr)-1)
    #print(arr[-1])
    if x > arr[-1]:
        return binary_search(arr, 0, index_min-1, x)
    else:
        return binary_search(arr, index_min, len(arr)-1, x)


if __name__ == '__main__':
    arr = [11, 12, 15, 18, 2, 5, 7]
    print(find_element(arr, 7))
