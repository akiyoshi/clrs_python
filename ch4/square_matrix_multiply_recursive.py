import numpy as np

def square_matrix_multiply_recursive(A,B):
	n = np.size(A,0)
	C = np.empty([n, n]).fill(0)

	if n == 1:
		C[0,0] = A[0,0]B[0,0]
	else:
		m = n/2
		C[:m,:m] = square_matrix_multiply_recursive(A[:m,:m],B[:m,:m])
		C[:m,m:] = square_matrix_multiply_recursive(A[:m,m:],B[:m,m:])
		C[m:,:m] = square_matrix_multiply_recursive(A[m:,:m],B[m:,:m])
		C[m:,m:] = square_matrix_multiply_recursive(A[m:,m:],B[m:,m:])

	return C
