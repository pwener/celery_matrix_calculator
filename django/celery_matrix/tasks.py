from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time

# Multiply line of A by column of B
# A lenght should be equals to B lenght
def calculate_element(A_line, B_column):
	if len(A_line) != len(B_column):
		raise ValueError("A lenght(%d) is not equals to B lenght(%d)" % (len(A_line), len(B_column)))
	else:
		final_element = 0

		for i in range(len(A_line)):
				final_element += A_line[i] * B_column[i]

		return final_element

# Given a line of matrix A, multiplied by another matrix B,
# we have a new row of matrix.
@shared_task
def calculate_line(A_line, B):
	new_line = []

	column_number = len(B[0])

	for column in range(column_number):
		element = calculate_element(A_line, [c[column] for c in B])
		new_line.append(element)

	return new_line

def read_matrix(matrix_file):
	f = open(matrix_file, 'r')

	lines = [map(int, line.strip().split(' ')) for line in f if line.strip() != '\n']
	lines = [list(l) for l in lines]

	return lines

def print_matrix(M):
	[print(element) for element in M]

def print_matrix_result():
	start = time.time()

	A = read_matrix('celery_matrix/input/A.matrix')

	B = read_matrix('celery_matrix/input/B.matrix')

	R = []

	results = []

	for A_line in A:
		# Save one async task
		results.append(calculate_line.delay(A_line, B))

	# Iterate into async tasks and get result
	for result in results:
		while not result.ready():
			pass
		R.append(result.get())

	end = time.time()

	print_matrix(R)

	print("Executed in %.3f sec", end-start)
