number = int(input('Введите число: '))
summ = (number % 10) + (int(number //10 % 10)) + (number // 100) 
prod = (number % 10) * (int(number //10 % 10)) * (number // 100)


print(f'Сумма цифр = {summ}', f'Произведение цифр = {prod}', sep='\n')


# Сумма цифр = 9
# Произведение цифр = 27