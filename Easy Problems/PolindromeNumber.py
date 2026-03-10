def check_polindrome(n):
    digits = str(n)
    digits_reverse = digits[::-1]

    if digits == digits_reverse:
        return True
    return False

if __name__ == "__main__":
    test_nums = [12321, 1234, 11, 123]
    for num in test_nums:
        print(num, "is palindrome", check_polindrome(num))