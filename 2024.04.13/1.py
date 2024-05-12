number1 = float(input('Введите первое число '))
number2 = float(input('Введите второе число '))
number3 = float(input('Введите третье число '))
summ = 0
if number1 > 0:
	summ += number1
	if number2 > 0:
		summ += number2
		if number3 > 0:
			summ += number3
			print(f'Результат = {summ}')
		else:
			print(f'Результат = {summ}')
	else:
		if number3 > 0:
			summ += number3
		else:
			print(f'Результат = {summ}')
else:
	if number2 > 0:
		summ += number2
		if number3 >0:
			summ += number3
			print(f'Результат = {summ}')
		else:
			print(f'Результат = {summ}')
	else:
		if number3 > 0:
			summ += number3
			print(f'Результат = {summ}')
		else:
			print(f'Результат = {summ}')
			
			
# Введите первое число -2
# Введите второе число 3
# Введите третье число -6
# Результат = 3.0