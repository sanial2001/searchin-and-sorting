def solve(arr, m, t, start, end):
    result = 0
    while start <= end:
        mid = start + (end-start) // 2
        if is_valid(arr, m, mid):
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result


def is_valid(arr, m, mid):
    sum_val, student = 0, 1
    for val in arr:
        sum_val = sum_val + val
        if sum_val > mid:
            student = student + 1
            sum_val = val
    if student == m:
        return True
    else:
        return False


def min_pages(arr, m):
    sum_ele = sum(arr)
    t = [i for i in range(sum_ele+1)]
    return solve(arr, m, t, 0, len(t)-1)


if __name__ == '__main__':
    arr = [250, 74, 159, 181, 23, 45, 129, 174]
    m = 6
    print(min_pages(arr, m))
