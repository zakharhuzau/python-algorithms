def even_first(list):
    swap_element = 0
    for i in range(len(list)):
        if not list[i] % 2:
            list[i], list[swap_element] = list[swap_element], list[i]
            swap_element += 1

    return list


test_list = [7, 3, 5, 6, 4, 10, 3, 2]
test_result = even_first(test_list)
print(test_result)