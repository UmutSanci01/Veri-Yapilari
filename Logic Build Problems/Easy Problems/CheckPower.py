def check_power(x, y):
    if x == 0: return y == 0
    if x == 1: return y == 1 # x^0 = 1
    if y <= 0: return False

    while y % x == 0:
        y //= x

    return y == 1

if __name__ == "__main__":
    test_sets = [
        (10, 1),
        (10, 1000),
        (10, 1001),
        (1, 2),
        (10, 0),
        (0, 5)
    ]

    for x, y in test_sets:
        print(f"({x},{y})", check_power(x, y))