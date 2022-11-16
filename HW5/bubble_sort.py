def bubble_sort(list):
    n = len(list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if list[j] < list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

test_list = [3, 1, 4, 2]
print(bubble_sort(test_list))