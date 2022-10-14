def sum_of_digits(n):
    sum = 1

    for i in range(2, n + 1):
        sum += i

    print(f'sum = {sum}')


sum_of_digits(5)