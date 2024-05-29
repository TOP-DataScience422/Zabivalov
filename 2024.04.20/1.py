my_str = input()

pos_1 = my_str.find("@")
pos_2 = my_str.find('.')
if pos_1 != -1 and pos_2 > pos_1:
	print('да')
else:
	print('нет')
	
# C:\Users\asu3\DS\Zabivalov\2024.04.20
  # 9:41:06 > python 1.py
 # sgd@ya.ru
# да


# C:\Users\asu3\DS\Zabivalov\2024.04.20
 # 11:23:06 > python 1.py
 # sg.d@yaru
# нет


# C:\Users\asu3\DS\Zabivalov\2024.04.20
 # 11:23:15 > python 1.py
 # sgd@yaru
# нет