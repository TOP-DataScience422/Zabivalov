import math


def orth_triangle(*, cathetus1: float = 0, cathetus2: float = 0 , hypotenuse: float = 0) -> float | None:
	""" Функция вычисляет третью сторону прямоугольного треугольника. """
	if (hypotenuse < cathetus1 or hypotenuse < cathetus2) and hypotenuse != 0:
		return print("Длина гипотенузы не может быть меньше длины катета")
	elif cathetus1 != 0 and cathetus2 != 0 and hypotenuse != 0: 
		return print("Все стороны известны")
	else:
		if hypotenuse == 0:
			hypotenuse = math.sqrt(cathetus1**2 + cathetus2**2)
			return print(hypotenuse)
		elif cathetus1  == 0:
			cathetus1 = math.sqrt(hypotenuse**2 - cathetus2**2)
			return print(cathetus1)
		elif cathetus2  == 0:
			cathetus2 = math.sqrt(hypotenuse**2 - cathetus1**2)
			return print(cathetus2)
		
orth_triangle(cathetus1=3, hypotenuse=5)
orth_triangle(cathetus1=8, cathetus2=15)
orth_triangle(cathetus2=9, hypotenuse=3)

# C:\Users\asu3\DS\Zabivalov\2024.04.21
 # 12:38:39 > python 6.py
# 4.0
# 17.0
# Длина гипотенузы не может быть меньше длины катета