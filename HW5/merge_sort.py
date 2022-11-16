def merge_sort(part_one, part_two):
    i = j = 0
    merge_list = []
    while i < len(part_one) or j < len(part_two):
        if i == len(part_one):
            merge_list.append(part_two[j])
            j += 1
            continue
        if j == len(part_two):
            merge_list.append(part_one[i])
            i += 1
            continue
        if part_one[i] <= part_two[j]:
            merge_list.append(part_two[j])
            j += 1
        else:
            merge_list.append(part_one[i])
            i += 1
    return merge_list

def split_list(list):
    n = len(list)
    mid = n // 2
    if n < 2: return list
    return merge_sort(split_list(list[:mid]), split_list(list[mid:]))


test_list = [5, 3, 1, 6, 4, 2, 7]
print(split_list(test_list))