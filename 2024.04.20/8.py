my_list = input('Введите имена файлов \n').split()
my_dict = {}
result_list = []
for elem in my_list:
	if elem.endswith(';'):
		elem = elem[:-1]
	if elem not in my_dict:
		my_dict[elem] = 1
	else:
		my_dict[elem] += 1

for x, y in my_dict.items():							
	if y > 1:
		for i in range(1, y + 1):						
			if i == 1:
				result_list.append(x)					
			else:
				index_point = x.find('.')
				my_word = x[:index_point] + '_' + str(i) + x[index_point:]
				result_list.append(my_word)
	else:
		result_list.append(x)
	
for elem in sorted(result_list):
	print(elem)
	
	
	# C:\Users\asu3\DS\Zabivalov\2024.04.20
 # 16:56:59 > python 8.py
# Введите имена файлов
# 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz


# 1.py
# 1_2.py
# 1_3.py
# aux.h
# functions.h
# main.cpp
# main_2.cpp
# main_3.cpp
# src.tar.gz
# src_2.tar.gz