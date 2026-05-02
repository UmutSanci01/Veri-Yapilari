def fact(n):
    if n == 0 or n == 1: return 1

    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def npr(n, r):
    if r < 0: return -1
    if r > n: return -1

    res = 1
    for i in range(r):
        res *= n - i

    # return fact(n) / fact(n-r)
    return res

if __name__ == "__main__":
    test_nums = [3, 4, 5]
    for num in test_nums:
        print(f"{num}!", fact(num))
    
    test_nums = [
        (5, 2), # 20
        (6, 3) # 120
    ]
    for n, r in test_nums:
        print(f"{n}, {r}", npr(n, r))
