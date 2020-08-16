def BinarySearch(A, key, low , high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if key == A[mid]:
            return True
        elif key < A[mid]:
            return BinarySearch(A, key, low, mid - 1)
        elif key > A[mid]:
            return BinarySearch(A, key, mid + 1, high)

A = [15, 21, 47, 96, 84]
B = A.sort()
print(A)
found = BinarySearch(A, 84, 0, 5)
print("The element 84 is found? ", found)