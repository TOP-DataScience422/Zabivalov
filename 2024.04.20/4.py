my_dict = {}
print('Введите ключ - значение\n')
while True:
	a = input()
	if a == '':
		break
	else:
		my_list = a.split(' ')
		my_dict[my_list[0]] = my_list[1]
		
answer = '! value error !'
search_str = input('Введите значение для которого необходим ключ\n')
for i,j in my_dict.items():
	if j == search_str:
		answer = i

print(answer)


# C:\Users\asu3\DS\Zabivalov\2024.04.20
 # 12:53:06 > python 4.py
# Введите ключ - значение

# 1 a
# 2 b
# 3 c
# 4 d

# Введите значение для которого необходим ключ
# c
# 3


# C:\Users\asu3\DS\Zabivalov\2024.04.20
 # 12:53:21 > python 4.py
# Введите ключ - значение

# 1 a
# 2 b
# 3 c

# Введите значение для которого необходим ключ
# d
# ! value error !