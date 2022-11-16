def selection_sort(list):
    max_index = 0
    n = len(list)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if list[max_index] < list[j]:
                max_index = j
        list[max_index], list[i] = list[i], list[max_index]
        max_index = i + 1
    return list

test_list = [3, 1, 4, 2]
print(selection_sort(test_list))
