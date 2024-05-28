import math


def central_tendency(num1: float, num2: float, *numbers: float) -> dict[str, float]:
	""" Функция вычисляет основные меры центральной тенденции """
	result = {}
	my_list = sorted([num1, num2, *numbers], reverse=True)
	if len(my_list) % 2 != 0:
		number_m = int((len(my_list) + 1) / 2)
		median = my_list[number_m - 1]
	else:
		a = int(len(my_list) / 2)
		c = int(len(my_list) / 2 + 1)
		median = (my_list[a - 1] + my_list[c - 1]) / 2
		
	arithmetic = sum(my_list) / len(my_list)
	geometric = math.pow(math.prod(my_list), 1 / len(my_list))
	harmonic = len(my_list) / sum(i ** -1 for i in my_list)
	result = {'median':median, 'arithmetic': arithmetic, 'geometric': geometric, 'harmonic': harmonic}
		
	return result
		
		
		
print(central_tendency(1, 2, 3, 4))
print(central_tendency(1, 2, 3, 4, 5))
print(central_tendency(8, 4, 1, 6, 9, 2))
print(central_tendency(1, 10, 3, 88, 6, 4, 99))


# C:\Users\asu3\DS\Zabivalov\2024.04.21
 # 11:16:17 > python 5.py
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.92}
# {'median': 3, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}
# {'median': 5.0, 'arithmetic': 5.0, 'geometric': 3.888322594479331, 'harmonic': 2.7870967741935484}
# {'median': 6, 'arithmetic': 30.142857142857142, 'geometric': 9.355442580204022, 'harmonic': 3.7403859128322763}



