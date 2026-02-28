def sum_of_sqr(n):
    if n <= 0: return 0

    res = 0
    for i in range(n):
        res += (i + 1) ** 2
    return res

if __name__ == "__main__":
    for i in range(10):
        print(i, sum_of_sqr(i))