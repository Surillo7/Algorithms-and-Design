def sort_and_count(arr):
    if len(arr) <= 1:  # Base case for recursion
        return arr, 0
    mid = len(arr) // 2  # Find the middle index

    # Recursively sort the left and right halves, and
    # count inversions in each half
    left_side, left_count = sort_and_count(arr[:mid])
    right_side, right_count = sort_and_count(arr[mid:])
    # Merge the sorted halves and count inversions
    merged_array, split_count = merge_and_count(left_side, right_side)
    # add the counts from both halves and the split count
    total_count = left_count + right_count + split_count

    return merged_array, total_count


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


def read_integer_file(filename):
    # Reads a file with one integer per line and
    # returns a list of integers.
    numbers = []
    with open(filename) as f:
        for line in f:
            # .strip() removes whitespace/newlines,
            # int() converts the string to a number.
            numbers.append(int(line.strip()))
    return numbers


# Test script to demonstrate the merge_sort function
if __name__ == "__main__":

    input_file = "/Users/king/Programming/ResumeRepo/AI-Specialization/Algorithms-and-Design/Inversion-Assignment/IntegerArray.txt"

    print(f"Reading integers from {input_file}...")
    numbers = read_integer_file(input_file)

    print("Counting inversions... ")
    sorted_numbers, inversion_count = sort_and_count(numbers)

    print(f"Number of inversions: {inversion_count}")
