def print_multiplication_table(n):
    print()
    print(n)
    for i in range(1, 11,):
        print(f"{n} * {i} = {n * i}")


if __name__ == "__main__":
    test = [5, 2, 4]
    for num in test:
        print_multiplication_table(num)