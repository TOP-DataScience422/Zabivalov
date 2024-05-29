list1 = input().split()
list2 = input().split()
answer = 'Нет'

for i in range(0, len(list1)):
	if list1[i:i + len(list2)] == list2:
		answer = 'Да'
		break
		
print(answer)
	
	
# C:\Users\asu3\DS\Zabivalov\2024.04.20
 # 11:51:17 > python 3.py
# 1 2 3 4
# 1 2
# да


# C:\Users\asu3\DS\Zabivalov\2024.04.20
 # 11:51:27 > python 3.py
# 1 2 3 4
# 2 4
# Нет
