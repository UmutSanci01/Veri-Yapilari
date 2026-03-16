def kthDigit(a, b, k):
    num = a ** b
    digit = 0
    res = 0
    while digit < k:
        if digit + 1 == k:
            res = num % 10
        num //= 10
        digit += 1
    return res

if __name__ == "__main__":
    test_nums = [
        (3, 3, 1),
        (5, 2, 2)
    ]
    for a, b, k in test_nums:
        print(f"{a}^{b}", "k-th digit", kthDigit(a, b, k))