def is_anagram(first_string, second_string):
    first_array = [i for i in first_string.lower()]
    second_array = [i for i in second_string.lower()]

    quick_sort(first_array, 0, len(first_array) - 1)
    quick_sort(second_array, 0, len(second_array) - 1)
    if first_array != second_array:
        # print("not anagram")
        return False
    # print("anagram")
    return True


def quick_sort(numbers, start, end):
    if start < end:
        p = partition(numbers, start, end)
        quick_sort(numbers, start, p - 1)
        quick_sort(numbers, p + 1, end)


def partition(numbers, start, end):
    pivot = numbers[end]
    delimiter = start - 1

    for index in range(start, end):
        if numbers[index] <= pivot:
            delimiter = delimiter + 1
            numbers[index], numbers[delimiter] = numbers[delimiter], numbers[index]

    numbers[delimiter + 1], numbers[end] = numbers[end], numbers[delimiter + 1]

    return delimiter + 1
