def search_first(arr, start, end, x):
    result = 0
    while start <= end:
        mid = start + (end - start) // 2
        if x == arr[mid]:
            result = mid
            end = mid -1
        elif x > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    #print(result)
    return result


def search_last(arr, start, end, x):
    result = -1
    while start <= end:
        mid = start + (end - start) // 2
        if x == arr[mid]:
            result = mid
            start = mid + 1
        elif x > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    #print(result)
    return result


def count(arr, x):
    return search_last(arr, 0, len(arr)-1, x) - search_first(arr, 0, len(arr)-1, x) + 1


if __name__ == '__main__':
    arr = [1, 10, 10, 10, 17, 19, 25]
    print(count(arr, 10))
