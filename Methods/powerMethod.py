import numpy as np

def apply(matrixArr, vector, steps):
	np.set_printoptions(precision=5)
	x = np.array(vector)
	matrix = np.array(matrixArr)
	print("Step 0\n  vector:",x)

	for i in range(1, steps+1):
		y = matrix.dot(x)
		r = np.amax(y)/np.amax(x)
		x = y/np.amax(y)
		print("\nStep",i,"\n  vector:",x,"\n  EigenValue:",r)
