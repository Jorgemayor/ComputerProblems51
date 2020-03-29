import sys
sys.path.append('../')
from Methods import powerMethod as pm

def solve():
	matrix = [[6, 5, -5],
			  [2, 6, -2],
			  [2, 5, -1]]
	vector = [1, 2, 3]
	steps = 100
	pm.apply(matrix, vector, steps)

if __name__ == "__main__":
    solve()
