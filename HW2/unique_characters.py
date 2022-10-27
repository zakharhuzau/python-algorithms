def unique_characters(string):
    unique = set()
    for char in string:
        if char not in unique:
            unique.add(char)
        else:
            return False
    return True

test_string = 'abcde'
print(unique_characters(test_string))