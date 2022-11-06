def increment_number(list):
    if not (list[-1] + 1) % 10:
        list[-1] = 0
        for i in range(len(list) - 2,-1,-1):
            if (list[i] + 1) % 10:
                list[i] += 1
                break
            else:
                list[i] = 0
                if i == 0:
                    list.insert(0, 1)
    else:
        list[-1] += 1

    return list

test_list = [1, 2, 9]
test_result = increment_number(test_list)
print(test_result)