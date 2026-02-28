def swap(a, b):
    return (b, a)


if __name__ == "__main__":
    test_sets = [
        (3, 5),
        (9, 4),
        (2, 12)
    ]

    for a, b in test_sets:
        print(f"({a}, {b}) => {swap(a, b)}")