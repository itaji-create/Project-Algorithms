def is_palindrome_iterative(word):
    drow = ''
    for item in word:
        drow = item + drow
    if drow != word or word == '':
        return False
    return True
