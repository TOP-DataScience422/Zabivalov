def countable_nouns(number: int, my_tuple: tuple[str, str, str]) -> str:
	""" Функция возвращает существительное соответствующее числу number """
	if number % 10 == 1 and number != 11:
		return my_tuple[0]
	elif number % 10 == 2 and number != 12 or number % 10 == 3 and number != 13 or number % 10 == 4 and number != 14:
		return my_tuple[1]
	else:
		return my_tuple[2]
		
		


print(countable_nouns(1, ('год', 'года', 'лет')))
print(countable_nouns(2, ('год', 'года', 'лет')))
print(countable_nouns(10, ('год', 'года', 'лет')))
print(countable_nouns(12, ('год', 'года', 'лет')))
print(countable_nouns(22, ('год', 'года', 'лет')))


# C:\Users\asu3\DS\Zabivalov\2024.04.21
  # 8:34:37 > python 4.py
# год
# года
# лет
# лет
# года