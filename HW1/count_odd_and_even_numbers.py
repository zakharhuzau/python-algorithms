def count_odd_and_even_numbers(n):
    even = odd = 0
    evens = []
    odds = []

    for i in str(n):
        if int(i) % 2 == 0:
            even += 1
            evens.append(int(i))
        else:
            odd += 1
            odds.append(int(i))

    print(f'number is {n}, then {even} digits will be even {evens} and {odd} odd digits {odds}')


count_odd_and_even_numbers(34560)