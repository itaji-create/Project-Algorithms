def is_palindrome_recursive(word, low_index, high_index):
    # try:
    if len(word) > 100:
        raise RecursionError
    if word == '':
        return False
    while low_index < high_index:
        if word[low_index] != word[high_index]:
            print("not recursive")
            return False
        low_index += 1
        high_index -= 1

    return True


is_palindrome_recursive('', 0, len('')-1)
