def insertion_sort(array: list) -> list:
    for i in range(1, len(array)):
        key_value = array[i]
        j = i - 1

        while j >= 0 and array[j] > key_value:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_value

    return array
