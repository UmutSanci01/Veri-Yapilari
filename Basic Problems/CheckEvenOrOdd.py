def check_even(n):
    if n % 2 == 0: return True
    return False

if __name__ == "__main__":
    print(2, check_even(2))
    print(4, check_even(4))
    print(6, check_even(6))
    print(5, check_even(5))
    print(8, check_even(8))
    print(11, check_even(11))