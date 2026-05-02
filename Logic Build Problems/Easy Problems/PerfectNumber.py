import math

def is_perfect_number(n):
    # smallest perfect number is 6
    if n < 6: return False

    sum = 1
    sqr = int(math.sqrt(n))
    for i in range(2, sqr + 1):
        if n % i == 0:
            if i * i != n: # ayni sayiyi iki kere eklemez
                # eger 28 / 2 = 14 ise hem 2 hem de 14 28'in bolenidir
                sum += i + n // i
            else:
                sum += i
    
    if n == sum:
        return True
    return False

if __name__ == "__main__":
    test_nums = [15, 6, 1, 2, 28, 496]
    for num in test_nums:
        print(num, "is perfect?", is_perfect_number(num))