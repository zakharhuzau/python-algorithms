def insertion_sort(list):
    n = len(list)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if list[j] > list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
            else:
                break
    return list

test_list = [3, 1, 4, 2]
print(insertion_sort(test_list))