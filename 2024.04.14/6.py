text = input('Введите билетик: ')


l1 = [int(l) for l in text[:3]]
l2 = [int(l) for l in text[3:]]

print('да' if sum(l1) == sum(l2) else 'нет')


# C:\Users\asu3\DS\Zabivalov\2024.04.14
 # 12:37:05 > python 6.py
# Введите билетик: 183534
# да


# C:\Users\asu3\DS\Zabivalov\2024.04.14
 # 12:37:10 > python 6.py
# Введите билетик: 401367
# нет