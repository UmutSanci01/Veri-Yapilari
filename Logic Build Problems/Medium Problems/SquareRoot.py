import math

def square(n):
    if n <= 0: return 0

    sqr = 1
    while sqr ** 2 <= n:
        sqr += 1

    return math.floor(sqr - 1)


if __name__ == "__main__":
    test_nums = [i for i in range(20)]
    for num in test_nums:
        print(num, "sqr", square(num))