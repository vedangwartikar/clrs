#Exercises

#2.1-1
def insertion_sort(A):
	for j in range(1,len(A),1):
		key = A[j] #black element
		i = j - 1
		while (i >= 0 and A[i] > key): #all grey elements
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key
	return A

#2.1-2
def reverse_insertion_sort(A):
	for j in range(1,len(A),1):
		key = A[j]
		i = j - 1
		while (i >= 0 and A[i] < key):
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key
	return A

#2.1-3
def linear_search(A, v):
	for i in A:
		if i == v:
			return A.index(i)
	return None

#2.1-4
def add_binary(x, y):
	length = len(x)
	carry = 0
	z = [0]*(length+1)
	for i in range(length-1,-1,-1):
		print(carry, x[i], y[i])
		if carry is 0:
			if (x[i] == 0 and y[i] == 0):
				z[i+1] = 0
				carry = 0
			elif (x[i] == 1 and y[i] == 1):
				z[i+1] = 0
				carry = 1
			elif (x[i] == 0 and y[i] == 1):
				z[i+1] = 1
				carry = 0
			elif (x[i] == 1 and y[i] == 0):
				z[i+1] = 1
				carry = 0
		elif carry is 1:
			if (x[i] == 0 and y[i] == 0):
				z[i+1] = 1
				carry = 0
			elif (x[i] == 1 and y[i] == 1):
				z[i+1] = 1
				carry = 1
			elif (x[i] == 0 and y[i] == 1):
				z[i+1] = 0
				carry = 1
			elif (x[i] == 1 and y[i] == 0):
				z[i+1] = 0
				carry = 1
		print(z[i])
	if carry == 1:
		z[0] = 1
	print(z)

A = [31, 41, 59, 26, 41, 58]
sorted_A = insertion_sort(A)
print(sorted_A)

A = [31, 41, 59, 26, 41, 58]
reverse_sorted_A = reverse_insertion_sort(A)
print(reverse_sorted_A)

print(linear_search(A, 31))

x = [1,1,1]
y = [1,1,1]

add_binary(x, y)
