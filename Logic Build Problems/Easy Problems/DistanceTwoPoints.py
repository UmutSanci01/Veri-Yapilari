import math

def distance_two_points(p1 : set, p2 : set):
    d = math.sqrt(
        (p2[0] - p1[0]) ** 2 +
        (p2[1] - p1[1]) ** 2
    )

    return round(d, 5)

if __name__ == "__main__":
    test_points = [
        (
            (3, 4), (7, 7)
        ),
        (
            (3, 4), (4, 3)
        )
    ]

    for p1, p2 in test_points:
        print(f"p1{p1}, p2{p2} distance {distance_two_points(p1, p2)}")