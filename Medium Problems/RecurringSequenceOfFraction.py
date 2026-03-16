def find_recurring(a, b):
    if b == 0: return "Zero Division Error"
    if a == 0: return 0

    remainders = {}
    res = [a//b, '.']
    rem = a % b
    while rem != 0:
        if rem in remainders:
            start_index = remainders[rem]
            return ''.join(res[start_index : ])
        remainders[rem] = len(res)
        rem *= 10
        res.append(str(rem//b))
        rem = rem % b
    return "No Recurring Secuence"

if __name__ == "__main__":
    test_nums = [
        (1, 2),    # 0.5
        (50, 22),  # 2.2(72) -> 72 tekrar eder
        (101, 10), # 10.1
        (2, 3),    # 0.(6)
        (1, 6),    # 0.1(6) -> Koda takla attıran o meşhur örnek
        (1, 17),
        (989, 12),
        (1, 7)     # 0.(142857) -> Float limitlerini aşan efsanevi uzun desen
    ]
    for a, b in test_nums:
        print(a, b, "Recurring Sequence is", find_recurring(a, b))