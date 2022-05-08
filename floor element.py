def floor(arr, start, end, x):
    result = -1
    while start <= end:
        mid = start + (end-start) // 2
        if x >= arr[mid]:
            result = arr[mid]
            start = mid + 1
        elif x < arr[mid]:
            end = mid-1
    return result


if __name__ == '__main__':
    arr = [2, 4, 6, 8, 10, 12]
    print(floor(arr, 0, len(arr)-1, 8))
