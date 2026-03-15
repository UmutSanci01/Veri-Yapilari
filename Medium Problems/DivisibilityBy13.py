def divisibility(num : str):
    # string boyutu 3'un kati olmali
    num += '0' * (3 - len(num) % 3)

    res = 0
    block_num = len(num) // 3
    for i in range(block_num):
        block = int(num[-3 : ])
        if i % 2:
            res -= block
        else:
            res += block
        num = num[ : -3]
    if res % 13: return False
    return True

"""
    # Stores running remainder
    rem = 0  

    # Process each digit and compute remainder modulo 13
    for ch in s:
        rem = (rem * 10 + int(ch)) % 13

    # Final check for divisibility
    return rem == 0
"""

if __name__ == "__main__":
    test_nums = [
        "2911285",
        "27",
    ]
    for num in test_nums:
        print(num, "divisibility", divisibility(num))