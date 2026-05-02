# days of week dictionary

# Output the result as an integer (0 = Sunday, 1 = Monday, ..., 6 = Saturday)
days = {
   0 : "Sunday",
   1 : "Monday",
   2 : "Tuesday",
   3 : "Wednesday",
   4 : "Thursday",
   5 : "Friday",
   6 : "Saturday"
}

def day_of_week(d, m, y):
    t = [ 0, 3, 2, 5, 0, 3,
          5, 1, 4, 6, 2, 4 ]
    y -= m < 3
    return (( y + int(y / 4) - int(y / 100)
             + int(y / 400) + t[m - 1] + d) % 7)

if __name__ == "__main__":
    test_dates = [
        (30, 8, 2010), # Monday
        (15, 6, 1995), # Thursday
        (29, 2, 2016), # Monday
    ]
    for d, m, y in test_dates:
        print(d, m, y, "day of week", days[day_of_week(d, m, y)])