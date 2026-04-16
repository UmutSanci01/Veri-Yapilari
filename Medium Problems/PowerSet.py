def power_set(s, k = 0):
    subs = []
    n = len(s)
    if k < n:
        subs.append(power_set(s, k + 1))

    if k <= 0:
        subs.append('')
        return subs

    # k = 3 n = 4
    for i in range(0, n):
        if k + i > n:
            break
        subs.append(s[i:k+i])

    return subs    


if __name__ == "__main__":
    test_string = [
        "ab", # "", "a", "b", "ab"
        "abc", # "", "a", "b", "c", "ab", "bc", "ac", "abc"
        "a" # "", "a"
    ]
    for string in test_string:
        print(power_set(string))
        