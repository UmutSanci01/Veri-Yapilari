def find_leaders(arr):
    leaders = []
    temp = arr
    while len(temp) > 0:
        greater, index = find_greater(temp)
        leaders.append(greater)
        temp = temp[index + 1: ]
    return leaders

def find_greater(arr):
    greater = 0
    index = 0
    for i in range(len(arr)):
        if arr[i] > greater:
            greater = arr[i]
            index = i
    
    return (greater, index)

if __name__ == "__main__":
    test_arr = [
        [16, 17, 4, 3, 5, 2],
        [1, 2, 3, 4, 5, 2]
    ]
    for arr in test_arr:
        print(arr, find_leaders(arr))