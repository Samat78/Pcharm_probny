# a = int(input('Машина проезжает за день: '))
# b = int(input('Нужно проехать: '))
# c = round(b / a, 1)
# print(f'Потребуется {c} дней')

# dist_per_day = 700
# total_dist = 750
# days = ((total_dist + dist_per_day - 1) // dist_per_day)
# print(days)

# Задача №7. Решение в группах
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# a = int(input())
# if a % 4 == 0 and a % 100 != 0:
#     print('YES')
# elif a % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# year = int(input('Введите год: '))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("YES")
# else:
#     print("NO")

# number = float(input('Введите значение:  '))
# if (number * 10) % 2 == 0:
#    print('None')
# else:
#       print(int(number * 10) % 10)



# Домашнее задание
# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# number = int(input('Введите число:  '))
# result = (1 + 2 + 3)
# print(result)
#
# number = int(input('Введите число:  '))
# result = (1 + 0 + 0)
# print(result)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

# s = int(input('ведите число: '))
# print((s//6), ((s//6)*4), (s//6))

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# n = str(input('Введите числа:  '))
# sum1 = int(n[0]) + int(n[1]) + int(n[2])
# sum2 = int(n[3]) + int(n[4]) + int(n[5])
# if sum1 == sum2:
#   print("YES")
# else:
#   print("NO")
#

# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> n

# n = int(input('Введите данные: '))
# m = int(input('Введите данные: '))
# k = int(input('Введите данные: '))
# if k < n * m and ((k % n == 0 or k % m == 0)):
#     print('YES')
# else:
#     print('NO')