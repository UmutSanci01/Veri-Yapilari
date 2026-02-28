def find_nth_term(a1, a2, n):
    pattern = a2 - a1
    first_term = a1
    for i in range(1, n):
        first_term += pattern
    return first_term

if __name__ == "__main__":
    test_sets = [
        (2, 3, 4),
        (1, 3, 10)
    ]

    for set in test_sets:
        a1 = set[0]
        a2 = set[1]
        n = set[2]
        print(f"a1 {a1} a2 {a2} n {n} = {find_nth_term(a1, a2, n)}")