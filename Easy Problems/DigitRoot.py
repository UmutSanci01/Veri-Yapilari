def root_of_digit(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    
    if sum // 10 == 0:
        return sum
    else:
        return root_of_digit(sum)

if __name__ == "__main__":
    test_nums = [1234, 5674]
    for num in test_nums:
        print(num, "root digit", root_of_digit(num))