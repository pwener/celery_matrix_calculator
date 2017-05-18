# Code calculator here

# Sample 3x3
X = [[12, 7, 3],
	[4, 5, 6],
	[7, 8, 9]]


# Sample 3x4
Y = [[5, 8, 1, 2],
	[6, 7, 3, 0],
	[4, 5, 9, 1]]

# Result is 3x4
R = [[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0]]


for i in range(len(X)):
	# New matriz have same quantity of Y rows
	for j in range(len(Y[0])):
		for k in range(len(Y)):
			R[i][j] += X[i][k] * Y[k][j]

for r in R:
	print(r)


