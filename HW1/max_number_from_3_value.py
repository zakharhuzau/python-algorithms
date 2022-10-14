def max_number_from_3_value(a, b ,c):
    max = a

    if b > max:
        max = b
    if c > max:
        max = c

    print(f'max namber = {max}')


max_number_from_3_value(124, 21, 32)