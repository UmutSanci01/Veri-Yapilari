import GCD

def lcm(a, b):
    if a <= 0 or b <= 0: return 0
    
    # lcm(a,b) = |a.b| / gcd(a,b)
    return (a * b) // GCD.gcd(a, b)

if __name__ == "__main__":
    test_nums = [
        (10, 5),
        (5, 11),
        (34, 12) # 204
    ]
    for a, b in test_nums:
        print(a, b, "lcm:", lcm(a, b))