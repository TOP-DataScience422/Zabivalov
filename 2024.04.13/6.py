
ceil1 = input('Введите первую клетку: ')
ceil2 = input('Введите вторую клетку: ')


if 0 <= abs(int(ceil2[1]) - int(ceil1[1])) <=1 :
	if 0 <= abs(ord(ceil2[0]) - ord(ceil1[0])) <=1:
		print('Да')
	else:
		print('Нет')
else:
	print('Нет')
	
	
# C:\Users\Никита\DS\Zabivalov\2024.04.13
 # 23:27:59 > 6.py
# Введите первую клетку: d2
# Введите вторую клетку: c1
# Да


# C:\Users\Никита\DS\Zabivalov\2024.04.13
 # 23:28:08 > 6.py
# Введите первую клетку: d4
# Введите вторую клетку: c6
# Нет