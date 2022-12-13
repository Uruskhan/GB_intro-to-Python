# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
# Пример:
# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5

number = int(input("Введите натуральное число N: "))
lowest_nat_div = -1
for n in range(number, 1, -1):
    if number % n == 0:
        lowest_nat_div = n
print(lowest_nat_div)