def search(arr, start ,end, x):
    while start <= end:
        mid = start + (end-start) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid-1] == x and (mid-1) <= start:
            return mid-1
        elif arr[mid+1] == x and (mid+1) <= end:
            return mid+1
        elif x > arr[mid]:
            start = mid+2
        elif x < arr[mid]:
            end = mid-2
    return -1


if __name__ == '__main__':
    arr = [5, 10, 8, 15, 20]
    print(search(arr, 0, len(arr)-1, 20))
