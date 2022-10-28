def below_arithmetical_mean(list):
    arithmetical_mean = sum(list) / len(list)
    list_result = []
    for l in list:
        if l < arithmetical_mean:
            list_result.append(l)
    return list_result


test_list = [1, 3, 5, 6, 4, 10, 2, 3]
result = below_arithmetical_mean(test_list)
print(result)