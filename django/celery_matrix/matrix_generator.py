import sys
from random import randint


# Order is the lenght of matrix
# Mininum order accept is 4
def create_matrix(filename, order=4):
	with open(filename, 'w') as out:
		for line in range(0, order):
			for matrix in range(0, order):
				out.write('%d ' % randint(0, 1000))
			out.write('\n')

if __name__ == '__main__':
	# Name of new file with matrix
	filename = sys.argv[1]

	try:
		# Order of matrix
		order = int(sys.argv[2])

		create_matrix(filename, order)

		print("Generating one matrix %dx%d\n" % (order, order))
		print("New file %s created" % filename)
	except ValueError:
		print("Ops! You need run: python3 matrix_generator.py <filename> <matrix_order>")
		print("filename is the name of your file matrix")
		print("matrix_order is lenght of matrix")
