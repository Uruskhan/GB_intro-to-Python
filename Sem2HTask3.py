# Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

number = int(input("Введите число N: "))
list = [i for i in range(-number, number+1)]
print(list)
list_of_ind = [2, 2, 3, 1, 8]
comp = 1
for n in range(0, len(list_of_ind)-1):
    comp = comp * list[list_of_ind[n]]
print(comp) 
