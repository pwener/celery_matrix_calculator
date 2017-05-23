# Runs without concurrency one matrix product

def read_matrix(matrix_file):
	f = open(matrix_file, 'r')

	lines = [map(int, line.strip().split(' ')) for line in f if line.strip() != '\n']
	lines = [list(l) for l in lines]

	return lines

def print_matrix(M):
	[print(element) for element in M]

# Sample 3x3
A = read_matrix('input/A.matrix')


# Sample 3x4
B = read_matrix('input/B.matrix')

# Result is 3x4
R = [[0 for x in range(len(A))] for y in range(len(B[0]))]


for i in range(len(A)):
	# New matriz have same quantity of Y rows
	for j in range(len(B[0])):
		for k in range(len(B)):
			R[i][j] += A[i][k] * B[k][j]


print_matrix(R)

print("Runs %d operations" % (2*len(A)*len(B[0])))
