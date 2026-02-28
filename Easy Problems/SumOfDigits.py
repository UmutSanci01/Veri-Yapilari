def sum_of_digits(n):
    if n == 0: return 0

    num = n
    digit = 0
    sum = 0
    while num > 0:
        digit = num % 10
        num = num // 10 # divides and rounds down
        sum += digit
    
    return sum

if __name__ == "__main__":
    test_nums = [687, 12, 123]
    for num in test_nums:
        print(num, "sum of digits:", sum_of_digits(num))