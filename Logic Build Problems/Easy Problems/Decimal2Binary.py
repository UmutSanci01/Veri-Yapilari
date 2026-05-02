def dec2bin(decimal):
    output = ''
    while decimal > 0:
        mb = decimal % 2 # mb = decimal & 1
        decimal //= 2 # decimal >>= 1

        output += str(mb)
    
    return output[::-1]


if __name__ == "__main__":
    test_nums = [12, 33]
    for num in test_nums:
        print(num, "=>", dec2bin(num))