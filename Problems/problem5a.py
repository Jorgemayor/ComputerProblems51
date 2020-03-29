import sys
sys.path.append('../')
from Methods import inversePowerMethod as ipm

def solve():
	matrix = [[6, 5, -5],
			  [2, 6, -2],
			  [2, 5, -1]]
	vector = [3, 7, -13]
	steps = 11
	print("\nSmallest eigenvalue:",ipm.apply(matrix, vector, steps))

if __name__ == "__main__":
    solve()
