def exchange_sort_v1(array: list) -> list:
    for i in range(len(array)):
        for j in range(len(array)):
            if i < j and array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array


def exchange_sort_v2(array: list) -> list:  # optimized
    for i in range(0, len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array
