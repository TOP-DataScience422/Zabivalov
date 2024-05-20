text = 'грузите апельсины бочках братья карамазовы'
format_text = ''
a = ' '
for i in text:
	if i != a:
		format_text += i
		
print(f'{len(format_text) * 30 // 100 } руб.', f'{len(format_text) * 30 % 100 } коп.')

# C:\Users\asu3\DS\Zabivalov\2024.04.14
 # 11:03:25 > python 5.py
# 11 руб. 40 коп.