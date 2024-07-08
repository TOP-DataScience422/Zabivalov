def repeat(func: 'function') -> 'function':
	""" Функция декоратор """
	def wrapper(num: int=2, *args, **kwargs):
		""" Функция обертка """
		for _ in range(num):
			func(*args, **kwargs)
	return wrapper
@repeat	
def testing_function():
	print('python')
	

testing_function()
print('-'*20)
testing_function(5)


# C:\Users\asu3\DS\Zabivalov\2024.04.28
  # 9:21:48 > python 4.py
# python
# python
# --------------------
# python
# python
# python
# python
# python