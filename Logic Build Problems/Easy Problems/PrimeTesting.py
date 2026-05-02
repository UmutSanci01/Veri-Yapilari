import math
import random

def check_prime(n):
    if n <= 1 or n % 2 == 0: return False

    root = int(math.sqrt(n)) + 1
    for i in range(3, root):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    test_nums = [11, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # test_nums = [random.randint(0, 1000) for x in range(100)]
    for num in test_nums:
        print(num, "is prime?", check_prime(num))