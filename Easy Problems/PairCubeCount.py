def pair_cube_count(n):
    count = 0

    # b^3 = n - a^3
    # eger i'nin kupu n'yi gecerse bu kosulu saglayacak b degeri yok
    for i in range(1, int(n ** (1/3)) + 1):
        cb = i ** 3
        diff = n - cb # b^3 = n - a^3
        if round(diff ** (1/3)) ** 3 == diff:
            count += 1
    
    return count

if __name__ == "__main__":
    test_nums = [9, 28]
    for num in test_nums:
        print(num, "cube count:", pair_cube_count(num))