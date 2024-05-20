n = int(input('Введите число разрядов: '))
a = "9" * n
summ = 0
for i in range(int('1'+ (n - 1) *'0'), int(a) + 1):
	b = 2
	while b <= i:
		if b == i:
			summ += 1
			break
		elif i % b == 0:
			break
		b += 1
		
print(summ)

		


# C:\Users\asu3\DS\Zabivalov\2024.04.14
 # 10:23:13 > python 4.py
# Введите число разрядов: 3
# 143


# C:\Users\asu3\DS\Zabivalov\2024.04.14
 # 10:23:15 > python 4.py
# Введите число разрядов: 4
# 1061