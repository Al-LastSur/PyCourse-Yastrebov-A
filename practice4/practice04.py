# Task 25. Check if the symbol repeated in a string and show the count of time
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# string = input ("Input a string: ").split()

# result = dict()

# for i in string:
#     if i in result.keys():
#         print(f"{i}_{result[i]}", end= " ")
#         result[i] += 1
#     else:
#         print(i, end = " ")
#         result[i] = 1
# print (result)

# # alternatively - correct output
# input_string = input("Введите строку: ") # Получаем строку от пользователя
# words = input_string.split() # Разбиваем строку на слова

# counter = {} # Создаем пустой словарь для подсчета повторений

# output = [] # Создаем пустой список для формирования выходной строки

# for word in words:
#     if word in counter:
#         counter[word] += 1
#         output.append(f"{word}_{counter[word]}") # Добавляем символ с постфиксом _n
#     else:
#         counter[word] = 0
#         output.append(word) # Добавляем символ без постфикса

# output_string = ' '.join(output) # Преобразуем список в строку с пробелами между элементами
# print(output_string)


# # alternatively
# list_1 = 'a a a b c a a d c d d'
# input_list = list_1.split()

# a = ''
# dict_1 = {}
# for i in input_list:
#     a += i
#     if i in dict_1:
#         dict_1[i] += 1
#         a += f'_{dict_1[i]} '
#     else:
#         dict_1[i] = 0
#         a += ' '
# print(a)

# Task 27. Count the number of words in a string and count the number of unrepeated words

# 1 36 35
