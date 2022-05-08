def search_first(arr, start, end, x):
    result = -1
    while start <= end:
        mid = start + (end - start) // 2
        if x == arr[mid]:
            #print(arr[mid], mid)
            result = mid
            end = mid-1
        elif x > arr[mid]:
            start = mid+1
        else:
            end = mid-1
    return result


def search_last(arr, start, end, x):
    result = -1
    while start <= end:
        mid = start + (end - start) // 2
        if x == arr[mid]:
            #print(arr[mid], mid)
            result = mid
            start = mid+1
        elif x > arr[mid]:
            start = mid+1
        else:
            end = mid-1
    return result


if __name__ == '__main__':
    arr = [1, 3, 3, 3, 5, 6]
    print(search_first(arr, 0, len(arr) - 1, 3))
    print(search_last(arr, 0, len(arr) - 1, 3))
