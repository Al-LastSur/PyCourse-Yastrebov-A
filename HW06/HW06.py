# # Task 1. Identify indexes within the range of meanings (use defs)
# # list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# # min_number = 0
# # max_number = 10

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = -10
# max_number = -4

# for position, i  in enumerate(list_1):
#     if i >= min_number and i <= max_number:
#         print(position)

# Task 2. Progression
# Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , 
# разность d и количество элементов n будет задано автоматически.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
a1 = 2
d = 3
n = 4

list_1 = []
# for i in range (n+1): # uncomment alternatively
for i in range (1, n+1):
    # if i == 0:
    #     i=+1
    # else:
        list_1.append(a1 + (i-1) * d)
for i in list_1:
    print (i)