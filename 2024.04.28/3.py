def math_function_resolver(func: 'function', *x: float, res_to_str: bool = False) -> list:
	""" Функция вычисляет округленные значения для различных математических функций и возвращает список  """
	result_list = list(map(func, x))
	if res_to_str:
		result_list = list(map(lambda x: str(round(x)), result_list))
	else:
		result_list = list(map(lambda x: round(x), result_list))
	
			
	return result_list


print(math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10)))
print(math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10)))
print(math_function_resolver(lambda x: 2.72**x, *range(1, 10), res_to_str=True))


# C:\Users\asu3\DS\Zabivalov\2024.04.28
 # 14:56:32 > python 3.py
# [2, 3, 4, 4, 4, 5, 6, 6, 6]
# [2, 1, 0, 0, 0, -1, -2, -2, -2]
# ['3', '7', '20', '55', '149', '405', '1101', '2996', '8149']