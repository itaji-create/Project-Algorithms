def is_anagram(first_string, second_string):
    first_string = order_string(first_string)
    second_string = order_string(second_string)

    if first_string != second_string:
        # print("not anagram")
        return False
    # print("anagram")
    return True


def order_string(string):
    _array = [i for i in string.lower()]

    _length = len(_array)
    for order in range(_length - 1):
        for item in range(0, _length - 1 - order):
            if _array[item] > _array[item + 1]:
                current_letter = _array[item]
                _array[item] = _array[item + 1]
                _array[item + 1] = current_letter
    # print(_array)

    return _array
