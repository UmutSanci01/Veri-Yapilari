def divisibility(num : str):
    digits = len(num)
    dif = 0
    positive = 0
    negative = 0
    for i in range(0, digits, 2):
        positive += int(num[i])
    
    for i in range(1, digits, 2):
        negative += int(num[i])
    
    dif = positive - negative
    if abs(dif) % 11 == 0:
        return True
    return False

if __name__ == "__main__":
    test_nums = [
        "76945",
        "7695",
        "1234567589333892",
    ]
    for num in test_nums:
        print(num, "divisibility", divisibility(num))