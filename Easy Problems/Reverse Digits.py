def reverse_digits(n):
    digits = str(n)
    redigits = digits[::-1]

    return int(redigits)

if __name__ == "__main__":
    test_nums = [123, 200, 12345]
    for num in test_nums:
        print(num, "Reversed:", reverse_digits(num))