# # # # # # # Напиши программу, которая проверяет, является ли введенное число четным или нечетным.
# # # # # #
# # # # # # inp = int(input("Введите число:"))
# # # # # # if inp %2 == 0:
# # # # # #     print("Четное число")
# # # # # # else:
# # # # # #     print("Нечетное число")
# # # # # #
# # # # # #
# # # # #
# # # # # # Напиши программу, которая проверяет, может ли человек приобрести билет на концерт. На концерт пустают только с 18 лет.
# # # # #
# # # # # age = int(input("Ваш возраст:"))
# # # # #
# # # # # if age >= 18:
# # # # #     print("Вы можете купить билет")
# # # # # else:
# # # # #     print("Иди играй в доту")
# # # #
# # # # # Проверка на положительное, отрицательное или ноль
# # # #
# # # # a = int(input("Введите число:"))
# # # #
# # # # if a > 0:
# # # #     print("Число положительное")
# # # # elif a == 0:
# # # #     print("Число равно нулю")
# # # # else:
# # # #     print("Число отрицательное")
# # #
# # # # Напиши программу, которая сравнивает два числа и выводит
# # #
# # # chisla = input("Введите 2 числа через пробел")
# # # a, b = map(int, chisla.split())
# # # if a > b:
# # #     print("Первое число больше второго")
# # # elif a == b:
# # #     print("Числа равны")
# # # else:
# # #     print("Второе число больше первого")
# #
# # # Напиши программу, которая проверяет, делится ли число на 3.
# #
# # a = int(input("Введите число"))
# # if a %3 == 0:
# #     print("Число",a,"делится на 3")
# # else:
# #     print("Число",a,"не делится на 3")
#
# # Напиши программу, которая принимает список чисел в интервале от -1 до +1 и выводит:
#
# listofvalues = input("введите список чисел состоящих из -1, 0 и 1 через пробел: ")
# cntmone = 0
# cntzero = 0
# cntone = 0
#
# for val in listofvalues.split():
#     if int(val) == -1:
#         cntmone += 1
#     elif int(val) == 0:
#         cntzero += 1
#     elif int(val) == 1:
#         cntone += 1
# print("Кол-во -1: ", cntmone)
# print("Кол-во 0: ", cntzero)
# print("Кол-во 1: ", cntone)

# Соотношение чисел в списке
#
# listofvalues = input("введите список чисел состоящих из -1, 0 и 1 через пробел: ")
# cntmone = 0
# cntzero = 0
# cntone = 0
# cntfull = 0
#
# for val in listofvalues.split():
#     if int(val) == -1:
#         cntmone += 1
#     elif int(val) == 0:
#         cntzero += 1
#     elif int(val) == 1:
#         cntone += 1
#     cntfull += 1
#
# print(f"Значения -1 составляют {cntmone/cntfull*100}% от имеющегося списка")
# print(f"Значения 0 составляют {cntzero/cntfull*100}% от имеющегося списка")
# print(f"Значения 1 составляют {cntone/cntfull*100}% от имеющегося списка")

#Частота вхождений всех возможных значений
#
# listofvalues = input("введите список чисел состоящих из -1, 0 и 1 через пробел: ")
# cntmone = 0
# cntzero = 0
# cntone = 0
# cntfull = 0
# listval2 = []
#
# for val in listofvalues.split():
#     if int(val) == -1:
#         cntmone += 1
#     elif int(val) == 0:
#         cntzero += 1
#     elif int(val) == 1:
#         cntone += 1
#     cntfull += 1
#
# listval2 = {-1:cntmone, 0:cntzero, 1:cntone}
#
# maxval = max(cntmone,cntzero,cntone)
# minval = min(cntmone,cntzero,cntone)
# midval = 0
#
# for l in listval2.values():
#     if l != maxval and l != minval:
#         midval = l
#     else:
#         midval = l
#
# if maxval != midval and maxval != minval:
#     print(f"Значение {next((k for k, v in listval2.items() if v == maxval), None)} встречается чаще остальных")
# if maxval == midval and maxval != minval:
#     print(f"Значения {next((k for k, v in listval2.items() if v == maxval), None)} и {next((k for k, v in listval2.items() if v == midval), None)} встречаются чаще чем {next((k for k, v in listval2.items() if v == minval), None)}")
# if maxval == midval and maxval == minval:
#     print(f"Все три возможных значения всречаются с одинаковой частотой")

#