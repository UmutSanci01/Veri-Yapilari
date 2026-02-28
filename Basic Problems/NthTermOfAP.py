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

    for a1, a2, n in test_sets:
        print(f"a1 {a1} a2 {a2} n {n} = {find_nth_term(a1, a2, n)}")