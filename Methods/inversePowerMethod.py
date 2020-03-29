from . import powerMethod as pw
import numpy as np

def apply(matrixArr, vector, steps):
	matrix = np.array(matrixArr)
	invertedMatrix = np.linalg.inv(matrix)
	u = pw.apply(invertedMatrix, vector, steps)
	r = 1/u
	return r
