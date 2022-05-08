def peak(arr, start, end):
    while start <= end:
        mid = start + (end-start) // 2
        if 0 < mid < len(arr)-1:
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid+1] > arr[mid]:
                start = mid+1
            elif arr[mid-1] > arr[mid]:
                end = mid-1
        elif mid == 0:
            return mid
        elif mid == len(arr)-1:
            return mid


if __name__ == '__main__':
    arr = [2, 8, 6, 4]
    print(peak(arr, 0, len(arr)-1))
