import numpy as np

def apply(matrixArr, vector, steps):
	np.set_printoptions(precision=5)
	x = np.array(vector)
	matrix = np.array(matrixArr)
	print("Step 0\n  vector:",x)
	
	r=None
	for i in range(1, steps+1):
		y = matrix.dot(x)
		r = np.amax(np.abs(y))/np.amax(np.abs(x))
		x = y/np.amax(y)
		print("\nStep",i,"\n  Vector:",x,"\n  Eigenvalue:",r)
	return r
