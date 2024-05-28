def list_edit(numbers: list, n: int = 1, is_copy: bool = False) -> list | None:
	""" Функция удаляет n макс и мин чисел в списке """
	for _ in range(n):
		numbers.remove(max(numbers))
		numbers.remove(min(numbers))
	if is_copy:
		edit_sample = numbers.copy()
		return  edit_sample
		
	else:
		return sample



sample = [1, 2, 3, 4, 5, 6, 7]
edit_sample = list_edit(sample, 2, is_copy = True)


# C:\Users\asu3\DS\Zabivalov\2024.04.21
 # 15:11:57 > python -i 3.py
# >>> id(sample)
# 2060170483840
# >>> id(edit_sample)
# 2060170481920
# >>> sample
# [3, 4, 5]
# >>> edit_sample
# [3, 4, 5]
# >>> sample is edit_sample
# False