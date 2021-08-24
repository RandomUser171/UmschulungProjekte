def multiplication_table(rows, cols=None):
	if not cols:
		cols = rows
	spacing_width = len(str(rows*cols))+2
	print('{0:>{1}}'.format('|',spacing_width), end='')
	for i in range(1,cols+1):
		print('{0:>{1}}'.format(i,spacing_width),end='')
	print('\n' + '-' * ((cols + 1) * spacing_width + 1))
	for i in range(1,rows+1):
		print('{0:>{1}}'.format(str(i)+' |',spacing_width), end="")
		for x in range(1,cols+1):
			print('{0:>{1}}'.format(x*i, spacing_width), end='')
		print()




multiplication_table(50,5)