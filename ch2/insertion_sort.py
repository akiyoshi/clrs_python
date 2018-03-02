def insertion_sort(A):

	if len(A) == 1:
		return A

	for j in range(1, len(A):
		key = A[i]
		i = j - 1

		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key

	return A
		
