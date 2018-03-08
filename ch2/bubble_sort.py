def bubble_sort(A):
	for i in range(0, A.length - 2):
		for j in range(A.length, i, -1):
			if A[j] < A[j-1]:
				A[j],A[j-1] = A[j-1], A[j]