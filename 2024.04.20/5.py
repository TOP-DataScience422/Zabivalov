scores_letters = {
    1: 'АВЕЁИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

my_word = input('Введите слово: ')
score = 0

for letter in my_word:
	for i,j in scores_letters.items():
		if letter.upper() in j:
			score += int(i)
			
			
print(score)


# C:\Users\asu3\DS\Zabivalov\2024.04.20
 # 12:57:32 > python 5.py
# Введите слово: синхрофазатрон
# 29