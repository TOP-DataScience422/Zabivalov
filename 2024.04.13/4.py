ceil1 = input('Введите первую клетку: ')
ceil2 = input('Введите вторую клетку: ')

color1 = ''
color2 = ''
if ord(ceil1[0]) % 2 == 0:
	if int(ceil1[1]) % 2 == 0:
		color1 = 'b'
	else:
		color1 = 'w'
else:
	if int(ceil1[1]) % 2 == 0:
		color1 = 'w'
	else:
		color1 = 'b'
if ord(ceil2[0]) % 2 == 0:
	if int(ceil2[1]) % 2 == 0:
		color2 = 'b'
	else:
		color2 = 'w'
else:
	if int(ceil2[1]) % 2 == 0:
		color2 = 'w'
	else:
		color2 = 'b'

if color1 == color2:
	print('да')
else:
	print('нет')
	
	
# Введите первую клетку: a8
# Введите вторую клетку: g1
# b b
# да


# C:\Users\Никита\DS\Zabivalov\2024.04.13
 # 23:07:26 > 4.py
# Введите первую клетку: a7
# Введите вторую клетку: b4
# b b
# да