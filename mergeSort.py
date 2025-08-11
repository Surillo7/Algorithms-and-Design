def merge_Sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left_side = merge_Sort(arr[:mid])
    right_side = merge_Sort(arr[mid:])

    return merge(left_side, right_side)
