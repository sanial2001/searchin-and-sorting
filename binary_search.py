def search_rec(arr, start, end, ele):
    if start <= end:
        mid = (start + end) // 2
        if arr[mid] == ele:
            print(mid)
            return mid
        elif ele > arr[mid]:
            search(arr, mid+1, end, ele)
        elif ele < arr[mid]:
            search(arr, start, mid-1, ele)
    else:
        return -1


def search_asc(arr, start, end, ele):
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == ele:
            return mid
        elif ele > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def search_desc(arr, start, end, ele):
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == ele:
            return mid
        elif ele > arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def search(arr, x):
    n = len(arr)
    if n == 1:
        return 0
    else:
        if arr[0] >= arr[n-1]:
            return search_desc(arr, 0, n, x)
        else:
            return search_asc(arr, 0, n, x)


if __name__ == '__main__':
    arr = [6, 6, 6, 6, 6, 6]
    print(search(arr, 6))
