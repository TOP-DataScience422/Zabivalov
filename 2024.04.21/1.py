import string


def letters(password: str) -> bool:
""" Функция поиска верхнего и нижнего регистра """
	if not password.islower() and not password.isupper():
		return True
	else:
		return False
		
		
def digits(password: str) -> bool:
""" Функция поиска чисел в пароле"""
	summ_digit = 0
	for p in password:
		if p.isdigit():
			summ_digit += 1
	if summ_digit >= 2:
		return True
	else:
		return False



def punctuation(password: str) -> bool:
""" Функция поиска спец символов """
	for p in password:
		if p in string.punctuation:
			return True
			


def strong_password(password: str) -> bool:
	""" Функция проверки пароля на прочность"""
	if len(password) >= 8 and punctuation(password) and digits(password) and letters(password):
		return print(True)
	else:
		return print(False)
		


strong_password('aP3:kD_l3')
strong_password('password')
strong_password('passwoRD2222')

# C:\Users\asu3\DS\Zabivalov\2024.04.21
 # 11:06:39 > python 1.py
# True
# False
# False