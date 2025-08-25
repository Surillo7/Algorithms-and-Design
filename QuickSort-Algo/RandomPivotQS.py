import random


def quicksort(arr, low, high):
    # Base case for recursion,
    # when the subarray has 1 or 0 elements, or sorted
    if low < high:
        # Partition the array and get pivot
        pi = partition(arr, low, high)

        # Recursively sort left and right side of pivot
        quicksort(arr, low, pi - 1)  # leftside
        quicksort(arr, pi + 1, high)  # rightside


def partition(arr, low, high):
    random_index = random.randint(low, high)  # select a random pivot

    # Swap random pivot with last index, we just swap locations
    # not pivot value
    arr[random_index], arr[high] = arr[high], arr[random_index]
    pivot = arr[high]
    i = low - 1  # Index of leftside of pivot boundary

    # Loop through the array
    for j in range(low, high):
        if arr[j] <= pivot:  # compare value with pivot
            i += 1  # increment boundary position
            arr[i], arr[j] = arr[j], arr[i]  # swap elements
    # swap pivot with boundary
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the final position of the pivot
