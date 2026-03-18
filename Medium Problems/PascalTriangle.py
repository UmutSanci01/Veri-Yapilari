def print_triangle(n):
    last_row = []
    for row in range(n):
        arr = []
        for i in range(row+1):
            if i == 0 or i == row:
                arr.append(1)
            else:
                arr.append(
                    last_row[i - 1] + last_row[i]
                )
        last_row = arr
        print(arr)

if __name__ == "__main__":
    print_triangle(6)