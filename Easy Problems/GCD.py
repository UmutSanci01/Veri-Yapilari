def gcd(a, b):
    a, b = abs(a), abs(b)

    while b > 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    test_nums = [
        (20, 28),
        (60, 36)
    ]
    for a, b in test_nums:
        print(a, b, "GCD is", gcd(a, b))