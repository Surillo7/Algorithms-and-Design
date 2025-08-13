def sort_and_count(arr):
    if len(arr) <= 1:  # Base case for recursion
        return arr
    mid = len(arr) // 2  # Find the middle index

    # Recursively sort the left and right halves
    left_side = sort_and_count(arr[:mid])
    right_side = sort_and_count(arr[mid:])

    # Merge the sorted halves
    return merge_and_count(left_side, right_side)


def merge_and_count(left, right):
    count = 0  # Initialize inversion count
    result = []  # Initialize the result list
    i = j = 0  # Pointers to traverse left and right lists

    # Compare elements from both halves and merge them
    # in sorted order
    # take elements from both lists and append the
    # smaller one to the result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            # Count inversions
            # An inversion occurs when an element in the left
            # half is greater than an element in the right half
            count += len(left[i:])
    # If there are remaining elements in either list,
    # append them to the result
    result.extend(left[i:])
    result.extend(right[j:])
    return result, count


# Test script to demonstrate the merge_sort function
if __name__ == "__main__":
    sample_list = [38, 27, 43, 3, 9, 82, 10]
    sorted_list, inversions = sort_and_count(sample_list)
    print(f"Sorted list: {sorted_list}")
    print(f"Number of inversions: {inversions}")
