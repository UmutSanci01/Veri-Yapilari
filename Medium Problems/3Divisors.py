def divisors(n):
    res = []
    for i in range(1, n + 1):
        count = 0
        for k in range(1, i + 1):
            if i % k == 0:
                count += 1
                if count > 3:
                    break
        if count == 3:
            res.append(k)
    return res

if __name__ == "__main__":
    test_nums = [16, 100]
    for num in test_nums:
        print(num, divisors(num))