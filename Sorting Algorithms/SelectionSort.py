def selectionsort(A):
    for i in range(len(A)-1, 0, -1):
        maxposition = 0
        for j in range(1, i + 1):
            if A[j] > A[maxposition]:
                maxposition = j
        A[i], A[maxposition] = A[maxposition], A[i]

A = [84, 21, 96, 15, 47] 
print("Original Array: ", A)
selectionsort(A)
print("Sorted Array: ", A)