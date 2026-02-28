def check_overlapping(l1, r1, l2, r2):
    # tamemen yukarida ya da asagida ya da solunda ya da sagindaysa asla kesismez
    if l1[0] > r2[0] or r1[0] < l2[0] or l2[1] < r1[1] or r2[1] > l1[1]:
        return False
    
    return True

if __name__ == "__main__":
    test_sets = [
        (
            (0, 10), (10, 0), (5, 5), (15, 0)
        ),
        (
            (0, 10), (10, 0), (-10, 5), (-1, 0)
        )
    ]

    for l1, r1, l2, r2 in test_sets:
        print(l1, r1, l2, r2, check_overlapping(l1, r1, l2, r2))