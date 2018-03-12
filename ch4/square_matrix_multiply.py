import numpy as np


def square_matrix_multiply(A,B):
	n = np.size(A,0)
	C = np.empty([n, n]).fill(0)

	for i in range(1, n+1):
		for j in range(1, n+1):
			for k in range(1, n+1):
			C[i][j] = C[i][j] + A[i][k] * B[k][j]

	return C
