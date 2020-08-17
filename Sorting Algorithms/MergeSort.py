def mergesort(A):

    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]

        mergesort(left)
        mergesort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1

A = [84, 21, 96, 15, 47] 
print("Original Array: ", A)
mergesort(A)
print("Sorted Array: ", A)