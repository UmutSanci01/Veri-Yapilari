from ComputenPr import fact

def ncr(n, r):
    if r < 0: return 0
    if r > n: return 0

    # kombinasyon işlemi her zaman tam sayı üretirmiş
    return fact(n) // (fact(r) * fact(n - r)) 

if __name__ == "__main__":
    test_nums = [
        (5, 2), # 10
        (2, 4), # 0
        (5, 0) # 1
    ]
    for n, r in test_nums:
        print(n, r, "nCr", ncr(n, r))