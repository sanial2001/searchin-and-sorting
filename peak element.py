def peak(arr, start, end):
    if len(arr) == 1:
        return arr[0]
    while start <= end:
        mid = start + (end-start) // 2
        if 0 < mid < len(arr)-1:
            if arr[mid] >= arr[mid-1] and arr[mid] >= arr[mid+1]:
                return arr[mid]
            elif arr[mid+1] > arr[mid]:
                start = mid+1
            elif arr[mid-1] > arr[mid]:
                end = mid-1
        elif mid == 0:
            if arr[mid] > arr[mid+1]:
                return arr[mid]
            else:
                return arr[mid+1]
        elif mid == len(arr)-1:
            if arr[mid] > arr[mid-1]:
                return arr[mid]
            else:
                return arr[mid-1]


if __name__ == '__main__':
    arr = [20, 40, 35, 30]
    print(peak(arr, 0, len(arr)-1))
