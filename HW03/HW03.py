# # Task 1. Count the same items on a list
# list_1 = [1, 2, 3, 4, 3, 3, 5]
# k = 3
# print(list_1.count(k))

# # Task2. The closest item in the list
# list_1 = [1, 12, 6, 7, 8, 15]
# k = 11
# lowerClose = k - 1
# higherClose = k + 1
# for i in list_1:
#     if i == k:
#         theClosest = k
#         break
#     else:
#         if i == lowerClose and lowerClose!= k:
#             theClosest = lowerClose 
#         elif i == higherClose and higherClose!= k:
#             theClosest = higherClose
# print(theClosest)

# Task 3. Scrable.
point1En = {"a", "e", "i", "o", "u", "l", "n", "s", "t", "r", A, E, I, O, U, L, N, S, T, R}
point2En = {"d", "g" D, G}
point3En = {"b", "c", "m", "p" B, C, M, P}
point4En = {"f", "h", "v", "w", "y" F, H, V, W, Y}
point5En = {"k" K}
point8En = {"j", "x" J, X}
point10En = {"q","z" Q, Z}

point1Ru = {"а", "в", "е", "и", "н", "о", "р", "с", "т" А, В, Е, И, Н, О, Р, С, Т}
point2Ru = {"д", "к", "л", "м", "п", "у" Д, К, Л, М, П, У}
point3Ru = {"б", "г", "ё", "ь", "я" Б, Г, Ё, Ь, Я}
point4Ru = {"й", "ы" Й, Ы}
point5Ru = {"ж", "з", "х", "ц", "ч"Ж, З, Х, Ц, Ч}
point8Ru = {"ш", "э", "ю" Ш, Э, Ю}
pont10Ru = {"ф", "щ", "ъ" Ф, Щ, Ъ}

"""

А русские буквы оцениваются так:

А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
"""
