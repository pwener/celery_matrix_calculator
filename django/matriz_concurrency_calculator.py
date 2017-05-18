import os
from NoConMaMu.tasks import calculate_line

# Code calculator here

def read_matrix(matrix_file):
	f = open(matrix_file, 'r')

	lines = [map(int, line.split(' ')) for line in f if line.strip() != '\n']
	lines = [list(l) for l in lines]

	return lines

def print_matrix(M):
	[print(element) for element in M]

if __name__ == '__main__':
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')


	# Sample 3x3
	A = read_matrix('NoConMaMu/input/A.matrix')


	# Sample 3x4
	B = read_matrix('NoConMaMu/input/B.matrix')

	R = []

	for A_line in A:
		result_line = calculate_line.delay(A_line, B)
		print(result_line.get())


	print_matrix(R)
