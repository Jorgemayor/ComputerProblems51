# Computer Problems 5.1

Este módulo es desarrollado completamente con el fin de resolver los problemas de computación propuestos en el taller de la asignatura Análisis y Métodos Numéricos.

Este taller se conforma por los puntos 1, 4.a y 5.a, de la sección Computer Problems, del capítulo 5.1 del libro Numerical Analysis, escrito por David R. Kincaid y E. Ward Cheney.

## Tecnologías usadas para el desarrollo

* [Python 3.7](python.org) - Lenguaje de programación
* [Numpy](numpy.org) - Librería de Python

## Estructura

La distribución de archivos viene dada por:

* main.py: Archivo principal
* Methods: Acá están implementados todos los métodos usados
	- powerMethod.py
	- inversePowerMethod.py
* Problems: Acá se encuentran los problemas que se solucionaron
	- problem1.py
	- problem4a.py
	- problem5a.py

## Instalar el módulo

Asegurarse de tener instalado python 3.7 y numpy en su sistema.

```bash
# Se clona el repositorio
git clone https://github.com/Jorgemayor/ComputerProblems51.git
```

## Ejecución

Desde el directorio *ComputerProblems51*, se pueden escribir los siguientes comandos en la terminal para interactuar con el módulo:

```bash
# Para obtener información general
python3 main.py

# Para ejecutar el punto 1
python3 main.py 1

# Para ejecutar el punto 4.a
python3 main.py 2

# Para ejecutar el punto 5.a
python3 main.py 3
```

También es posible ejecutar cada problema individualmente. Estando en el directorio *Problems*, se ejecutan de la forma:

```bash
# Para ejecutar el problema 1
python3 problem1.py

# Para ejecutar el problema 4.a
python3 problem4a.py

# Para ejecutar el problema 5.a
python3 problem5a.py
```

## Desarrollador

* **Jorge Eduardo Mayor Fernández** - [Jorgemayor](github.com/Jorgemayor)
