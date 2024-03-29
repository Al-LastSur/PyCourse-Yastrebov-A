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
# point1En = {"a", "e", "i", "o", "u", "l", "n", "s", "t", "r", "A", "E", "I", "O", "U", "L", "N", "S", "T", "R"}
# point2En = {"d", "g", "D", "G"}
# point3En = {"b", "c", "m", "p", "B", "C", "M", "P"}
# point4En = {"f", "h", "v", "w", "y", "F", "H", "V", "W", "Y"}
# point5En = {"k", "K"}
# point8En = {"j", "x", "J", "X"}
# point10En = {"q","z", "Q", "Z"}

# point1Ru = {"а", "в", "е", "и", "н", "о", "р", "с", "т", "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"}
# point2Ru = {"д", "к", "л", "м", "п", "у", "Д", "К", "Л", "М", "П", "У"}
# point3Ru = {"б", "г", "ё", "ь", "я", "Б", "Г", "Ё", "Ь", "Я"}
# point4Ru = {"й", "ы", "Й", "Ы"}
# point5Ru = {"ж", "з", "х", "ц", "ч", "Ж", "З", "Х", "Ц", "Ч"}
# point8Ru = {"ш", "э", "ю", "Ш", "Э", "Ю"}
# pont10Ru = {"ф", "щ", "ъ", "Ф", "Щ", "Ъ"}

k = 'gameboy'
# alternatively working solution
# Введите ваше решение ниже
scores = {
    'А': 1, 'Б': 3, 'В': 1, 'Г': 3, 'Д': 2, 'Е': 1, 'Ё': 3, 'Ж': 5, 'З': 5,
    'И': 1, 'Й': 4, 'К': 2, 'Л': 2, 'М': 3, 'Н': 1, 'О': 1, 'П': 2, 'Р': 1,
    'С': 1, 'Т': 1, 'У': 2, 'Ф': 10, 'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Щ': 10,
    'Ъ': 10, 'Ы': 4, 'Ь': 3, 'Э': 8, 'Ю': 8, 'Я': 3,
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
    'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
    'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

score = sum(scores.get(letter, 0) for letter in k.upper())
print(score)

