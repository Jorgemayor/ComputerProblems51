from Problems import problem1 as p1
from Problems import problem2 as p2
from Problems import problem3 as p3
import sys

def main():

	try:
		option=sys.argv[1]
	except:
		option=None

	if option == None:
		print("Módulo desarrollado para resolver la sección computer problems del capítulo 5.1\n")
		print("Para resolver el problema 1, pasar como argumento el número 1\n")
		print("Para resolver el problema 4.a, pasar como argumento el número 2\n")
		print("Para resolver el problema 5.a, pasar como argumento el número 3\n")
	elif option == "1":
		p1.solve()
	elif option == "2":
		p2.solve()
	elif option == "3":
		p3.solve()
	else:
		print("Opción inválida.")
	exit(0)

if __name__ == "__main__":
    main()
