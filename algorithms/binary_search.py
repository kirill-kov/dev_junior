def binary_search(value: int, array: list) -> int:
    low = 0
    high = len(array)

    while low <= high:
        mid = (low + high) // 2

        if value == array[mid]:
            return mid

        if value > array[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_recursive(value: int, array: list, low: int, high: int) -> int:
    if low > high:
        return -1

    mid = (low + high) // 2
    if value == array[mid]:
        return mid

    if value > array[mid]:
        return binary_search_recursive(value, array, mid + 1, high)
    else:
        return binary_search_recursive(value, array, low, mid - 1)
