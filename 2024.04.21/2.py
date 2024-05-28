def taxi_cost(distance: int, waiting_time: int = 0) -> int | None:
	""" Функция расчёта стоимости поездки в такси """
	price = 0
	price_distance = round(distance / 150 * 6, 0)
	price_time = waiting_time * 3
	if distance > 0 and waiting_time >= 0:
		price = int(round(80 + price_time + price_distance , 0))
		return price
	elif distance == 0 and waiting_time >= 0:
		price = int(round(80 + price_time + 80, 0))
		return price
	else:
		return None
		
		
		


print(taxi_cost(1500))
print(taxi_cost(2560))
print(taxi_cost(0, 5))
print(taxi_cost(42130, 8))
print(taxi_cost(-300))


# C:\Users\asu3\DS\Zabivalov\2024.04.21
 # 11:31:20 > python 2.py
# 140
# 182
# 175
# 1789
# None