def check_even(n):
    if n % 2 == 0: return True
    return False

if __name__ == "__main__":
    test = [2, 4, 6, 5, 8, 11]
    for num in test:
        print(num, check_even(num))