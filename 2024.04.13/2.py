number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))

if number1 % number2 == 0:
	print(f'{number1} делится на {number2} нацело', f'частное: {number1 // number2}', sep='\n')
else:
	print(f'{number1} не делится на {number2} нацело',
	f'неполное частное: {number1 // number2}',
	f'остаток: {number1 % number2}',
	sep='\n')
	
	
# Введите первое число: 10
# Введите второе число: 3
# 10 не делится на 3 нацело
# неполное частное: 3
# остаток: 1