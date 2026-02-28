def closest_number(n, m):
    if m == 0: return 0

    closest = 0
    min_difference = abs(m) + 1 # uzaklik en fazla sayinin kendisi olabilir
    offset = abs(m)

    for i in range(n - offset, n + offset + 1):
        # n etrafindaki sayilari yazdir
        #print(i)

        if i % m == 0:
            diff = abs(n - i)
            # i ve m arasindaki uzakligi yazdir
            #print(i, m, diff)
            
            # if diff <= min_difference: # esitlik durumunda mutlak degeri kucuk olan sayiyi verir 
            if diff < min_difference: # esitlik durumunda mutlak degeri buyuk olan sayiyi verir
                min_difference = diff
                closest = i
    return closest



if __name__ == "__main__":
    test_sets = [
        (13, 4), # 12
        (-15, 6), # -18
        (0, 5), # 0
        (13, 1), # 13
        (5, 0), # 0
        (-15, 10) # -20
    ]

    for set in test_sets:
        n = set[0]
        m = set[1]
        print(f"({n}, {m})", closest_number(n, m))