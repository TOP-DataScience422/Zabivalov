year = int(input('Введите год: '))


if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
	print(f'{year} год високосный')
else:
	print(f'{year} год не високосный')
	
	
# C:\Users\Никита\DS\Zabivalov\2024.04.13
 # 22:26:16 > 3.py -i
# Введите год: 2005
# 2005 год не високосный


# C:\Users\Никита\DS\Zabivalov\2024.04.13
 # 22:26:25 > 3.py -i
# Введите год: 2012
# 2012 год високосный