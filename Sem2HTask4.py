# Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

number = int(input("Введите число N: "))
sum_of_even_num = 0
for n in range(1, number + 1, 1):
    if n % 2 == 0:
        sum_of_even_num = sum_of_even_num + n
print(sum_of_even_num)