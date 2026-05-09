def rotate_array(arr : list, d):
    n = len(arr)
    d %= n

    temp = []

    for i in range(d):
        temp = arr[-d:]
    
    for i in temp:
        pass
    
    return temp

if __name__ == "__main__":
    test_arrs = [
        ([1, 2, 3, 4, 5, 6], 2),
        ([1, 2, 3], 4)
    ]
    for arr, d in test_arrs:
        print(rotate_array(arr, d))
        # print(arr[:], "rotated", rotate_array(arr, d))