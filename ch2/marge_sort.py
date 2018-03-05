def merge(A, p, q, r):
	n1 = q - p + 1
	n2 = r - q

	L = []
	R = []

	for i in range(0, n1):
		L.append(A[p+i])

	for j in range(0, n2):
		R.append(A[q+j])

	L.append(float('inf'))
	R.append(float('inf'))

	i = 1
	j = 1

	for k in range(p,r+1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i = i + 1
		else:
			A[k] = R[j]
			j = j + 1


import math
def merge_sort(A, p, r):

	if p < r:
		q = math.floor((p + r) / 2)
		merge_sort(A, p, q)
		merge_sort(A, q + 1, r)
		merge(A, p, q, r)
