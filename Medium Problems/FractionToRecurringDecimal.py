def find_fraction(a, b):
    if b == 0: return 0

    pattern = ''
    pattern_step = 0
    pattern_start = 0
    res = str(a/b)

    start = res.find('.') + 1
    front = res[:start]
    remain = res[start : ]

    pattern += remain[0]
    for i in range(1, len(remain)):
        if remain[i] == pattern[pattern_step]:
            pattern_start = i
            pattern_step += 1
        if i == pattern_start:
            return front + pattern[:pattern_start]

        pattern += remain[i]

    return front + pattern

if __name__ == "__main__":
    test_nums = [
        (1, 2),
        (50, 22),
        (101, 10),
        (2, 3)
    ]
    for a, b in test_nums:
        print(f"{a}/{b}={a/b}", find_fraction(a, b))