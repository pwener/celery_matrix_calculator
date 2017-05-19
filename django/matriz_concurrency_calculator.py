from celery import Celery
from NoConMaMu.tasks import calculate_line

app = Celery(
    'NoConMaMu',
    broker='amqp://guest@localhost//',
)

# Code calculator here

def read_matrix(matrix_file):
	f = open(matrix_file, 'r')

	lines = [map(int, line.split(' ')) for line in f if line.strip() != '\n']
	lines = [list(l) for l in lines]

	return lines

def print_matrix(M):
	[print(element) for element in M]

if __name__ == '__main__':
	# Sample 3x3
	A = read_matrix('NoConMaMu/input/A.matrix')


	# Sample 3x4
	B = read_matrix('NoConMaMu/input/B.matrix')

	R = []

	for A_line in A:
		result = calculate_line.delay(A_line, B)
		while not result.ready():
			sleep(0.5)
		R.append(result.get())

	print_matrix(R)
