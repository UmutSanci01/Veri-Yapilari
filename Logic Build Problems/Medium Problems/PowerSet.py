def power_set(s):
    sonuc = []

    def back_tracking(yol : str, index):
        sonuc.append(yol) # yol : str türünde olduğundan kopyasını değil doğrudan kendisini ekleriz.

        for i in range(index, len(s)):
            yol += s[i]
            # power_set(s, yol, i+1, sonuc)
            back_tracking(yol, i + 1)
            yol = yol[:-1]
    
    back_tracking("", 0)
    return sonuc


if __name__ == "__main__":
    test_sets = [
        "ab",
        "abc",
        "a"
    ]
    for s in test_sets:
        print(s, power_set(s))