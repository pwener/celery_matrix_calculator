from __future__ import absolute_import, unicode_literals
from celery import shared_task
from time import sleep

# Multiply line of A by column of B
# A lenght should be equals to B lenght
def calculate_element(A_line, B_column):
	if len(A_line) is not len(B_column):
		raise ValueError("A lenght is not equals to B lenght")
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

        lines = [map(int, line.split(' ')) for line in f if line.strip() != '\n']
        lines = [list(l) for l in lines]

        return lines

def print_matrix(M):
        [print(element) for element in M]

def print_matrix_result():
        # Sample 3x3
        A = read_matrix('celery_matrix/input/A.matrix')

        # Sample 3x4
        B = read_matrix('celery_matrix/input/B.matrix')

        R = []

        for A_line in A:
                result = calculate_line.delay(A_line, B)
                while not result.ready():
                        pass
                R.append(result.get())

        print_matrix(R)
