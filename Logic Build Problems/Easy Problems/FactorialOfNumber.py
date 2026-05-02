def factorial(n):
    if n < 0: return 0
    if n == 0: return 1

    res = 1
    for i in range(2, n + 1):
        res *= i
    return res



if __name__ == "__main__":
    test_nums = [5, 4, 3, 2, 1, 0, -1]
    for num in test_nums:
        print(num, "factorial :", factorial(num))