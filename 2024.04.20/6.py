my_str = input()
answer = 'нет'
other = {0, 1}
my_set = set()
if my_str.startswith('0b'):
	try:
		my_set = set(int(x) for x in my_str[2:])
		if my_set <= other:
			print('да')
		else:
			print('нет')
	except ValueError:
		print('нет')
	
	
elif my_str.startswith('b'):
	try:
		my_set = set(int(x) for x in my_str[1:])
		if my_set <= other:
			print('да')
		else:
			print('нет')
	except ValueError:
		print('нет')
else: 
	try:
		my_set = set(int(x) for x in my_str)
		if my_set <= other:
			print('да')
		else:
			print('нет')
	except ValueError:
		print('нет')
	
	


# C:\Users\asu3\DS\Zabivalov\2024.04.20
 # 14:34:23 > python 6.py
# b11123
# нет


# C:\Users\asu3\DS\Zabivalov\2024.04.20
 # 14:34:29 > python 6.py
# b11111
# да


# C:\Users\asu3\DS\Zabivalov\2024.04.20
 # 14:34:33 > python 6.py
# bc00000
# нет


# C:\Users\asu3\DS\Zabivalov\2024.04.20
 # 14:34:41 > python 6.py
# bb11111
# нет


# C:\Users\asu3\DS\Zabivalov\2024.04.20
 # 14:34:46 > python 6.py
# 1234
# нет