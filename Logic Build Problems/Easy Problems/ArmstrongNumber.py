def check_armstrong(x):
    if x <= 0: return False
    
    sum = 0
    temp = x
    digits = str(x)
    n = len(digits)
    digit = 0

    for i in digits:
        sum += pow(int(i), n)
    # for i in range(n):
    #     digit = temp % 10
    #     temp //= 10

    #     sum += pow(digit, n)
    
    if sum == x:
        return True
    
    return False


if __name__ == "__main__":
    test_nums = [153, 9474, 123]
    for num in test_nums:
        print(num, "is Armstrong Number", check_armstrong(num))