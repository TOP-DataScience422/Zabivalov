number = int(input('Введите число: '))
result = 0
for i in range(1, number // 2 + 1) :
	if number % i == 0:
		result += i

result += number
print(result)


# Введите число: 49
# 57