def two_lowest_elements(list):
    list.sort()
    # return f'{list[0]}, {list[1]}'
    return list[:2]

def two_lowest_elements2(list):
    min = list[0]
    last_min = 0
    for i in range(1, len(list)):
        if min > list[i]:
            last_min = min
            min = list[i]
    return [min, last_min]


test_list =  [198, 3, 4, 9, 10, 9, 2]
result = two_lowest_elements(test_list)
print(result)
test_list2 = [198, 3, 4, 9, 10, 9, 2]
result2 = two_lowest_elements2(test_list2)
print(result2)