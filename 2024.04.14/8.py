number = int(input('Введите число: '))
a1 = 1
a2 = 0

fibb_list = []
for i in range(1, number + 1):
	if number == 1 or number == 2:
		fibb = 1
	else:
		fibb = a1 + a2
		a1 = a2
		a2 = fibb
		
	fibb_list += [fibb]
		
print(*fibb_list)
	
	
# C:\Users\asu3\DS\Zabivalov\2024.04.14
  # 9:37:34 > python 8.py
# Введите число: 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597


# C:\Users\asu3\DS\Zabivalov\2024.04.14
  # 9:37:57 > python 8.py
# Введите число: 1
# 1


# C:\Users\asu3\DS\Zabivalov\2024.04.14
  # 9:38:26 > python 8.py
# Введите число: 2
# 1 1


# C:\Users\asu3\DS\Zabivalov\2024.04.14
  # 9:38:30 > python 8.py
# Введите число: 3
# 1 1 2


# C:\Users\asu3\DS\Zabivalov\2024.04.14
  # 9:38:32 > python 8.py
# Введите число: 4
# 1 1 2 3


# C:\Users\asu3\DS\Zabivalov\2024.04.14
  # 9:38:35 > python 8.py
# Введите число: 5
# 1 1 2 3 5