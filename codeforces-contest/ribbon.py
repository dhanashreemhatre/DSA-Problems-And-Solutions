t = int(input())
while t:
    n_cell = int(input())
    chips = list(map(int, input().split()))

    # Find the index of the first and last chip
    first_chip_index = next(i for i, x in enumerate(chips) if x == 1)
    last_chip_index = next(i for i, x in enumerate(reversed(chips)) if x == 1)
    last_chip_index = n_cell - 1 - last_chip_index

    # Count zeros between the first and last chip
    count = sum(1 for i in range(first_chip_index, last_chip_index) if chips[i] == 0)

    print(count)

    t -= 1
