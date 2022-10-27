def split_in_half(string):
    count = len(string)
    if count % 2 == 0:
        return string[int(count / 2):] + string[:int(count / 2)]
    else:
        return string[int(count / 2) + 1:] + string[:int(count / 2) + 1]


test_string = 'bbbbbcaaaaa'
print(split_in_half(test_string))