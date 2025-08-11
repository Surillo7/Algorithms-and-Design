def merge_sort(arr):
    if len(arr) <= 1:  # Base case for recursion
        return arr
    mid = len(arr) // 2  # Find the middle index

    # Recursively sort the left and right halves
    left_side = merge_sort(arr[:mid])
    right_side = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_side, right_side)


def merge(left, right):
    result = []  # Initialize the result list
    i = j = 0  # Pointers to traverse left and right lists

    # Compare elements from both halves and merge them
    # in sorted order
    # take elements from both lists and append the
    # smaller one to the result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # If there are remaining elements in either list,
    # append them to the result
    result.extend(left[i:])
    result.extend(right[j:])
    return result
