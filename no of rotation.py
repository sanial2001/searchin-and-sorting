def solve(arr, start, end):
    while start <= end:
        n = len(arr)
        mid = start + (end - start) // 2
        prev = (mid-1+n) % n
        next = (mid+1) % n
        if arr[mid] < arr[prev] and arr[mid] < arr[next]:
            return mid
        elif arr[start] < arr[end]:
            return start
        elif arr[mid] > arr[end]:
            start = mid + 1
        elif arr[mid] < arr[start]:
            end = mid - 1


if __name__ == '__main__':
    arr = [2, 5, 7, 11, 12, 15, 18]
    print(solve(arr, 0, len(arr)-1))
