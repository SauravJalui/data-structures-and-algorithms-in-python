def BinarySearch(A, key):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2
        if key == A[mid]:
            return True
        elif key < A[mid]:
            high = mid - 1
        elif key > A[mid]:
            low = mid + 1
    return False

A = [15, 21, 47, 84, 96]
print(A)
found = BinarySearch(A, 96)
print("The element 96  is found ?: ", found)

