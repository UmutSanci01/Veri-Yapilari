def power_set(s : str, yol : str, index = 0, sonuc : list = []):
    sonuc.append(yol[:])

    for i in range(index, len(s)):
        yol += s[i]
        power_set(s, yol, i+1, sonuc)
        yol = yol[:-1]
    
    return sonuc


if __name__ == "__main__":
    test_sets = [
        "ab",
        "abc",
        "a"
    ]
    for s in test_sets:
        print(s, power_set(s, ""))