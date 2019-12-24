A = [5,2,4,6,1,3] #indexing from 0

def insertion_sort(A):
	for j in range(1,len(A),1):
		key = A[j] #black element
		i = j - 1
		while (i >= 0 and A[i] > key): #all grey elements
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key
	return A

sorted_A = insertion_sort(A)
print(sorted_A)