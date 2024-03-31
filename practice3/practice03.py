# # Task 13. Ottepel
# daysCount = int( input ("Input the amount of days here: ", ))
# count = 0
# maxcount = 0
# print(daysCount)
# if daysCount >= 1 and daysCount <= 100:
#     for temperature in range(daysCount):
#         temperature = int(input ("Input the temperature of each day: ", ))
#         if temperature >0:
#             count += 1
#         else:
#             maxcount = max (maxcount, count)
#             count = 0
#     maxcount = max (maxcount, count)
        
#         # temperature = int(input ("Input the temperature of each day: ", ))
#         # if temperature > 0:
            
#         #     count += 1
#         #     if count >= maxcount:
#         #         maxcount = count
#         # else:
#         #     if count >= maxcount:
#         #         maxcount = count
#         #         count = 0
#     print ("The amount of days with temperature > 0 is ", maxcount)

# # Task 15. Watermelons (AKA weights) 48: 08
# melonsCount = int( input ("Input the amount of watermelons here: ", ))
# print(melonsCount)

# for i in range(melonsCount):
#     weight = int(input ("Input the weight of each watermelon: ", ))
#     if weight > 0:
#         if i == 0:
#             melonMin = weight
#             melonMax = weight
#         elif weight < melonMin:
#             melonMin = weight
#         elif weight > melonMax:
#             melonMax = weight
#     else:
#         print("mellons cannot weight zero")
# print(melonMin, melonMax)
# alternative solution 
# n = int(input("Введите число арбузов: "))
# arr = [int(input()) for _ in range(n)]
# print("Мой арбуз весит: ", max(arr))
# print("Арбуз для тёщи весит: ", min(arr))

# # Task 17. Identify amount of different (not similar) numbers
# list_num = [1, 1, 2, 0, -1, 3, 4, 4]
# set_num = set()
# for i in list_num:
#     set_num.add(i)
# print(*set_num)
# print(len(set_num))
# # alternatively
# list_num = [1, 1, 2, 0, -1, 3, 4, 4, 4, 7, 1]
# Num = set(list_num)
# print(len(Num))
# # alternatively
# list_num = [1, 1, 2, 0, -1, 3, 4, 4, 4, 7, 1]
# result_list = list()
# for i in list_num:
#     if i not in result_list:
#         result_list.append(i)
# print(result_list)
# print(len(result_list))

# # Task 19. More the list for K elements count
# #  use of shift
# numbers = [1, 2, 3, 4, 5]
# k = 3
# shifted_numbers = numbers [-k:] + numbers[:-k]
# print (shifted_numbers)
# # alternatively - the output is wrong
# # numbers = [1, 2, 3, 4, 5]
# # k = 3
# print(numbers[k:] + numbers[:k])

# # alternatively with pop - gives wrong output
# numbers = [1, 2, 3, 4, 5]
# k = 3
# for i in range (k):
#     numbers.insert(0, numbers.pop())
# print(numbers)

# Task 21. Print all unique values of the dictionary
# input : [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI":"S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
# # output : {"S005", "S002", "S007", "S001", "S009"}
# dict_1 = [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI":"S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":" S007 "}]
# dict_2 = set()
# for dictionary in dict_1:
#     for value in dictionary.values():
#         dict_2.add(value.strip()) # strip erases all unnesecary spacebars
# print(dict_2)
# # alternatively
# dict_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII":" S007 "}]
# print({list(dict_2.values())[0].strip() for dict_2 in dict_1})

# # Task 23. Count the amount of array element that more than the previous one
# # Input: [0, -1, 5, 2, 3]
# # Output: 2 (-1 < 5, 2 < 3)
# numbers = [0, -1, 5, 2, 3]
# count = 0
# for i in range(1, len(numbers)):
#     if numbers[i] > numbers[i - 1]:
#         count += 1
# print("Количество элементов, больших предыдущего:", count)
# alternatively
numbers = [0, -1, 5, 2, -5]
count = 0
for i in range (1,len(numbers)):
    if numbers [i] > numbers[i-1]:
        count += 1
print (count)
