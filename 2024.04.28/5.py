def logger(func: 'function') -> 'function':
	"""Функция декоратор. Выводит в стандартный поток вывода название функции, позиционные и ключевые аргументы. Также выводится результат выполнения функции или исключение."""
	def wrapper(*args, **kwargs):
		result = ''
		result += func.__name__ + '('
		for i in args:
			result += str(i) + ', '
		if kwargs:
			for i,j in kwargs.items():
				result += f'{i}={j}' + ', '
			result = result[:-2] + ') -> '
		else:
			for a,b in func.__kwdefaults__.items(): 
				result += f'{a}={b}'
			result += ') -> '
			
		try:
			result += str(func(*args, **kwargs))
			print(result)
			print(str(func(*args, **kwargs)))
		except Exception as exp:
			result = result[:-3] + '.. ' + str(type(exp)).strip("<>class' ") + f': {exp}'
			print(result)
		
	return wrapper
	

def my_func(num1, num2, *, digits=0):
	return round(num1 / num2, digits)
	

# C:\Users\asu3\DS\Zabivalov\2024.04.28
 # 11:00:24 > python -i 5.py
# >>> my_func = logger(my_func)
# >>> my_func(1, 3, digits=2)
# my_func(1, 3, digits=2) -> 0.33
# 0.33
# >>> my_func(7,2)
# my_func(7, 2, digits=0) -> 4.0
# 4.0
# >>> my_func(5, 0)
# my_func(5, 0, digits=0) .. ZeroDivisionError: division by zero
# >>>
