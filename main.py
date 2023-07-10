# some_list = [1, 'hello', True, 5.43, [1,2,3], {1,2,3}]
#
# for el in some_list:
#     print(el)
#
# for ind in range(0, len(some_list)):
#     print(some_list[ind])
#
# # print(type(some_list))


# Вводится сначала количество чисел, потом сами числа, добавить их в список

# import random
# some_list = []
# count = int(input('Количество элементов: '))
# for _ in range(count):
#     number = random.randint(1, 10)
#     some_list.append(number)
# print(some_list)

# some_tuple = (1,2,3,4,5)

# some_set = {1,2,3}
# some_set.add(3)
# print(some_set)
#
# for i in some_set:
#     print(i)

# import random
# import time
# some_set = set()
# for _ in range(10 ** 6):
#     number = random.randint(1, 10 ** 6)
#     some_set.add(number)
#
# some_list = list(some_set)
#
# start = time.perf_counter()
# print(-1 in some_list)
# end = time.perf_counter()
# list_duration = end - start

# start = time.perf_counter()
# print(-1 in some_set)
# end = time.perf_counter()
# set_duration = end - start
# print(list_duration/set_duration)

# a = {1,2,3}
# b = {3,4,5}
# print(a.intersection(b))
# print(a.union(b))

# Задача 1

# some_list = []
# count = int(input('Введите количество чисел: '))
# for _ in range(count):
#     some_list.append((int(input())))
# k = int(input('Введите число для сдвига: '))
# print(some_list[k:] + some_list[:k])

# Задача 2

# some_list = []
# count = int(input("Введите количество чисел: "))
# for _ in range(count):
#     some_list.append(int(input()))
#
# res_count = 0
# for ind in range(0, count - 1):
#     if some_list[ind] < some_list[ind+1]:
#         res_count +=1
# print()
# print(res_count)

# Напишите программу, которая принимает на вход
# строку, и выводит количество повторов каждого символа
# Input: aaabcaadcdd
# Output: a: 5, b: 1, c: 2, d: 3

# some_str = input()
# for letter in set(some_str):
#     count = 0
#     for letter_1 in some_str:
#         if letter == letter_1:
#             count +=1
#     print(f"{letter}: {count}", end='  ')

# some_str = input()
# for letter in set(some_str):
#     print(f"{letter}: {some_str.count(letter)}", end= '  ')

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены пробелом. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# some_str = input()
# some_list = some_str.split()
# print(len(set(some_list)))

# some_str = input()
#
# word = ' '
# res_set = set()
# for letter in some_str:
#     if letter != ' ':
#         word += letter
#     else:
#         res_set.add(word.lower())
#         word = ' '
# if word:
#     res_set.add(word)
# print(len(res_set))

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# n1 = int(input('Введите количество элементов первого набора чисел: '))
# n2 = int(input('Введите количество элементов второго набора чисел: '))
# arr1 = []
# arr2 = []
# for i in range(n1):
#     arr1.append(int(input('Введите элемент первого массива: ')))
# for j in range(n2):
#     arr2.append(int(input('Введите элемент второго массива: ')))
# arr3 = []
# for i in arr1:
#     if i in arr2 and i not in arr3:
#             arr3.append(i)
# arr3.sort()
# print(arr3)

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# import random
# kust = int(input("введите количество кустов: "))
# berryes = list(random.randint(0, 10) for i in range(kust))
# result = []
# i = 0
# sum = 0
#
# print(berryes)
#
# while (i < kust):
#     if (i == kust - 1):
#         sum = berryes[i] + berryes[i - 1] + berryes[0]
#     else:
#         sum = berryes[i] + berryes[i - 1] + berryes[i + 1]
#         result.append(sum)
#         result.sort()
#     i += 1
#
# print(f"максимальное число ягод за одну итерацию {result[-1]}")