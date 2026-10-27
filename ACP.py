
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


def reverse_in_groups(arr, k):
    for i in range(0, len(arr), k):
        arr[i:i + k] = arr[i:i + k][::-1]
    return arr


def left_rotate_by_one(arr):
    if len(arr) > 0:
        first = arr.pop(0)
        arr.append(first)
    return arr


def left_rotate_by_n(arr, n):
    if len(arr) > 0:
        n = n % len(arr)
        arr[:] = arr[n:] + arr[:n]
    return arr


def find_leaders(arr):
    leaders = []
    max_right = float('-inf')

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] >= max_right:
            leaders.append(arr[i])
            max_right = arr[i]

    leaders.reverse()
    return leaders


# Main program
scores = list(map(int, input("Enter scores separated by spaces: ").split()))

print("Original scores:", scores)

print("Reversed scores:", reverse_array(scores.copy()))

k = int(input("Enter group size k: "))
print("Reversed in groups:", reverse_in_groups(scores.copy(), k))

print("Left rotation by 1:", left_rotate_by_one(scores.copy()))

n = int(input("Enter rotation count n: "))
print("Left rotation by n:", left_rotate_by_n(scores.copy(), n))

print("Leaders in scores:", find_leaders(scores))
