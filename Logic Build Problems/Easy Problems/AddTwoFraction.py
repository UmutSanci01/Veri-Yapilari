import LCM

def add_two_fraction(a, b):
    lcm = LCM.lcm(a[1], b[1])

    num = (a[0]) * (lcm // a[1]) + (b[0]) * (lcm // b[1])
    common_factor = LCM.GCD.gcd(num, lcm)

    numerator = num // common_factor
    denominator = lcm // common_factor

    return (numerator, denominator)

if __name__ == "__main__":
    test_fractions = [
        (
            (1, 2), (3, 2) # 2, 1
        ),
        (
            (1, 3), (3, 9) # 2, 3
        ),
        (
            (1, 5), (3, 15) # 2, 5
        )
    ]

    for a, b in test_fractions:
        print(f"{a}+{b}={add_two_fraction(a, b)}")