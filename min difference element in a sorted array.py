def floor(arr, start, end, x):
    result = -1
    while start <= end:
        mid = start + (end - start) // 2
        if x >= arr[mid]:
            result = arr[mid]
            start = mid + 1
        elif x < arr[mid]:
            end = mid - 1
    return result


def ceil(arr, start, end, x):
    result = -1
    while start <= end:
        mid = start + (end - start) // 2
        if x <= arr[mid]:
            result = arr[mid]
            end = mid - 1
        elif x > arr[mid]:
            start = mid + 1
    return result


def min_difference(arr, key):
    v1 = floor(arr, 0, len(arr) - 1, key)
    v2 = ceil(arr, 0, len(arr) - 1, key)
    if v1 == -1:
        return v2
    elif v2 == -1:
        return v1
    else:
        x1 = abs(v1 - key)
        x2 = abs(v2 - key)
        return v1 if x1 < x2 else v2


if __name__ == '__main__':
    arr = [2, 5, 7, 10, 15]
    print(min_difference(arr, 0))
