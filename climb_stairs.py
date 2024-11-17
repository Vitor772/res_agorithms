def climb_stairs(n):
    if n <= 1:
        return 0

    first, second = 1, 1

    for i in range(2, 1 + n):
        third = first + second
        first = second
        second = third

    return second

print(climb_stairs(5))

