def find_max_crossing_subarray(A, low, mid, high):

	left-sum = -floot('inf')
	sum = 0
	for i in range(mid,low-1, -1):
		sum = sum + A[i]
		if sum > left-sum
		left-sum = sum
		max-left = i

	right-sum = -floot('inf')
	sum = 0
	for j in range(mid+1,high+1):
		sum = sum + A[j]
		if sum > right-sum:
			right-sum = sum
			max-right = j

	return [max-left, max-right, left-sum + right-sum]

import math

def find_maximum_subarray(A, low, high):
	if high == low:
		return [low, high, A[low]]

	else:
		mid = floor((low + high) / 2)

		left-maximum = find_maximum_subarray(A, low, mid)
		right-maximum = find_maximum_subarray(A, mid + 1, high)
		cross-maximum = find_max_crossing_subarray(A, low, mid, high)

		if left-maximum[3] >= right-maximum[3] and left-maximum[3] >= cross-maximum[3]:
			return left-maximum
		elif right-maximum[3] >= left-maximum[3] and right-maximum[3] >= cross-maximum[3]:
			return right-maximum
		else:
			return cross-maximum

