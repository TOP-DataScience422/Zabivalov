dict_base ={
'0': 0,
'1': 1,
'2': 2,
'3': 3,
'4': 4,
'5': 5,
'6': 6,
'7': 7,
'8': 8,
'9': 9,
'a': 10,
'b': 11,
'c': 12,
'd': 13,
'e': 14,
'f': 15,
'g': 16,
'h': 17,
'i': 18,
'j': 19,
'k': 20,
'l': 21,
'm': 22,
'n': 23,
'o': 24,
'p': 25,
'q': 26,
'r': 27,
's': 28,
't': 29,
'u': 30,
'v': 31,
'w': 32,
'x': 33,
'y': 34,
'z': 35,
}


def base(number: str, base: int) -> str:
	""" Функция возвращает искомое число """
	result = ''
	num = int(number)
	while num != 0:
		k = num % base
		for a,b in dict_base.items():
			if k == b:
				result += a
		num = num // base
	return result[::-1]

def base10(number: str, base: int) -> str:
	""" Функция возвращает число в 10 системе счисления """
	return str(int(number, base))


def int_base(number: str, base1: int, base2: int) -> str:
	""" Функция перевода из одной системы счисления в другую """
	return base(base10(number, base1), base2)
	
	
print(int_base('1101010', 2, 30))
print(int_base('ff00', 16, 2))


# C:\Users\asu3\DS\Zabivalov\2024.04.21
  # 9:19:09 > python 7.py
# 3g
# 1111111100000000