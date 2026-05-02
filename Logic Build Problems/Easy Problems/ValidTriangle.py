def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

if __name__ == "__main__":
    test_edges = [
        (7, 10, 5),
        (1, 10, 12),
        (0, 0, 0),
        (3, 4, 5),
        (5, 12, 13),
        (8, 8, 8)
    ]

    for a, b, c in test_edges:
        print(a, b, c, check_triangle(a, b, c))