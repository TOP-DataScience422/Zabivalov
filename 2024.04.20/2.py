my_list = []
my_word = '1'
while True:
	my_word = input('')
	if my_word == '':
		break
	else:
		my_list.append(my_word)
if len(my_list) == 1:
	print(my_list[0])
else:
	print(', '.join(my_list[:-1]) + ' и ' + my_list[len(my_list) - 1])
	
	
# C:\Users\asu3\DS\Zabivalov\2024.04.20
 # 11:38:02 > python 2.py
# яблоко

# яблоко


# C:\Users\asu3\DS\Zabivalov\2024.04.20
 # 11:38:08 > python 2.py
# яблоко
# груша

# яблоко и груша


# C:\Users\asu3\DS\Zabivalov\2024.04.20
 # 11:38:16 > python 2.py
# яблоко
# груша
# апельсин

# яблоко, груша и апельсин


# C:\Users\asu3\DS\Zabivalov\2024.04.20
 # 11:38:27 > python 2.py
# яблоко
# груша
# апельсин
# лимон

# яблоко, груша, апельсин и лимон