def nth_fibonacci(n):
    if n <= 1: return n

    terms = [0, 1]
    sum = 0
    for i in range(2, n + 1):
        sum = terms[0] + terms[1]
        terms[0], terms[1] = terms[1], sum
    
    return sum

if __name__ == "__main__":
    for num in range(-2, 10):
        print(f"{num}th fibonacci is", nth_fibonacci(num))