def merge(A, p, q, r):
	n1 = q - p + 1
	n2 = r - q

	L = []
	R = []

	for i in range(0, n1):
		L.append(A[p+i])

	for j in range(0, n2):
		R.append(A[q+j])

	i = 1
	j = 1

	for k in range(p,r+1):
		if i > L.length:
			A[k:] = R[j:]
			break

		if j > R.length:
			A[k:] = L[i:]
			break


		if L[i] <= R[j]:
			A[k] = L[i]
			i = i + 1
		else:
			A[k] = R[j]
			j = j + 1

