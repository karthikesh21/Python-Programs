def rotate_array(arr, d):
    n = len(arr)
    d = d % n  # In case d > n
    return arr[d:] + arr[:d]

# Input
arr = list(map(int, input("Enter array elements separated by space: ").split()))
d = int(input("Enter number of positions to rotate: "))

rotated = rotate_array(arr, d)
print("Rotated array:", rotated)
