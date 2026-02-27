def swap(a, b):
    return (b, a)


if __name__ == "__main__":
    a, b = 3, 5
    print(a, b)
    a, b = swap(a, b)
    print(a, b)